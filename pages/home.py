"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Prediksi Diabetes Menggunakan Deep Neural Network")

    # Add image to the home page
    #st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
    Diabetes adalah penyakit kronis yang ditandai dengan tingginya kadar gula darah. Gula darah adalah sumber energi utama bagi sel tubuh manusia. Akan tetapi, pada penderita diabetes, glukosa tersebut tidak dapat digunakan oleh tubuh.
    Kadar gula darah dikendalikan oleh hormon insulin yang diproduksi pankreas. Namun, pada penderita diabetes, pankreas tidak mampu memproduksi insulin sesuai kebutuhan tubuh. Tanpa insulin, sel-sel tubuh tidak dapat menyerap dan mengolah glukosa menjadi energi.
    Ada dua jenis diabetes, yaitu diabetes tipe 1 dan diabetes tipe 2. Diabetes tipe 1 adalah penyakit autoimun yang menyebabkan sistem kekebalan tubuh menyerang dan menghancurkan sel-sel penghasil insulin di pankreas. Diabetes tipe 2 adalah penyakit yang disebabkan oleh kombinasi faktor genetik, gaya hidup, dan obesitas.
    Dataset ini berasal dari POSBINDU Puskesmas Mergangsan. Tujuan dari kumpulan data ini adalah untuk memprediksi secara diagnostik apakah pasien menderita diabetes atau tidak, berdasarkan pengukuran diagnostik tertentu yang disertakan dalam kumpulan data. Beberapa batasan ditempatkan pada pemilihan contoh-contoh ini dari basis data yang lebih besar.
        </p>
    """, unsafe_allow_html=True)
