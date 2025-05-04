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
    st.header("Vitamin A")
    st.markdown("---")
    st.subheader("Fungsi Vitamin A")
    st.write("- Menjaga kesehatan mata (penglihatan malam)")
    st.write("- Mendukung sistem imun")
    st.write("- Membantu pertumbuhan dan perkembangan sel")
    st.subheader("Sumber Vitamin A")
    st.write("Hati💖, telur🥚, susu🍼, wortel🥕, ubi🍠, bayam🥬, mangga🥭")
    st.header("Vitamin B")
    st.markdown("---")
    st.subheader("Fungsi Vitamin B1 (Thiamin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B1 (Thiamin)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")
    
    st.subheader("Fungsi Vitamin B2 (Riboflavin)")
    st.write("- Membantu produksi energi")
    st.write("- Menjaga kesehatan kulit dan mata")
    st.subheader("Sumber Alami Vitamin B2 (Riboflavin)")
    st.write("Susu 🥛, telur 🥚, hati 🐄, sayur hijau 🥬")
    
    st.subheader("Fungsi Vitamin B3 (Niasin)")
    st.write("- Metabolisme energi")
    st.write("- Menjaga kulit dan pencernaan")
    st.write("- Membantu menurunkan kolesterol")
    st.subheader("Sumber Alami Vitamin B3 (Niasin)")
    st.write("Daging ayam 🍗, ikan tuna 🐟, gandum utuh 🌾")

    st.subheader("Fungsi Vitamin B5 (Pantotenat)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B5 (Pantotenat)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")

    st.subheader("Fungsi Vitamin B6 (Piridoksin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B6 (Piridoksin)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")

    st.subheader("Fungsi Vitamin B7 (Biotin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B7 (Biotin)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")

    st.subheader("Fungsi Vitamin B9 (Asam Folat)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B9 (Asam Folat)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")

    st.subheader("Fungsi Vitamin B12 (Kobalamin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Sumber Alami Vitamin B12 (Kobalamin)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")
elif selection == "Kekurangan dan Kelebihan":
    st.write("Ini konten untuk Mengetahui Kekurangan.")
elif selection == "Fakta Menarik":
    st.write("Ini konten untuk Mengetahui Fakta Menarik Vitamin.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
