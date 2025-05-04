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
    st.markdown("---")
    st.header("Vitamin A")
    st.markdown("---")
    st.subheader("Fungsi Vitamin A")
    st.write("- Menjaga kesehatan mata (penglihatan malam)")
    st.write("- Mendukung sistem imun")
    st.write("- Membantu pertumbuhan dan perkembangan sel")
    st.subheader("Contoh sehari-hari")
    st.write("Saat kamu belajar di malam hari atau sering menatap layar mata-mu bisa menjadi rabun, maka kamu butuh vitamin A untuk membantu menjaga penglihatan tetap tajam.")
    st.subheader("Sumber Vitamin A")
    st.write("Hati💖, telur🥚, susu🍼, wortel🥕, ubi🍠, bayam🥬, mangga🥭")
    st.markdown("---")
    st.header("Vitamin B Kompleks")
    st.markdown("---")
    st.subheader("Fungsi Vitamin B1 (Thiamin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu belajar atau kerja seharian, maka kamu butuh Vitamin B1 untuk bantu kamu tetap fokus dan bertenaga.")
    st.subheader("Sumber Alami Vitamin B1 (Thiamin)")
    st.write("Beras merah 🍚, daging babi 🍖, biji bunga matahari 🌻")  
    st.subheader("Fungsi Vitamin B2 (Riboflavin)")
    st.write("- Membantu produksi energi")
    st.write("- Menjaga kesehatan kulit dan mata")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kalau kamu sering pakai gadget, maka kamu butuh Vitamin B2 untuk bantu kamu menjaga mata tetap sehat.")
    st.subheader("Sumber Alami Vitamin B2 (Riboflavin)")
    st.write("Susu 🥛, telur 🥚, hati 🐄, sayur hijau 🥬")
    st.subheader("Fungsi Vitamin B3 (Niasin)")
    st.write("- Metabolisme energi")
    st.write("- Menjaga kulit dan pencernaan")
    st.write("- Membantu menurunkan kolesterol")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Setelah kamu makan, Vitamin B3 dapat membantu proses pencernaan-mu bekerja dengan baik.")
    st.subheader("Sumber Alami Vitamin B3 (Niasin)")
    st.write("Daging ayam 🍗, ikan tuna 🐟, gandum utuh 🌾")
    st.subheader("Fungsi Vitamin B5 (Pantotenat)")
    st.write("- Sintesis hormon dan metabolisme lemak")
    st.write("- Pembentukan sel darah merah")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu stres atau kurang tidur, maka kamu butuh Vitamin B5 untuk membantu tubuh mengatur hormon stres seperti kortisol.")
    st.subheader("Sumber Alami Vitamin B5 (Pantotenat)")
    st.write("Alpukat 🥑, jamur 🍄, ayam 🍗, biji-bijian 🌰")
    st.subheader("Fungsi Vitamin B6 (Piridoksin)")
    st.write("- Metabolisme protein dan memproduksi neurotransmiter")
    st.write("- Mendukung fungsi otak dan suasana hati")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Ketika kamu sedang stres atau cemas, maka Vtamin B6 akan membantu kamu untuk menstabilkan mood.")
    st.subheader("Sumber Alami Vitamin B6 (Piridoksin)")
    st.write("Pisang 🍌, kentang 🥔, ayam 🍗, ikan 🐟")
    st.subheader("Fungsi Vitamin B7 (Biotin)")
    st.write("- Mendukung kesehatan rambut, kulit, dan kuku")
    st.write("- Membantu metabolisme lemak dan protein")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Jika kamu sering styling rambut atau mengalami rambut rontok, maka kamu butuh banget Vitamin B7 yang akan membantu memperkuat rambut dari dalam.")
    st.subheader("Sumber Alami Vitamin B7 (Biotin)")
    st.write("Telur 🥚, kacang-kacangan 🥜, hati 🐄, kembang kol 🥦")
    st.subheader("Fungsi Vitamin B9 (Asam Folat)")
    st.write("- Membantu pembentukan sel darah merah")
    st.write("- Mencegah cacat lahir pada janin")
    st.write("- Sintesis DNA dan RNA")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kegunaan Vitamin B9 sangat banyak loh! seperti pada ibu hamil asam folat akan membantu mencegah cacat tabung saraf (seperti spina bifida) pada janin. Lalu pada anak-anak atau remaja yang sedang tumbuh, asam folat akan membantu pembelahan dan perkembangan sel tubuh. Serta untuk pelajar seperti kita, Vitamin B9 membantu pembentukan sel-sel otak baru yang penting untuk daya pikir dan konsentrasi.")
    st.subheader("Sumber Alami Vitamin B9 (Asam Folat)")
    st.write("Sayur hijau 🥬, jeruk 🍊, kacang 🫘, roti fortifikasi 🍞")
    st.subheader("Fungsi Vitamin B12 (Kobalamin)")
    st.write("- Membantu pembentukan sel darah merah")
    st.write("- Menjaga fungsi sistem saraf")
    st.write("- Mendukung metabolisme energi")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kamu sering lemas atau pusing? bisa jadi itu karena tubuh-mu kekurangan Vitamin B12 loh!")
    st.subheader("Sumber Alami Vitamin B12 (Kobalamin)")
    st.write("Daging 🥩, ikan 🐟, telur 🥚, susu 🥛")
    st.markdown("---")
    st.header("Vitamin C")
    st.markdown("---")
    st.subheader("Fungsi Vitamin C")
    st.write("- Meningkatkan daya tahan tubuh")
    st.write("- Membantu penyembuhan luka, antioksidan")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu mulai flu atau sariawan, maka vitamin C akan membantu mempercepat pemulihan tubuh.")
    st.subheader("Sumber Alami Vitamin C")
    st.write("Jeruk 🍊, Stroberi 🍓, Tomat 🍅, Paprika 🫑")  
    st.markdown("---")
    st.header("Vitamin D")
    st.markdown("---")
    st.subheader("Fungsi Vitamin D")
    st.write("- Membantu penyerapan kalsium untuk tulang dan gigi yang kuat")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu jarang kena sinar matahari karena sering di dalam ruangan, kamu berisiko kekurangan vitamin D, yang bisa membuat tulang rapuh. Jadi kamu perlu Vitamin D untuk mengatasi risiko tulang rapuh")
    st.subheader("Sumber Alami Vitamin D")
    st.write("Sinar matahari ☀, Ikan berlemak 🐟, Telur 🥚")
    st.markdown("---")
    st.header("Vitamin E")
    st.markdown("---")
    st.subheader("Fungsi Vitamin E")
    st.write("- Antioksidan")
    st.write("- Melindungi sel dari kerusakan")
    st.write("- Menjaga kesehatan kulit.")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Setelah seharian terpapar polusi atau sinar matahari kulit-mu bisa rusak dan mengalami penuaan dini, maka dari itu kamu butuh vitamin E untuk membantu-mu melindungi kulit dari kerusakan dan penuaan dini.")
    st.subheader("Sumber Alami Vitamin E")
    st.write("Kacang-kacangan 🥜, Biji-bijian 🌻, Minyak nabati 🧴")
    st.markdown("---")
    st.header("Vitamin K")
    st.markdown("---")
    st.subheader("Fungsi Vitamin K")
    st.write("- Membantu pembekuan darah")
    st.write("- Menjaga kesehatan tulang")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Jika Saat kamu terluka, dan luka-mu tak kunjung kering atau membeku, maka kamu butuh vitamin K untuk membantu proses pembekuan darah.")
    st.subheader("Sumber Alami Vitamin K")
    st.write("Brokoli 🥦, Sayuran hijau 🥬, Hati 💖")
