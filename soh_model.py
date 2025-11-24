import joblib
import pandas as pd

def load_model():
    model = joblib.load("model.pkl")
    features = joblib.load("features.pkl")
    return model, features

def predict_soh(model, features, values_dict):
    row = {f: values_dict.get(f) for f in features}
    df = pd.DataFrame([row])

    if df.isnull().any(axis=None):
        missing = df.columns[df.isnull().any()].tolist()
        raise ValueError(f"Missing values: {missing}")

    return float(model.predict(df.values)[0])
