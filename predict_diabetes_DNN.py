# importing Important Liberaries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes_dnn = pickle.load(open('model_diabetes_dnn.sav', 'rb'))

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
  _SMOKER3 = st.selectbox(
    'Apakah Anda Merokok',
    ('Tidak', '<20bks/thn', '20-30bks/thn'))

with col2 :
  _TOTINDA = st.selectbox(
    'Apakah Melakukan Aktifitas Fisik',
    ('Tidak', 'Ya, TIdak Setiap Hari', 'Ya, Setiap Hari'))

with col1 :
  _BMI5CAT = st.selectbox(
    'Indeks Masa Tubuh Anda',
    ('Pilih Indeks Masa Tubuh', 'Kekurangan Berat Badan', 'Berat Badan Normal', 'Kelebihan Berat Badan', 'Obesitas'))

with col2 :
  DIABETE4 = st.selectbox(
    'Riwayat Diabetes Pada Diri Sendiri',
    ('Pilih Riwayat Diabetes', 'Tidak', 'Iya', 'Tidak Tahu'))

# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
  diabetes_prediction = model_diabetes.predict([[SEXVAR,_AGEG5Y,_SMOKER3,_TOTINDA,_BMI5CAT,DIABETE4]])
  
  if(diabetes_prediction[0]==1):
    diabetes_diagnosis = 'The patient has diabetes'
  else :
    diabetes_diagnosis = 'The patient does not have diabetes'

#st.success(diabetes_diagnosis)
