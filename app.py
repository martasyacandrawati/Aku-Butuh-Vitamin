import streamlit as st
import math

st.set_page_config(page_title="Buah dan Vitamin Didalam-nya", layout="centered")

# Title
st.title("🍎Buah dan Vitamin Didalam-nya")

# Description
st.write("""
Aplikasi ini memberikan informasi mengenai buah dan kandungan vitamin didalam-nya serta manfaat vitamin yang terkandung.
""")

# Sidebar for input
st.header("Menu")
    selection = st.radio("About", ["Kenali Vitamin", "Manfaat Vitamin", "Fungsi Vitamin", "Kekurangan", "Fakta Menarik"])

# Konten berdasarkan pilihan
if selection == "Kenali Vitamin":
    st.write("Ini konten untuk Kenali Macam-macam Vitamin.")
elif selection == "Manfaat Vitamin":
    st.write("Ini konten untuk Mengetahui Manfaat Vitamin.")
elif selection == "Fungsi Vitamin":
    st.write("Ini konten Mengetahui Fungsi Vitamin.")
elif selection == "Kekurangan":
    st.write("Ini konten untuk Mengetahui Kekurangan.")
elif selection == "Fakta Menarik":
    st.write("Ini konten untuk Mengetahui Fakta Menarik Vitamin.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
