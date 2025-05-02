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
with st.sidebar:
    st.header("About")
    your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py
    options = ["Buah", "Vitamin", "Manfaat", "Kekurangan"]
    selection = st.page_link('ingin tau tentang?', options, selection_mode="multi")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
