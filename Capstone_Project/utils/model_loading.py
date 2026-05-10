import joblib


def load_model(file_path="models/compatibility_model.pkl"):
    return joblib.load(file_path)