elif selection == "Kekurangan dan Kelebihan":
    st.title("Kalian Tau Ga Sih?")
    st.subheader("Jika kita kekurangan vitamin atau kelebihan vitamin dalam tubuh bisa berdampak buruk?")
    st.markdown("---")
    st.subheader("Yuk kita lihat apa saja yang kita alami jika kekurangan vitamin.")
elif selection == "Fakta Menarik":
    st.write("Ini konten untuk Mengetahui Fakta Menarik Vitamin.")

page_bg_style = """
<style>
/* Background utama */
[data-testid="stAppViewContainer"] > div:first-child {
    background-image: url("https://i.pinimg.com/736x/b7/99/a1/b799a14446a6511b50f934abcb0eaf1c.jpg") !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}

/* Warna teks mahogany */
html, body, [class*="st-"] {
    color: #5C2E1F !important;
    font-family: "Arial", sans-serif;
}
/* Judul */
h1, h2, h3 {
    color: #5C2E1F !important;
}

/* Sidebar dengan warna pink keunguan */
[data-testid="stSidebar"] {
    background-color: #D291BC !important;
    color: #5C2E1F !important;
}

/* Header transparan */
[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0.0) !important;
}

/* Button */
button, .stButton button, .stDownloadButton button {
    background-color: #5C2E1F !important;
    color: white !important;
    border: none;
    border-radius: 6px;
}

button:hover {
    background-color: #3E1B16 !important;
}

/* Link dan teks interaktif */
a, .stMarkdown a {
    color: #5C2E1F !important;
    text-decoration: underline;
}
</style>
"""

import streamlit as st
st.markdown(page_bg_style, unsafe_allow_html=True)


st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
