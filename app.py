from flask import Flask, request, jsonify
from soh_model import load_model, predict_soh

app = Flask(__name__)

model, features = load_model()

def classify(soh, threshold):
    return "Healthy" if soh >= threshold else "Problem"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "inputs" not in data:
        return jsonify({"error": "Missing 'inputs'"}), 400

    threshold = float(data.get("threshold", 0.6))

    try:
        soh = predict_soh(model, features, data["inputs"])
        status = classify(soh, threshold)
        return jsonify({"soh": soh, "status": status})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/hello", methods=["GET"])
def hello():
    return {"message": "Backend is running!"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)
