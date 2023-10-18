# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Import pages
from pages import home, data, predict, visualise, about

# Load model


# Configure the app
st.set_page_config(
    page_title = 'Prediksi Diabetes Menggunakan Deep Neural Network,
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.number_input('Enter the Pregnancies value')

with col2 :
  Glucose = st.number_input('Enter the Glucose value')
  
with col1 :
  BloodPressure = st.number_input('Enter the Blood Pressure value')

with col2 :
  SkinThickness = st.number_input('Enter the Skin Thickness value')

with col1 :
  Insulin = st.number_input('Enter the Insulin value')

with col2 :
  BMI = st.number_input('Enter the BMI value')

with col1 :
  DiabetesPedigreeFunction = st.number_input('Enter the Diabetes Pedigree Function value')

with col2 :
  Age = st.number_input('Enter the Age value')
  
st.button('Diabetes Prediction Test')
