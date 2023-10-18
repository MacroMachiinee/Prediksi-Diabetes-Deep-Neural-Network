# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Import pages
#from pages import home, data, predict, visualise, about

# Load model

# Web Title
st.title('Prediksi Diabetes Dengan Deep Neural Network')

st.markdown(
    """<p style="font-size:20px;">
            Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
            There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
            This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.
        </p>

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
