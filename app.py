
from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Memuat model dari folder yang sama dengan app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "netflix_model.pkl")

model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Netflix Release Year Prediction API",
        "status": "running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict) or not data:
            return jsonify({
                "error": "Kirim satu objek JSON berisi fitur."
            }), 400

        # Mengubah input menjadi DataFrame
        X_new = pd.DataFrame([data])

        # Melakukan prediksi
        prediction = model.predict(X_new)

        return jsonify({
            "predicted_release_year": int(
                round(float(prediction[0]))
            )
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)