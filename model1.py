import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("hr_performance_dataset.csv")

# Create performance column (3 classes)
def get_performance(row):
    if row["satisfaction_level"] >= 0.75 and row["last_evaluation"] >= 0.75:
        return "High"
    elif row["satisfaction_level"] >= 0.45 and row["last_evaluation"] >= 0.45:
        return "Average"
    else:
        return "Low"

data["performance"] = data.apply(get_performance, axis=1)

# Features
X = data[
    [
        "satisfaction_level",
        "last_evaluation",
        "number_project",
        "average_montly_hours",
        "time_spend_company",
    ]
]

# Target (NOW 3 classes)
y = data["performance"]

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully with 3 classes!")
