# 🧠 Capital Agent — Built for Beginners. Powered for Pros.

> _Timeless decisions for timeless returns_  
> 🏆 WeHack Hackathon 2025 — Theme: **Timeless Moments Await**

---

## 🕵️‍♀️ Project Vision

**Capital Agent** is your AI-powered investment advisor designed to make property and stock investments smarter, safer, and more strategic.

In a world full of financial complexity, hidden risks, and fast-moving markets, our app acts as a **virtual detective**. It analyzes real estate and stock data (with sensor inputs, crime indexes, market sentiment, and more) to:
- 📈 Predict value trends (5 & 10 years ahead)
- 🚨 Assess investment risk (Low / Medium / High)
- 💬 Provide tailored, conversational financial advice using Gemini AI
- 🔄 Recommend portfolio diversification based on historical behavior

Whether you're a seasoned investor or a curious beginner, **Capital Agent** brings clarity to your financial choices — making every moment a timeless one.

---

## 🧰 Tech Stack

| Layer          | Tools & Libraries                                           |
|----------------|-------------------------------------------------------------|
| 💬 Conversational AI | Gemini API (Google Generative AI)                     |
| 📊 ML Models         | LSTM, Sentiment Analysis (custom-trained models)      |
| 📦 Backend           | Flask, Python, scikit-learn, Pandas                   |
| 🧠 Database          | MongoDB Atlas (for user history & investment logs)    |
| 📁 IDE & Dev         | VSCode, Python virtual environments                   |
| 🎨 UI/UX             | Figma (designed for future front-end integration)     |

---

## 🧑‍🤝‍🧑 Team Capital Agents

- Varsha (AI + ML Modeling)
- Harshitha (Data Processing + Risk Classification)
- Nanddanaa (Sentiment Analysis + Integration)
- Chinmayi (Conversational Design + Gemini API + UI Concepts)

---

## 📦 Features

- 🏠 **Property Risk Analysis**  
  Upload sensor data + transaction info to get:
  - 5-year and 10-year value estimates  
  - High/Medium/Low investment risk  
  - Explanation of risk (based on noise, temperature, soil moisture, crime rate)

- 📈 **Stock Sentiment Insights**  
  Analyze past stock trends + news-based sentiment to:
  - Predict short/long-term performance  
  - Warn users about risky behavior  
  - Recommend diversified options

- 💬 **Conversational AI Advisor**  
  Ask Gemini-powered chatbot questions like:  
  _“Should I invest in more properties in this area?”_  
  _“What’s the trend for my stock in 5 years?”_  
  The bot will use your own historical investments to guide you intelligently.

---

## 📁 Dataset

> 📌 **Self-Generated Datasets**
- Property data simulated with sensor values + transaction logs
- Stock data scraped and sentiment-scored from mock news headlines

---

## 🚀 How to Run (Local)

1. Clone the repo  
   `git clone https://github.com/<your-team>/capital-agent.git`

2. Create virtual environment  
   `python -m venv venv && .\venv\Scripts\activate`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Set up `.env` file (sample below):

```env
GEMINI_API_KEY=your_gemini_api_key_here
MONGO_URI=your_mongo_uri_here
