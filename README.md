# Simple-Forest-Fire-Predictor
A basic Flask web app that predicts the Forest Fire Weather Index (FWI) using a machine learning Ridge Regression model.
Just input simple weather parameters and get an instant prediction of fire risk.

🌐 Click here to use the live app

📌 Features
Predict FWI (Fire Weather Index) using user input

Deployed with Render

Clean UI with form-based inputs

Lightweight and beginner-friendly structure
## 📁 Project Structure
simple-forest-fire-predictor/
│
├── application.py # Main Flask app
│
├── models/
│ ├── ridge.pkl # Trained Ridge Regression model
│ └── scaler.pkl # StandardScaler used for input normalization
│
├── templates/
│ ├── index.html # Welcome page (says: "Welcome to the home page")
│ └── home.html # Main input form for prediction
│
├── notebooks/
│ ├── FWI_Predictor.ipynb # Jupyter notebook used for model training and testing
│ └── data.csv # Dataset used (or other reference materials)
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
