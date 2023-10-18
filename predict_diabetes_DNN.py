# Importing the necessary Python modules.
import streamlit as st

# Import pages
from pages import home, data, prediksi, visualisasi, about

# Configure the app
st.set_page_config(
    page_title = 'Prediksi Diabetes Menggunakan Deep Neural Network',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)
