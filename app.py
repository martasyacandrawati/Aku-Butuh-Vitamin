import streamlit as st
import math

st.set_page_config(page_title="Buah dan Vitamin Didalam-nya", layout="centered")

# Sidebar for input
with st.sidebar:
    st.header("Menu")
    selection = st.radio("Ingin Tahu Tentang Apa?", ["Kenali Vitamin", "Fungsi dan Sumber Vitamin", "Kekurangan dan Kelebihan", "Fakta Menarik", "Quiz", "Tentang Aplikasi"])

# Konten berdasarkan pilihan
if selection == "Kenali Vitamin":
    st.title("Ayo Kita Kenali Vitamin!")
    st.markdown("---")
    st.subheader("Tapi sebelum itu, kalian tau ga sih siapa penemu vitamin?")
    st.image("https://i.pinimg.com/736x/74/0a/f4/740af4b86e32855fd4486de3315ade73.jpg")
    st.write("Penemu vitamin adalah Casimir Funk, seorang ahli biokimia 🧪👨🏼‍🔬yang menemukan dan memberikan nama vitamin pada zat-zat penting yang dibutuhkan tubuh untuk kesehatan. Ia juga dikenal sebagai Bapak Terapi Vitamin karena karyanya yang penting dalam memahami dan mengobati kekurangan vitamin. Funk mempopulerkan istilah ✨vitamin✨(Vital Amine) untuk menyebut zat-zat penting yang dibutuhkan tubuh, yang kemudian disingkat menjadi vitamin.")
    st.markdown("---")
    st.subheader("Vitamin Itu Apa?")
    st.write("kita sudah tidak asing dengan vitamin, tetapi masih banyak orang yang jarang mengkonsumsi vitamin. Sebenarnya vitamin itu apa sih?")
    st.write("Vitamin adalah senyawa organik mikronutrien penting yang dibutuhkan tubuh dalam jumlah kecil untuk menjalankan berbagai fungsi biokimiawi. Vitamin tidak dapat disintesis oleh tubuh sendiri dan umumnya harus diperoleh dari makanan.") 
    st.markdown("---")
    st.subheader("Apa Saja Macam Vitamin?")
    st.write("Vitamin dibagi menjadi dua kelompok utama yakni vitamin larut lemak (A, D, E, K) dan vitamin larut air (C dan B kompleks).")
