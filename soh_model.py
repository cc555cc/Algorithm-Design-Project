# Project: Battery Pack SOH Prediction 
# Date: October 12, 2025
# Description: Train and evaluate a Linear Regression model on PulseBat Dataset

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

#default dataset
file = pd.read_excel('PulseBat Dataset.xlsx')

#global variables
current_model = None
cell_columns = None
df = file

def train(df):
    global current_model, cell_columns
    # ======================
    # 1. LOAD DATA
    # ======================
    data = df

    # ======================
    # 2. PREPROCESSING
    # ======================
    # Used the read_data() logic was meant to extract numeric cell values per row (U1–U21)
    #cleaned and handled missing or invalid entries here.

    # sorting the dataset by battery packs' ID
    data = data.sort_values(by=['Mat', 'No.', 'ID'], ascending=True, ignore_index=True)

    # Extract U1–U21 columns (cell voltages)
    cell_columns = [col for col in data.columns if col.startswith('U')]
    data = data.dropna(subset=['SOH'])  # ensure SOH is present
    data['avg_voltage'] = data[cell_columns].mean(axis=1)  # aggregate cell voltages

    # Define features (independent variables)
    X = data[cell_columns + ['avg_voltage']].values

    # Define target (dependent variable)
    y = data['SOH'].values

    # ======================
    # 3. SPLIT DATA
    # ======================
    # Previously used random selection for 20%; we'll use sklearn for cleaner reproducibility
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )

    # ======================
    # 4. TRAIN LINEAR REGRESSION MODEL
    # ======================
    current_model = LinearRegression()
    current_model.fit(X_train, y_train)
 

    # ======================
    # 5. EVALUATE MODEL
    # ======================
    y_pred = current_model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print("=== MODEL EVALUATION RESULTS ===")
    print(f"R² Score: {r2:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.6f}")
    print(f"Mean Absolute Error (MAE): {mae:.6f}")

    # ======================
    # 6. CLASSIFICATION USING THRESHOLD
    # ======================
    # ask user for battery threshold value
    #threshold = float(input("Enter battery classification threshold: "))

    #data['Predicted SOH'] = current_model.predict(X)
    #data['Battery Status'] = np.where(data['Predicted SOH'] >= threshold, 'Healthy', 'Problem')

    # Save output for verification
    #data[['SOH', 'Predicted SOH', 'Battery Status']].to_csv('soh_predictions.csv', index=False)
    #print("\nResults saved to soh_predictions.csv")


def predict(battery_cell_value):
    global current_model, cell_columns

    if current_model is None:
        raise Exception("No linear regression model is defined at the moment")
    
    if len(battery_cell_value) != 21:
        raise ValueError("Unable to predict battery SOH because not all 21 voltage of the battery cells are provided")
    
    avg_voltage = np.mean(battery_cell_value)
    features = np.append(battery_cell_value,avg_voltage).reshape(1,-1)

    return float(current_model.predict(features)[0])




