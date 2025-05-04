import streamlit as st
import math

st.set_page_config(page_title="Buah dan Vitamin Didalam-nya", layout="centered")

# Sidebar for input
with st.sidebar:
    st.header("Menu")
    selection = st.radio("Ingin tahu tentang apa?", ["Kenali Vitamin", "Manfaat Vitamin", "Fungsi Vitamin", "Kekurangan", "Fakta Menarik"])

# Konten berdasarkan pilihan
if selection == "Kenali Vitamin":
    st.title("Yuk Kenali Macam-macam Vitamin!")
    st.subheader("Vitamin Itu Apa?")
    st.write("kita sudah tidak asing dengan vitamin, tetapi masih banyak orang yang jarang mengkonsumsi vitamin. Sebenarnya vitamin itu apa sih?")
    st.write("Vitamin adalah senyawa organik mikronutrien penting yang dibutuhkan tubuh dalam jumlah kecil untuk menjalankan berbagai fungsi biokimiawi. Vitamin tidak dapat disintesis oleh tubuh sendiri dan umumnya harus diperoleh dari makanan.") 

elif selection == "Manfaat Vitamin":
    st.write("Ini konten untuk Mengetahui Manfaat Vitamin.")
elif selection == "Fungsi Vitamin":
    st.write("Ini konten Mengetahui Fungsi Vitamin.")
elif selection == "Kekurangan":
    st.write("Ini konten untuk Mengetahui Kekurangan.")
elif selection == "Fakta Menarik":
    st.write("Ini konten untuk Mengetahui Fakta Menarik Vitamin.")

st.markdown(
    """
    <style>
    body, h1, h2, h3, h4, h5, h6, p, span, label, div, li, ul, ol, select, input, textarea, button {
        color: white !important;
    }

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
                    url(https://www.freepik.com/free-photo/vitamin-b-tablets-yellow-background_1168207.htm#fromView=search&page=2&position=44&uuid=2bc5d22f-28ba-4221-b9a1-36be2ef3daa1&query=vitamin);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
