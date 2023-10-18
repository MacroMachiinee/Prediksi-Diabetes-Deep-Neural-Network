# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Import pages
#from pages import home, data, predict, visualise, about

# Load model

# Web Title
st.title('Prediksi Diabetes Dengan Deep Neural Network')

st.write("Diabetes adalah penyakit kronis yang ditandai dengan tingginya kadar gula darah. Gula darah adalah sumber energi utama bagi sel tubuh manusia. Akan tetapi, pada penderita diabetes, glukosa tersebut tidak dapat digunakan oleh tubuh.")
st.write("Kadar gula darah dikendalikan oleh hormon insulin yang diproduksi pankreas. Namun, pada penderita diabetes, pankreas tidak mampu memproduksi insulin sesuai kebutuhan tubuh. Tanpa insulin, sel-sel tubuh tidak dapat menyerap dan mengolah glukosa menjadi energi.")
st.write("Ada dua jenis diabetes, yaitu diabetes tipe 1 dan diabetes tipe 2. Diabetes tipe 1 adalah penyakit autoimun yang menyebabkan sistem kekebalan tubuh menyerang dan menghancurkan sel-sel penghasil insulin di pankreas. Diabetes tipe 2 adalah penyakit yang disebabkan oleh kombinasi faktor genetik, gaya hidup, dan obesitas.")
st.write("-----------------------------------------------------------------------------------------------------------")

st.title("Prediksi Diabetes")

# Split Columns
col1, col2 = st.columns(2)

with col1 :
  SEXVAR = st.selectbox(
    'Jenis Kelamin',
    ('Pilih Jenis Kelamin', 'Laki Laki', 'Perempuan'))

with col2 :
  _AGEG5YR = st.selectbox(
    'Rentang Umur',
    ('Pilih Jenis Rentang Umur', '18 - 24', '25 - 29', '30 - 34', '35 - 39', '40 - 44', '45 - 49', '50 - 54', '55 - 59', '60 - 64', '65 - 69', '70 - 74', '75 - 79', '80 - Lebih Tua'))
  
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
