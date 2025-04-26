import streamlit as st
import math

st.set_page_config(page_title="Kalkulator pH & pOH", layout="centered")

# Title
st.title("🧪 Kalkulator pH & pOH Larutan")

# Description
st.write("""
Aplikasi ini membantu menghitung nilai pH dan pOH larutan berdasarkan input konsentrasi ion [H⁺] atau [OH⁻].
""")

# Sidebar for input
with st.sidebar:
    st.header("Input Parameter")
    ion_type = st.radio("Pilih jenis ion yang diketahui:", ("[H⁺]", "[OH⁻]"))
    concentration = st.number_input(f"Masukkan konsentrasi {ion_type} (mol/L):", min_value=1e-14, max_value=1.0, format="%.2e")
    show_dark_mode = st.checkbox("Aktifkan Mode Gelap")

# Apply dark mode
if show_dark_mode:
    st.markdown(
        """
        <style>
            body { background-color: #1e1e1e; color: white; }
            .stApp { background-color: #1e1e1e; }
        </style>
        """, unsafe_allow_html=True
    )

# Divider
st.markdown("---")

if st.button("Hitung pH dan pOH"):
    if ion_type == "[H⁺]":
        pH = -math.log10(concentration)
        pOH = 14 - pH
    else:
        pOH = -math.log10(concentration)
        pH = 14 - pOH

    if pH < 7:
        sifat = "Asam"
        sifat_desc = "Asam berarti larutan memiliki ion H⁺ yang lebih banyak daripada OH⁻."
    elif pH == 7:
        sifat = "Netral"
        sifat_desc = "Larutan netral memiliki konsentrasi ion H⁺ dan OH⁻ yang seimbang."
    else:
        sifat = "Basa"
        sifat_desc = "Basa berarti larutan memiliki ion OH⁻ yang lebih banyak daripada H⁺."

    if pH < 4:
        indikator = "Metil Merah"
    elif 4 <= pH < 7:
        indikator = "Bromtimol Biru"
    elif 7 <= pH < 10:
        indikator = "Fenolftalein"
    else:
        indikator = "Lakmus Biru"

    st.success(f"pH: {pH:.2f}")
    st.info(f"pOH: {pOH:.2f}")
    st.warning(f"Sifat larutan: {sifat}")
    st.caption(sifat_desc)
    st.markdown(f"**🔬 Rekomendasi indikator pH:** {indikator}")

    # Visualisasi
    st.subheader("🌈 Visualisasi Skala pH")
    colors = ["#ff0000", "#ff4500", "#ffa500", "#ffff00", "#adff2f", "#00ff00",
              "#00fa9a", "#00ced1", "#1e90ff", "#4169e1", "#0000cd", "#00008b", "#191970", "#4b0082", "#8a2be2"]

    st.markdown("<div style='display: flex; flex-direction: row;'>", unsafe_allow_html=True)
    for i in range(15):
        highlight = "border: 3px solid black;" if int(round(pH)) == i else ""
        st.markdown(
            f"<div style='background-color: {colors[i]}; width: 30px; height: 40px; margin-right: 2px; {highlight}' title='pH {i}'></div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
    st.caption(f"pH kamu di sekitar angka {round(pH)} pada skala warna di atas.")

st.markdown("---")
st.caption("📘 Made with Streamlit for educational purposes.")
