import os

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

features = [
    "Same Water Type",
    "Temperature Overlap Ratio",
    "pH Overlap Ratio",
    "Salinity Overlap Ratio",
    "Tank Requirement Similarity",
    "Adult Size Ratio",
    "Predation Size Risk",
    "Temperament Risk",
    "Diet/Predation Risk",
    "Water Level Compatibility",
    "Schooling Conflict",
    "Reef Safety Conflict",
    "Same Group Aggression Conflict"
]

target = "Compatibility Label Code"

def train_model(pair_df):
    X = pair_df[features]
    y = pair_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    compatibility_model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    compatibility_model.fit(X_train, y_train)

    predictions = compatibility_model.predict(X_test)

def save_model(model, file_path="models/compatibility_model.pkl"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, file_path)