elif selection == "Fungsi dan Sumber Vitamin":
    st.title("Sebenarnya, Apa Saja Fungsi dan Sumber Dari Vitamin?")
    st.markdown("---")
    st.write("Vitamin Memiliki Berbagai Fungsi Dari Berbagai Sumber loh! namun vitamin memiliki fungsi umum sebagai kofaktor dalam reaksi kimia yang dikatalisis oleh enzim, membantu tubuh dalam pertumbuhan, perkembangan, dan fungsi normal.")
    st.markdown("---")
    st.header("Vitamin A")
    st.image("https://i.pinimg.com/736x/60/60/ba/6060baba5fb1bc1fd43193d2852c51e2.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin A")
    st.write("- Menjaga kesehatan mata (penglihatan malam)")
    st.write("- Mendukung sistem imun")
    st.write("- Membantu pertumbuhan dan perkembangan sel")
    st.subheader("Contoh sehari-hari")
    st.write("Saat kamu belajar di malam hari atau sering menatap layar mata-mu bisa menjadi rabun, maka kamu butuh vitamin A untuk membantu menjaga penglihatan tetap tajam.")
    st.subheader("Sumber Vitamin A")
    st.write("Hati sapi & ayam♥, ikan salmon & ikan tenggiri🐟, ubi jalar🍠, paprika🫑, kacang panjang, labu🎃, jeruk🍊, telur 🥚, keju🧀, sereal🥣, brokoli🥦, paprika🫑, pepaya, jambu biji, dan susu🥛.")
    st.markdown("---")
    st.header("Vitamin B Kompleks")
    st.image("https://i.pinimg.com/736x/1e/8c/bf/1e8cbf9679b94b7d8ca7f20c55aa0e97.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin B1 (Thiamin)")
    st.write("- Mengubah karbohidrat menjadi energi")
    st.write("- Mendukung fungsi saraf dan otot")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu belajar atau kerja seharian, maka kamu butuh Vitamin B1 untuk bantu kamu tetap fokus dan bertenaga.")
    st.subheader("Sumber Alami Vitamin B1 (Thiamin)")
    st.write("Gandum🌾, beras merah🍚♦,daging babi🥓, daging sapi🥩, unggas🍗, ikan tuna🐟, salmon🍣, kacang kedelai, kacang merah🫘, nanas🍍, alpukat🥑, anggur🍇, semangka🍉, brokoli🥦, asparagus, kubis🥬, dan kentang🥔.")  
    st.subheader("Fungsi Vitamin B2 (Riboflavin)")
    st.write("- Membantu produksi energi")
    st.write("- Menjaga kesehatan kulit dan mata")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kalau kamu sering pakai gadget, maka kamu butuh Vitamin B2 untuk bantu kamu menjaga mata tetap sehat.")
    st.subheader("Sumber Alami Vitamin B2 (Riboflavin)")
    st.write("Hati sapi♥, susu🥛, keju🧀, yogurt 🧃,kuning telur🥚, daging ayam🐓, daging kalkun🦃, ikan salmon🍣, dan jamur 🍄.")
    st.subheader("Fungsi Vitamin B3 (Niasin)")
    st.write("- Metabolisme energi")
    st.write("- Menjaga kulit dan pencernaan")
    st.write("- Membantu menurunkan kolesterol")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Setelah kamu makan, Vitamin B3 dapat membantu proses pencernaan-mu bekerja dengan baik.")
    st.subheader("Sumber Alami Vitamin B3 (Niasin)")
    st.write("Daging merah🥩, unggas🐓, ikan🐟, kacang-kacangan🥜, biji-bijian🫘, sereal utuh🫘, mangga 🥭dan melon🍈.")
    st.subheader("Fungsi Vitamin B5 (Pantotenat)")
    st.write("- Sintesis hormon dan metabolisme lemak")
    st.write("- Pembentukan sel darah merah")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu stres atau kurang tidur, maka kamu butuh Vitamin B5 untuk membantu tubuh mengatur hormon stres seperti kortisol.")
    st.subheader("Sumber Alami Vitamin B5 (Pantotenat)")
    st.write("Hati sapi♥, kuning telur🍳, kerang🐚, salmon🍣, daging ayam🐓, alpukat🥑, brokoli🥦, jamur enoki & shitake🍄, ubi jalar🍠, susu🥛, keju🧀, gandum 🌾, dan kacang polong 🫛.")
    st.subheader("Fungsi Vitamin B6 (Piridoksin)")
    st.write("- Metabolisme protein dan memproduksi neurotransmiter")
    st.write("- Mendukung fungsi otak dan suasana hati")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Ketika kamu sedang stres atau cemas, maka Vtamin B6 akan membantu kamu untuk menstabilkan mood.")
    st.subheader("Sumber Alami Vitamin B6 (Piridoksin)")
    st.write("Daging sapi 🐄, daging ayam 🐓, telur 🥚, kentang 🥔, pisang 🍌, alpukat 🥑, bayam 🥬, wortel🥕, salmon🍣, tuna🐟, kacang arab/chickpea🥜, mangga🥭, nanas🍍, dan semangka🍉.")
    st.subheader("Fungsi Vitamin B7 (Biotin)")
    st.write("- Mendukung kesehatan rambut, kulit, dan kuku")
    st.write("- Membantu metabolisme lemak dan protein")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Jika kamu sering styling rambut atau mengalami rambut rontok, maka kamu butuh banget Vitamin B7 yang akan membantu memperkuat rambut dari dalam.")
    st.subheader("Sumber Alami Vitamin B7 (Biotin)")
    st.write("Hati ayam🐓, hati sapi🐄, kuning telur🍳, almond🥜, kedelai🥜, polong🫛, buncis🫘, kembang kol🥬, bayam🥬, serta buah-buahan seperti pisang🍌, rasberi🫐 dan alpukat🥑.")
    st.subheader("Fungsi Vitamin B9 (Asam Folat)")
    st.write("- Membantu pembentukan sel darah merah")
    st.write("- Mencegah cacat lahir pada janin")
    st.write("- Sintesis DNA dan RNA")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kegunaan Vitamin B9 sangat banyak loh! seperti pada ibu hamil asam folat akan membantu mencegah cacat tabung saraf (seperti spina bifida) pada janin. Lalu pada anak-anak atau remaja yang sedang tumbuh, asam folat akan membantu pembelahan dan perkembangan sel tubuh. Serta untuk pelajar seperti kita, Vitamin B9 membantu pembentukan sel-sel otak baru yang penting untuk daya pikir dan konsentrasi.")
    st.subheader("Sumber Alami Vitamin B9 (Asam Folat)")
    st.write("Bayam🥬, brokoli🥦, lobak hijau🫜, selada🥬, buah bit🍑, pisang 🍌, alpukat 🥑, kacang merah🫘, kacang polong🫛,  biji bunga matahari🌻, gandum🌾, hati sapi🐄, telur🥚.")
    st.subheader("Fungsi Vitamin B12 (Kobalamin)")
    st.write("- Membantu pembentukan sel darah merah")
    st.write("- Menjaga fungsi sistem saraf")
    st.write("- Mendukung metabolisme energi")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Kamu sering lemas atau pusing? bisa jadi itu karena tubuh-mu kekurangan Vitamin B12 loh!")
    st.subheader("Sumber Alami Vitamin B12 (Kobalamin)")
    st.write("Hati sapi♥, kerang🐚, ikan salmon🍣, tuna & sarden🐟, daging ayam🐓, telur🥚, susu🥛, yogurt, keju🧀, Nori atau rumput laut kering🍀, bayam🥬, dan spirulina💊.")
    st.markdown("---")
    st.header("Vitamin C")
    st.image("https://i.pinimg.com/736x/9f/a4/f0/9fa4f04e044bdb25ca12602d0d89be87.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin C")
    st.write("- Meningkatkan daya tahan tubuh")
    st.write("- Membantu penyembuhan luka, antioksidan")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu mulai flu atau sariawan, maka vitamin C akan membantu mempercepat pemulihan tubuh.")
    st.subheader("Sumber Alami Vitamin C")
    st.write("Jeruk🍊, lemon🍋, kiwi🥝, strawberry🍓, nanas🍍, tomat🍅, brokoli 🥦, paprika🫑, kentang🥔, kangkung🌿, kembang kol🥬.")  
    st.markdown("---")
    st.header("Vitamin D")
    st.image("https://i.pinimg.com/736x/1d/4c/d7/1d4cd7731cf769d81733b3ae09febb1b.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin D")
    st.write("- Membantu penyerapan kalsium untuk tulang dan gigi yang kuat")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Saat kamu jarang kena sinar matahari karena sering di dalam ruangan, kamu berisiko kekurangan vitamin D, yang bisa membuat tulang rapuh. Jadi kamu perlu Vitamin D untuk mengatasi risiko tulang rapuh")
    st.subheader("Sumber Alami Vitamin D")
    st.write("Salmon🍣, tuna, sarden, makarel, hati sapi♥, kuning telur🍳, daging sapi🥩, jamur maitake🍄‍🟫, keju🧀, susu kedelai🥛🫛, bayam, brokoli🥦, buncis, alpukat🥑, kiwi🥝, dan apel🍎.")
    st.markdown("---")
    st.header("Vitamin E")
    st.image("https://i.pinimg.com/736x/21/94/db/2194dbd80b019204abb24e093ba8d401.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin E")
    st.write("- Antioksidan")
    st.write("- Melindungi sel dari kerusakan")
    st.write("- Menjaga kesehatan kulit.")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Setelah seharian terpapar polusi atau sinar matahari kulit-mu bisa rusak dan mengalami penuaan dini, maka dari itu kamu butuh vitamin E untuk membantu-mu melindungi kulit dari kerusakan dan penuaan dini.")
    st.subheader("Sumber Alami Vitamin E")
    st.write("Telur ayam🥚, kacang tanah🥜, alpukat🥑, biji bunga matahari🌻, brokoli🥦, telur ikan🐟, hazelnut 🌰, dan labu🎃.")
    st.markdown("---")
    st.header("Vitamin K")
    st.image("https://i.pinimg.com/736x/d9/d0/f2/d9d0f2c7e8cdba86ef5aeb9c686347c2.jpg")
    st.markdown("---")
    st.subheader("Fungsi Vitamin K")
    st.write("- Membantu pembekuan darah")
    st.write("- Menjaga kesehatan tulang")
    st.subheader("Contoh Kegunaan Dalam Kehidupan Sehari-hari")
    st.write("Jika kamu terluka, dan luka-mu tak kunjung kering atau membeku, maka kamu butuh vitamin K untuk membantu proses pembekuan darah.")
    st.subheader("Sumber Alami Vitamin K")
    st.write("Bayam, brokoli🥦, sawi🥬, kubis, daun bawang kiwi🥝, alpukat🥑, tomat🍅, buah delima, keju🧀, hati sapi & ayam♥, minyak zaitun🫒, susu sapi🥛dan kuning telur🍳.")
    st.markdown("---")
    st.subheader("Jadi, apakah kamu sudah tau vitamin apa yang kamu butuhkan?")
