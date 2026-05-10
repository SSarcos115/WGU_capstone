import joblib
import pandas as pd

def species_df():
    return pd.read_excel(
    "data/aquarium_fish_ml_dataset.xlsx",
    sheet_name="Species_Info"
)

def pair_df():
    return pd.read_excel(
    "data/aquarium_fish_ml_dataset.xlsx",
    sheet_name="Pair_Compatibility_ML"
)

def load_model():
    return joblib.load("models/compatibility_model.pkl")