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

# Dictionary for pages
pages = {
    "Home": home,
    "Data Info": data,
    "Prediction": prediksi,
    "Visualisation": visualisasi,
    "About me": about
  }

# Create a sidebar
# Add title to sidear
st.sidebar.title("Navigasi")

# Create radio option to select the page
page = st.sidebar.radio("pages", list(pages.keys()))