elif selection == "Kekurangan dan Kelebihan":
    st.title("Kalian Tau Ga Sih?")
    st.subheader("Jika kita kekurangan vitamin atau kelebihan vitamin dalam tubuh bisa berdampak buruk.")
    st.write("Yuk kita lihat apa saja yang kita alami jika kekurangan vitamin.")
    st.markdown("---")
    st.write("Yuk kita lihat apa saja yang kita alami jika kelebihan vitamin.")
    st.write("Kalian tau ga sih? Mengonsumsi terlalu banyak vitamin, terutama yang larut dalam lemak, dapat menyebabkan keracunan dan masalah kesehatan lainnya pada dirimu loh!")
elif selection == "Fakta Menarik":
    st.header("Kalian tau ga sih? Vitamin juga punya fakta menarik loh! yuk, kita cari tau bersama!")
    st.markdown("---")
    st.write("Vitamin tidak dapat dihasilkan oleh tubuh karena mereka adalah senyawa organik esensial yang dibutuhkan untuk berbagai fungsi tubuh, namun tubuh tidak memiliki kemampuan untuk memproduksinya secara alami.")
    st.write("Vitamin yang dapat diproduksi oleh tubuh antara lain adalah vitamin D dan vitamin K. Tubuh dapat memproduksi vitamin D ketika kulit terpapar sinar matahari☀, dan vitamin K diproduksi oleh bakteri di usus besar🦠. Vitamin D berperan penting dalam kesehatan tulang dan sistem kekebalan tubuh🩻, sedangkan vitamin K berperan dalam pembekuan darah🧛🏻‍♀🩸.")
    st.write("Jadi kesimpulannya tidak semua jenis vitamin dapat diproduksi secara alami oleh tubuh, sehingga penting bagi setiap individu untuk memenuhi asupan vitamin tubuh dengan mengonsumsi makanan sehat dan bergizi seimbang🥗🍉🥛")
