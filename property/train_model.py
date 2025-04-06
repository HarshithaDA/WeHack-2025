# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load training data
df = pd.read_csv("property_train_dataset_fixed.csv")

# Feature columns (modify if needed)
features = ["avg soil moisture", "avg temp", "avg noise sensor value","avg voltage","Zip Code","Crime Index"]
X = df[features]

# Target column: RiskLevel (0 = Low, 1 = Medium, 2 = High)
y = df["Risk"]

# Train/test split for validation (optional)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "risk_model.pkl")

print("✅ Risk model trained and saved as risk_model.pkl")
