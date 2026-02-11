import streamlit as st
import numpy as np
import joblib

# Load Model & Scaler
model = joblib.load("heart_rf_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Heart Disease Predictor")

st.title("Heart Disease Prediction App")

st.write("Enter Patient Details Below:")

# Inputs
age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.number_input("Chest Pain Type (0-3)", 0, 3)
trestbps = st.number_input("Resting BP", 80, 200)
chol = st.number_input("Cholesterol", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.number_input("Rest ECG (0-2)", 0, 2)
thalach = st.number_input("Max Heart Rate", 60, 220)
oldpeak = st.number_input("Oldpeak", 0.0, 6.0)

# Encode sex
sex = 1 if sex == "Male" else 0

# Predict Button
if st.button("Predict"):

    data = np.array([[age, sex, cp, trestbps, chol,
                      fbs, restecg, thalach, oldpeak]])

    data = scaler.transform(data)

    pred = model.predict(data)

    if pred[0] == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk - Healthy")
