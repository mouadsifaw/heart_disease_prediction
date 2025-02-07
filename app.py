import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Function to make predictions
def predict_heart_disease(input_data):
    prediction = model.predict(input_data)
    return prediction

# Page Configuration
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# App Title
st.markdown("<h2 style='text-align: center; color: red;'>❤️ Heart Disease Prediction App</h2>", unsafe_allow_html=True)
st.write("This app predicts the likelihood of heart disease based on user input.")

# Sidebar for Input Features
st.sidebar.header("🩺 Enter Patient Details")
cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
thalach = st.sidebar.slider("Maximum Heart Rate Achieved", 60, 220, 120)
exang = st.sidebar.radio("Exercise Induced Angina", [0, 1], index=0)
oldpeak = st.sidebar.slider("Oldpeak (Depression Level)", 0.0, 6.0, 1.0)
slope = st.sidebar.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.sidebar.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])
thal = st.sidebar.selectbox("Thalassemia Type", [0, 1, 2, 3])

# Format input as DataFrame
input_data = pd.DataFrame([[cp, thalach, exang, oldpeak, slope, ca, thal]], 
                           columns=['cp', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

# Predict Button
if st.button("🔍 Predict"):
    prediction = predict_heart_disease(input_data)
    
    if prediction == 1:
        st.error("🚨 **High Risk of Heart Disease!** Please consult a doctor immediately.", icon="⚠️")
    else:
        st.success("✅ **No Heart Disease Detected!** Maintain a healthy lifestyle.", icon="💖")

# Footer
st.markdown("<p style='text-align: center; color: grey;'>Developed by MOUAD AIT KHOUYA | Powered by Machine Learning</p>", unsafe_allow_html=True)
