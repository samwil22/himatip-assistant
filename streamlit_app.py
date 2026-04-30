import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="HIMATIP Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================
# DARK MODE
# =========================
dark_mode = st.toggle("🌙 / ☀️ Mode", value=False)

# =========================
# STYLE
# =========================
if dark_mode:
    st.markdown("""
    <style>
    .stApp {background: linear-gradient(135deg, #1B263B, #0D1B2A);}
    h1 {color: #E0E1DD; text-align:center;}
    p, label {color: #E0E1DD;}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp {background: linear-gradient(135deg, #E4EFE7, #FDFAF6);}
    h1 {color:#2F3E46; text-align:center;}
    p, label {color:#344E41;}
    </style>
    """, unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("🤖 HIMATIP Assistant")

# =========================
# FAQ DATA (AKADEMIS)
# =========================
faq_data = [

    {"kategori":"PKL","pertanyaan":"cara daftar pkl",
     "jawaban":
     "Pendaftaran PKL dilakukan melalui program studi dengan menyiapkan KHS dan transkrip.\n\n"
     "Pengajuan administrasi dilakukan melalui Biro Administrasi Akademik (BAA).\n\n"
     "Setelah disetujui, mahasiswa dapat mendaftar ke instansi tujuan."},

    {"kategori":"UJIAN","pertanyaan":"cara daftar ujian pkl",
     "jawaban":
     "Pendaftaran ujian dilakukan setelah laporan disetujui dosen pembimbing.\n\n"
     "Berkas diserahkan ke BAA untuk verifikasi dan penjadwalan."},

    {"kategori":"LAB","pertanyaan":"cara pinjam lab",
     "jawaban":
     "Peminjaman laboratorium dilakukan dengan mengajukan permohonan ke laboran.\n\n"
     "Mahasiswa mengisi formulir dan menunggu persetujuan penggunaan."},

    {"kategori":"PEMBAYARAN","pertanyaan":"cara bayar toefl",
     "jawaban":
     "Pembayaran dilakukan melalui Biro Administrasi Keuangan dan Umum (BAKU).\n\n"
     "Simpan bukti pembayaran untuk proses administrasi lanjutan."},

    {"kategori":"UJI_KOMPETENSI","pertanyaan":"cara daftar uji kompetensi",
     "jawaban":
     "Isi formulir pendaftaran dan lengkapi dokumen seperti KTP, transkrip, dan pas foto.\n\n"
     "Pembayaran dilakukan melalui BAKU.\n\n"
     "Jadwal ujian diinformasikan oleh panitia."},

    {"kategori":"KRS","pertanyaan":"cara heregistrasi",
     "jawaban":
     "Heregistrasi dilakukan dengan membayar UKT melalui BAKU.\n\n"
     "Setelah itu mahasiswa dapat mengakses sistem akademik."},

    {"kategori":"KRS","pertanyaan":"cara validasi krs",
     "jawaban":
     "Isi KRS pada sistem akademik.\n\n"
     "Lakukan konsultasi dengan dosen wali.\n\n"
     "KRS sah setelah mendapatkan ACC."}
]

# =========================
# CHATBOT (TANPA SKLEARN)
# =========================
def chatbot(user_input):
    user_input = user_input.lower()

    best_score = 0
    best_answer = None

    for f in faq_data:
        pertanyaan = f["pertanyaan"].lower()
        keywords = pertanyaan.replace("cara","").split()

        score = sum(1 for word in keywords if word in user_input)

        if score > best_score:
            best_score = score
            best_answer = f["jawaban"]

    if best_score == 0:
        return "Informasi belum ditemukan. Silakan hubungi admin HIMATIP atau bagian terkait seperti BAA, BAKU, atau laboratorium."

    return best_answer

# =========================
# DATA DOSEN (LENGKAP)
# =========================
dosen_data = [

    {"nama":"Dr. Lorine Tantalu, S.Pi., M.P., M.Sc",
     "bidang":"Lingkungan Agroindustri",
     "deskripsi":"Pengolahan limbah dan pengendalian pencemaran",
     "topik":["limbah cair","biochar","lingkungan"]},

    {"nama":"Prof. Dr. Ir. KGS. Ahmadi, M.P",
     "bidang":"Teknologi Industri Pertanian",
     "deskripsi":"Proses industri dan efisiensi produksi",
     "topik":["produksi","mesin","efisiensi"]},

    {"nama":"Razhika Faradilla, S.TP., M.P",
     "bidang":"Teknologi Industri Pertanian",
     "deskripsi":"Pengolahan hasil pertanian",
     "topik":["industri","produksi","pengolahan"]},

    {"nama":"Dr. Ir. Sri Handayani, M.P",
     "bidang":"Manajemen Agroindustri",
     "deskripsi":"Manajemen proses produksi",
     "topik":["efisiensi","manajemen","perencanaan"]},

    {"nama":"Ir. Endang Rusdiana, M.P",
     "bidang":"Manajemen Agroindustri",
     "deskripsi":"Optimasi sistem industri",
     "topik":["optimasi","sistem","manajemen"]},

    {"nama":"Dr. T. Wahyu Mushollaeni, S.Pi., M.P",
     "bidang":"Rekayasa Produk",
     "deskripsi":"Inovasi produk agroindustri",
     "topik":["produk","formulasi","inovasi"]},

    {"nama":"Dr. T. Budi Santosa, S.P., M.P",
     "bidang":"Rekayasa Produk",
     "deskripsi":"Kualitas dan mutu produk",
     "topik":["kualitas","mutu","pengujian"]},

    {"nama":"Dr. Atina Rahmawati, S.TP., M.P",
     "bidang":"Rekayasa Produk",
     "deskripsi":"Produk inovatif berbasis pangan",
     "topik":["pangan","inovasi","produk"]},

    {"nama":"Pramono Sasongko, S.TP., M.P., M.Sc",
     "bidang":"Multidisiplin",
     "deskripsi":"Pendekatan lintas bidang",
     "topik":["integrasi","multidisiplin"]},

    {"nama":"Dr. Wirawan, S.TP., MMA",
     "bidang":"Manajemen Agroindustri",
     "deskripsi":"Manajemen bisnis dan kelayakan usaha",
     "topik":["bisnis","kelayakan","manajemen"]},

    {"nama":"Editiya Hendrawarman, S.TP., M.P",
     "bidang":"Manajemen Agroindustri",
     "deskripsi":"Supply chain dan logistik",
     "topik":["supply chain","logistik","manajemen"]}
]

# =========================
# UI
# =========================
tab1, tab2, tab3 = st.tabs(["🤖 Assistant", "📚 FAQ", "🎓 Dosen & TA"])

# TAB 1
with tab1:
    user_input = st.text_input("💬 Tanyakan sesuatu...")
    if user_input:
        st.success(chatbot(user_input))

# TAB 2
with tab2:
    kategori = st.selectbox("📂 Kategori", ["Semua","PKL","UJIAN","LAB","PEMBAYARAN","UJI_KOMPETENSI","KRS"])
    for f in faq_data:
        if kategori == "Semua" or f["kategori"] == kategori:
            with st.expander(f["pertanyaan"]):
                st.write(f["jawaban"])

# TAB 3
with tab3:
    minat = st.selectbox("🎯 Pilih minat", ["Semua","Lingkungan","Produk","Manajemen","Teknik"])

    for d in dosen_data:
        cocok = (
            minat=="Semua" or
            (minat=="Lingkungan" and "Lingkungan" in d["bidang"]) or
            (minat=="Produk" and "Produk" in d["bidang"]) or
            (minat=="Manajemen" and "Manajemen" in d["bidang"]) or
            (minat=="Teknik" and "Teknologi" in d["bidang"])
        )

        if cocok:
            with st.expander(d["nama"]):
                st.write("**Bidang:**", d["bidang"])
                st.write("**Deskripsi:**", d["deskripsi"])
                st.write("**Topik TA:**")
                for t in d["topik"]:
                    st.write("-", t)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.write("📞 Admin HIMATIP")
