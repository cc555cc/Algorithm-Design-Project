import pandas as pd
from soh_model import train, predict

def test():
    # Train model using your existing training function
    train()

    # Load dataset
    data = pd.read_excel("PulseBat Dataset.xlsx")
    data = data.dropna(subset=["SOH"])

    # Extract U1–U21 columns (same way as in soh_model.py)
    cell_columns = [col for col in data.columns if col.startswith("U")]

    # Show descriptive stats of the voltage columns
    print("=== VOLTAGE STATS ===")
    print(data[cell_columns].describe())

    # Test prediction on first real row
    row = data.iloc[0]
    true_soh = row["SOH"]
    voltages = row[cell_columns].tolist()

    print("\n=== REAL ROW PREDICTION ===")
    print("True SOH:", true_soh)
    print("Predicted SOH:", predict(voltages))

