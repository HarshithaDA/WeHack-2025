from flask import Flask, request, jsonify
from bot import predict_and_respond, gemini_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the homepage!"

@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    data = request.json
    user_id = data["user_id"]
    input_data = data["input"]

    risk, explanation = predict_and_respond(user_id, input_data)
    return jsonify({
        "risk": risk,
        "explanation": explanation
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data["user_id"]
    user_input = data["message"]

    response = gemini_response(user_id, user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
