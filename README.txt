Battery Pack SOH Prediction with AI Chatbot
============================================

Project Objective:
Train and evaluate a Linear Regression model to predict the State of Health (SOH) of battery packs
using the PulseBat Dataset. Integrate with Google Gemini AI to provide an intelligent chatbot
interface for battery health predictions.

============================================
SETUP AND RUN INSTRUCTIONS:
============================================

1. PREREQUISITES
   - Python 3.7 or higher installed
   - Internet connection (for Gemini API)

2. INSTALL DEPENDENCIES
   Run this command in the project directory:
   
   pip install pandas numpy scikit-learn openpyxl streamlit google-genai python-dotenv

   Required packages:
   - pandas, numpy: Data processing and numerical operations
   - scikit-learn: Machine learning (Linear Regression)
   - openpyxl: Reading Excel files (PulseBat Dataset)
   - streamlit: Web UI framework
   - google-genai: Google Gemini AI integration
   - python-dotenv: Environment variable management

3. CONFIGURE GEMINI API (OPTIONAL)
   To use the AI chatbot features:
   a) Create a .env file in the project root
   b) Add your Gemini API key:
      GEMINI_AI_KEY=your_api_key_here
   
   Note: If no API key is provided, the chatbot will use default configuration.

4. RUN THE APPLICATION
   Open a terminal in the project directory and run:
   
   python main.py

5. ACCESS THE WEB INTERFACE
   - Open your browser and go to: http://localhost:8501
   - Navigate between "Chatbot" and "Dataset" tabs using the sidebar
   - Interact with the Battery Health Chatbot

============================================
WHAT THE APPLICATION DOES:
============================================

1. MODEL TRAINING
   - Loads the PulseBat Dataset from the Excel file
   - Preprocesses data: sorts by material/ID, removes missing values
   - Extracts 21 cell voltage features (U1-U21) and computes average voltage
   - Splits data into 80% training and 20% testing sets
   - Trains a Linear Regression model using scikit-learn
   - Evaluates performance using R², MSE, and MAE metrics

2. CHATBOT INTERFACE
   - Accepts natural language queries about battery health
   - Uses Google Gemini AI to understand user intent
   - Classifies queries as either PREDICT (battery SOH prediction) or GENERAL (FAQ)
   - For predictions: Extracts 21 cell voltage values from user input
   - Runs predictions through the trained model
   - Returns human-readable explanations of battery health status

3. DATASET VIEWER
   - Displays the PulseBat Dataset in an interactive table
   - Allows users to upload new Excel files for exploration

============================================
EXPECTED MODEL PERFORMANCE:
============================================

After training, the model displays:
R² Score: 0.63 (explains ~63% of variance)
Mean Squared Error (MSE): ~0.0015
Mean Absolute Error (MAE): ~0.03 (3% average error)

Battery Classification:
- Healthy: SOH ≥ 0.6 (60%)
- Problem: SOH < 0.6 (60%)

============================================
FILES INCLUDED:
============================================

Core Application:
- main.py: Entry point - trains model and launches UI
- soh_model.py: Linear Regression model, training, and prediction logic
- UI.py: Streamlit main page layout
- chatbot.py: Chatbot UI component
- datasetDisplay.py: Dataset viewer component
- gemini_api.py: Google Gemini AI integration

Data:
- PulseBat Dataset.xlsx: Raw battery measurement data

Documentation:
- README.txt: This file (quick start guide)
- COMPREHENSIVE_GUIDE.md: Detailed technical documentation
- explanatory_doc.txt: Previous documentation

Configuration:
- package.json: JavaScript/Node dependencies
- .env (optional): Environment variables for API keys

============================================
TROUBLESHOOTING:
============================================

Issue: "ModuleNotFoundError: No module named 'streamlit'"
Solution: Run: pip install streamlit

Issue: "FileNotFoundError: PulseBat Dataset.xlsx not found"
Solution: Ensure PulseBat Dataset.xlsx is in the project root directory

Issue: "Gemini API Error"
Solution: Check your internet connection and API key in .env file

Issue: "SyntaxError in chatbot.py"
Solution: Ensure you have the latest version of the code with proper Python syntax

============================================
QUICK START SUMMARY:
============================================

1. pip install pandas numpy scikit-learn openpyxl streamlit google-genai python-dotenv
2. python main.py
3. Open http://localhost:8501 in your browser
4. Use the Chatbot tab to ask about battery health predictions
5. Use the Dataset tab to view the raw data
