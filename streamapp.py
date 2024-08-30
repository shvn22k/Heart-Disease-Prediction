import streamlit as st
import numpy as np
import pickle

# load the model
model = pickle.load(open('heartDiseasePrediction.pkl', 'rb'))

# title and description
st.title("Heart Disease Prediction (90.77% Accuracy)")
st.write("Enter the details below to predict the likelihood of heart disease.")

# taking inputs
age = st.number_input("Age:", min_value=5, max_value=110, value=30)
sex = st.radio("Gender:", options=["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type:", options=[
    "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic Pain"
])
bp = st.number_input("Blood Pressure (mmHg):", min_value=80, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol (mg/dl):", min_value=100, max_value=500, value=200)
fbs = st.radio("Is your FBS (fasting blood sugar) over 120?", options=["Yes", "No"])
ekg = st.selectbox("ECG Test Results:", options=[
    "Normal", "Having ST-T wave abnormality", "Probable ventricular hypertrophy"
])
max_hr = st.number_input("Maximum Heart Rate:", min_value=60, max_value=220, value=150)
ex_angina = st.radio("Do you have exercise angina?", options=["Yes", "No"])
st_depression = st.number_input("ST Depression:", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.selectbox("ST Depression Slope:", options=[
    "Unsloping", "Flat", "Downsloping"
])
vessels = st.number_input("Number of Major Vessels:", min_value=0, max_value=3, value=0)
thallium = st.selectbox("Thallium Scan Results:", options=[
    "Normal", "Fixed Defect", "Reversible Defect"
])

# converting categorical inputs to numerical
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "Yes" else 0
ex_angina = 1 if ex_angina == "Yes" else 0
chest_pain = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic Pain"].index(chest_pain) + 1
ekg = ["Normal", "Having ST-T wave abnormality", "Probable ventricular hypertrophy"].index(ekg)
st_slope = ["Unsloping", "Flat", "Downsloping"].index(st_slope) + 1
thallium = 3 if thallium == "Normal" else 6 if thallium == "Fixed Defect" else 7 if thallium == "Reversible Defect" else 0

# predict button
if st.button("Predict"):
    input_data = np.array([age, sex, chest_pain, bp, cholesterol, fbs, ekg, max_hr, ex_angina, st_depression, st_slope, vessels, thallium]).reshape(1, -1)
    prediction = model.predict(input_data) # make predictions
    
    if prediction[0] == "Presence":
        st.error("You may have a heart disease. 😔")
    elif prediction[0] == "Absence":
        st.success("You don't have a heart disease. 😊")
    else:
        st.error("Error 🤖")