elif selection == "Quiz":
    st.title("Yuk, kita lihat apakah kamu sudah benar-benar mengetahui tentang vitamin🫵😏")
    st.markdown("---")

    questions = [
        {
            "question": "Saat kamu belajar di malam hari atau sering menatap layar mata-mu bisa menjadi rabun, maka vitamin apa yang kamu butuhkan?",
            "options": ["A. Vitamin B1","B. Vitamin B2","C. Vitamin A","D.Vitamin K"],
            "answer": "C"
        },
        {
            "question": "Saat kamu belajar atau kerja seharian, maka kamu butuh Vitamin?",
            "options": ["A. Vitamin B1", "B. Vitamin B2", "C. Vitamin B6", "D. Vitamin B7"],
            "answer": "A"
        },
        {
            "question": "Bahan pangan apa yang mengandung vitamin C, A, K dan folat?",
            "options": ["A. Jeruk & Apel", "B. Ayam & Ikan", "C. Bayam & Brokoli", "D. Udang Keju & Mie gacoan"],
            "answer": "C"
        },
        {
            "question": "Vitamin berikut yang berperan sebagai antioksidan utama dalam tubuh adalah...",
            "options": ["A. Vitamin B12", "B. Vitamin K", "C. Vitamin E", "D. Vitamin B6"],
            "answer": "C"
        },
        {
            "question": "Untuk mendukung pertumbuhan janin secara optimal, vitamin apakah yang diperlukan?",
            "image": "https://i.pinimg.com/736x/d5/fc/52/d5fc5250f5dea26d4c679fdbd0dcc4d1.jpg",
            "options": ["A. Vitamin B9", "B. Vitamin B6", "C. Vitamin B5", "D. Vitamin B2"],
            "answer": "A"
        }
    ]
    score = 0
    user_answers = {}

    for idx, q in enumerate(questions):
        st.subheader(f"Pertanyaan {idx+1}: {q['question']}")
        if "image" in q:
            st.image(q["image"], width=300)
        user_choice = st.radio("Pilih jawaban:", q["options"], key=f"q{idx}")
        user_answers[f"q{idx}"] = user_choice[0]
        st.markdown("---")

    if st.button("Lihat Skor"):
        for idx, q in enumerate(questions):
            if user_answers[f"q{idx}"] == q["answer"]:
                score += 1
        st.success(f"Skor akhir Anda: {score}/{len(questions)}")

        if score == 0:
            st.write("☠ Wah, kamu ngisi kuisnya sambil merem ya? ☠")
        elif score == 1:
            st.write("🤡 Hmm... minimal kamu tau satu hal, itu pun mungkin kebetulan... 🤡")
        elif score == 2:
            st.write("🤯 Lumayan, udah mulai keliatan bibit-bibit paham vitamin. 🤯")
        elif score == 3:
            st.write("👏🏻 Bagus! Setengah jalan menuju jadi master vitamin! 👏🏻")
        elif score == 4:
            st.write("😻 Wow! Dikit lagi jadi ahli gizi nih! 😻")
        elif score == 5:
            st.write("🏆 PERFECT! Kamu emang panutan hidup sehat! 🏆")
            st.balloons()

   
