
from flask import Flask, request, jsonify, g
import pandas as pd
import joblib
import logging
import time
from datetime import datetime

app = Flask(__name__)

# Memuat pipeline preprocessing dan model
model = joblib.load("netflix_model.pkl")

FEATURES = [
    "type", "title", "director", "cast", "country",
    "date_added", "rating", "duration", "listed_in",
    "description"
]

# Menyimpan log monitoring ke file
logging.basicConfig(
    filename="api_monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Metrik selama server berjalan
metrics = {
    "total_requests": 0,
    "successful_predictions": 0,
    "failed_requests": 0,
    "total_response_time_ms": 0.0
}


@app.before_request
def start_monitoring():
    g.start_time = time.perf_counter()


@app.after_request
def record_monitoring(response):
    elapsed_ms = (
        time.perf_counter() - g.start_time
    ) * 1000

    metrics["total_requests"] += 1
    metrics["total_response_time_ms"] += elapsed_ms

    if request.path == "/predict":
        if response.status_code < 400:
            metrics["successful_predictions"] += 1
        else:
            metrics["failed_requests"] += 1

    logging.info(
        "method=%s path=%s status=%s response_time_ms=%.2f",
        request.method,
        request.path,
        response.status_code,
        elapsed_ms
    )

    response.headers["X-Response-Time-ms"] = f"{elapsed_ms:.2f}"
    return response


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "message": "Netflix Release Year Prediction API"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict) or not data:
            return jsonify({
                "error": "Kirim satu objek JSON yang valid."
            }), 400

        missing = [col for col in FEATURES if col not in data]
        if missing:
            return jsonify({
                "error": "Fitur belum lengkap.",
                "missing_features": missing
            }), 400

        X_new = pd.DataFrame([
            {col: data[col] for col in FEATURES}
        ])

        prediction = model.predict(X_new)

        return jsonify({
            "predicted_release_year": int(
                round(float(prediction[0]))
            )
        })

    except Exception:
        logging.exception("Prediction failed")
        return jsonify({
            "error": "Prediksi gagal. Periksa log aplikasi."
        }), 500


@app.route("/monitoring", methods=["GET"])
def monitoring():
    total = metrics["total_requests"]
    avg_ms = (
        metrics["total_response_time_ms"] / total
        if total > 0 else 0
    )

    return jsonify({
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "total_requests": total,
        "successful_predictions": metrics[
            "successful_predictions"
        ],
        "failed_requests": metrics["failed_requests"],
        "average_response_time_ms": round(avg_ms, 2),
        "log_file": "api_monitoring.log"
    })


if __name__ == "__main__":
    app.run(host='127.0.0.1',
            port=5000,
            debug=False,
            use_reloader=False
            )