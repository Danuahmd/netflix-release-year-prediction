from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Memuat pipeline preprocessing dan model
model = joblib.load("netflix_model.pkl")

FEATURES = [
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "rating",
    "duration",
    "listed_in",
    "description"
]

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
                "error": "Kirim satu objek JSON berisi data fitur."
            }), 400

        missing = [col for col in FEATURES if col not in data]
        if missing:
            return jsonify({
                "error": "Fitur berikut belum dikirim.",
                "missing_features": missing
            }), 400

        X_new = pd.DataFrame(
            [{col: data[col] for col in FEATURES}]
        )

        prediction = model.predict(X_new)

        return jsonify({
            "predicted_release_year": int(round(float(prediction[0])))
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)