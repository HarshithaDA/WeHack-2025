import os
import google.generativeai as genai
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import joblib

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load trained ML model
model = joblib.load("risk_model.pkl")

# Connect to MongoDB
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client.investbot
user_col = db.users

# Risk explanation logic
def explain_risk(data):
    explanation = []
    if data["avg soil moisture"] < 0.2:
        explanation.append("Low soil moisture may indicate poor vegetation or land issues.")
    if data["avg soil moisture"] > 0.6:
        explanation.append("High soil moisture might suggest drainage problems.")
    if data["avg temp"] > 40:
        explanation.append("Extreme temperature may increase maintenance costs.")
    if data["avg noise sensor value"] > 65:
        explanation.append("Noise levels are high, which may affect livability.")
    if data["Crime Index"] > 2:
        explanation.append("High crime rate could reduce buyer interest and safety.")
    return " ".join(explanation) if explanation else "No major risks detected."

# Predict and explain
def predict_and_respond(user_id, input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    explanation = explain_risk(input_data)

    # Log interaction in MongoDB
    user_col.update_one(
        {"user_id": user_id},
        {"$push": {"history": {
            "input": input_data,
            "risk": prediction,
            "explanation": explanation
        }}},
        upsert=True
    )

    return prediction.capitalize(), explanation

# Gemini response logic
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_response(user_id, user_input):
    user_data = user_col.find_one({"user_id": user_id}) or {"history": []}

    prompt = f"""
You are Finvestigator, a smart investment detective helping users spot hidden risks and suggest smart strategies.

User ID: {user_id}
User History: {user_data['history']}
User Question: {user_input}
"""
    print("Using Gemini version:", genai.__file__)


    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini API Error: {str(e)}"