elif selection == "Tentang Aplikasi":
    st.title("Aplikasi Ini Dibuat Dengan Tujuan :")
    st.markdown("---")
    st.write("💊 Membantu user untuk mengenali vitamin.")
    st.write("🥗 Membantu User untuk mengetahui tentang berbagai macam jenis vitamin.")
    st.write("🥩 Membantu user untuk mengetahui kekurangan dan kelebihan vitamin.")
    st.write("🍌 Membantu user untuk mengetahui bahan pangan apa saja yang mengandung vitamin yang dibutuhkan.")
    st.write("🍎 Memberikan penjelasan kepada user agar user mengetahui pentingnya mengkonsumsi vitamin.")
    st.write("🫛 Memberikan pengetahuan tentang fakta unik dari vitamin.")
    st.write("🍇 Memberikan quiz kepada user untuk mengetahui pemahaman user mengenai Vitamin.")
    st.write("🥜 Aplikasi ini dibuat sebagai tugas akhir mata kuliah Logika Dan Pemograman Komputer.")

page_bg_style = """
<style>
/* Background Utama */
.stApp {
    background-image: url("https://i.pinimg.com/736x/b7/99/a1/b799a14446a6511b50f934abcb0eaf1c.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-color: rgba(255, 255, 255, 0.3); /* warna putih semi-transparan */
    background-blend-mode: overlay; /* blend warna + gambar */
}

/* Warna Teks */
html, body, [class^="st-"], [class*=" st-"] {
    color: #5C2E1F !important;
}

/* Sidebar */
[data-testid="stSidebarContent"] {
    background-color: #D291BC !important;
    color: #5C2E1F !important;
}
/* Judul */
h1, h2, h3 {
    color: #5C2E1F !important;
}

/* Tombol */
button, .stButton button, .stDownloadButton button {
    background-color: #E6B8A2 !important;  /* pastel coklat */
    color: #5C2E1F !important;
    border-radius: 6px;
}
button:hover {
    background-color: #D39E88 !important;
}

/* Garis pemisah (---) */
hr {
    border: none !important;
    border-top: 3px solid #5C2E1F !important;
    margin: 1rem 0 !important;
    opacity: 1 !important;
}
</style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
