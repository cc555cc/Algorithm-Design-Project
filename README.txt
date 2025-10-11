Battery Pack SOH Prediction - Milestone 1
----------------------------------------

Project Objective:
Train and evaluate a Linear Regression model to predict the State of Health (SOH) of battery packs
using the PulseBat Dataset.

Files Included:
- soh_model.py
- PulseBat Dataset.xlsx
- soh_predictions.csv (generated after running)
- explanatory_doc.txt

-----------------------------
SETUP AND RUN INSTRUCTIONS:
-----------------------------
1. Make sure Python 3.x is installed.
2. Install the required libraries:
   pip install pandas numpy scikit-learn openpyxl

3. Place the following files in the same folder:
   - soh_model.py
   - PulseBat Dataset.xlsx

4. Open a terminal or VS Code and run:
   python soh_model.py

5. The script will:
   - Load and preprocess the dataset.
   - Train a Linear Regression model.
   - Evaluate performance metrics (R², MSE, MAE).
   - Apply a 0.6 threshold to classify battery health.
   - Save results in `soh_predictions.csv`.

-----------------------------
EXPECTED OUTPUT:
-----------------------------
Terminal will display:
R² Score: ...
MSE: ...
MAE: ...

soh_predictions.csv will contain:
SOH | Predicted SOH | Battery Status
