import streamlit as st
import math

st.set_page_config(page_title="Pengenalan Bahan Pangan dan Vitamin Yang Terkandung", layout="centered")

# Title
st.title("🍎Bahan Pangan dan Vitamin Yang Terkandung🍎")

# Description
st.write("""
Aplikasi ini memberikan informasi mengenai jenis bahan pangan serta kandungan vitamin didalam-nya serta manfaat-nya.
""")

# Sidebar for input
with st.sidebar:
    st.header("About")
    options = ["Bahan Pangan", "Vitamin", "Manfaat", "Kekurangan"]
    selection = st.pills("Tentang", options, selection_mode="multi")
    st.markdown(f"Your selected options: {selection}.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
