import streamlit as st
import math

st.set_page_config(page_title="Buah dan Vitamin Didalam-nya", layout="centered")

# Sidebar for input
with st.sidebar:
    st.header("Menu")
    selection = st.radio("Ingin Tahu Tentang Apa?", ["Kenali Vitamin", "Fungsi dan Sumber Vitamin", "Kekurangan dan Kelebihan", "Fakta Menarik", "Tentang Kami"])

# Konten berdasarkan pilihan
if selection == "Kenali Vitamin":
    st.title("Yuk Kenali Macam-macam Vitamin!")
    st.markdown("---")
    st.subheader("Vitamin Itu Apa?")
    st.markdown("---")
    st.write("kita sudah tidak asing dengan vitamin, tetapi masih banyak orang yang jarang mengkonsumsi vitamin. Sebenarnya vitamin itu apa sih?")
    st.write("Vitamin adalah senyawa organik mikronutrien penting yang dibutuhkan tubuh dalam jumlah kecil untuk menjalankan berbagai fungsi biokimiawi. Vitamin tidak dapat disintesis oleh tubuh sendiri dan umumnya harus diperoleh dari makanan.") 
    st.subheader("Apa Saja Macam Vitamin?")
    st.markdown("---")
    st.write("Vitamin dibagi menjadi dua kelompok utama yakni vitamin larut lemak (A, D, E, K) dan vitamin larut air (C dan B kompleks).")
elif selection == "Fungsi dan Sumber Vitamin":
    st.title("Sebenarnya, Apa Saja Fungsi dan Sumber Dari Vitamin?")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh! namun vitamin memiliki fungsi umum sebagai kofaktor dalam reaksi kimia yang dikatalisis oleh enzim, membantu tubuh dalam pertumbuhan, perkembangan, dan fungsi normal.")
    st.subheader("Vitamin A")
    st.markdown("---")
    st.write("- Menjaga kesehatan mata (penglihatan malam)",
             "-Mendukung sistem imun",
             "-Membantu pertumbuhan dan perkembangan sel")
    st.subheader("Vitamin B")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh!")
    st.subheader("Vitamin C")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh!")
    st.subheader("Vitamin D")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh!")
    st.subheader("Vitamin E")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh!")
    st.subheader("Vitamin K")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh!")
elif selection == "Kekurangan dan Kelebihan":
    st.write("Ini konten untuk Mengetahui Kekurangan.")
elif selection == "Fakta Menarik":
    st.write("Ini konten untuk Mengetahui Fakta Menarik Vitamin.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
