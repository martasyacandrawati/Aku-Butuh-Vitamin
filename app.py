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
    st.page_link("your_app.py", label="Home", icon="🏠")
    st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
    st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
    st.page_link("http://www.google.com", label="Google", icon="🌎")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
