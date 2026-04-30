import streamlit as st
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import cosine_similarity

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="HIMATIP Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================
# DARK MODE TOGGLE
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
     "Pendaftaran Praktik Kerja Lapang (PKL) dilakukan melalui koordinasi dengan program studi.\n\n"
     "Mahasiswa perlu menyiapkan dokumen akademik seperti KHS dan transkrip nilai sebagai syarat administrasi.\n\n"
     "Selanjutnya, pengajuan surat pengantar dan validasi dilakukan melalui Biro Administrasi Akademik (BAA) atau Tata Usaha fakultas.\n\n"
     "Setelah disetujui, mahasiswa dapat mendaftarkan diri ke instansi tujuan PKL."},

    {"kategori":"UJIAN","pertanyaan":"cara daftar ujian pkl",
     "jawaban":
     "Pendaftaran ujian PKL dilakukan setelah laporan akhir disetujui oleh dosen pembimbing.\n\n"
     "Mahasiswa wajib melengkapi berkas seperti laporan, lembar pengesahan, dan bukti pembayaran.\n\n"
     "Seluruh berkas kemudian diserahkan ke Biro Administrasi Akademik (BAA) untuk proses verifikasi dan penjadwalan ujian."},

    {"kategori":"LAB","pertanyaan":"cara pinjam lab",
     "jawaban":
     "Peminjaman laboratorium dilakukan dengan mengajukan permohonan kepada pengelola laboratorium.\n\n"
     "Mahasiswa diwajibkan mengisi formulir peminjaman serta menjelaskan tujuan penggunaan.\n\n"
     "Proses persetujuan dan penjadwalan akan dikoordinasikan oleh laboran atau kepala laboratorium terkait."},

    {"kategori":"PEMBAYARAN","pertanyaan":"cara bayar toefl",
     "jawaban":
     "Pembayaran biaya TOEFL dan administrasi akademik lainnya dilakukan melalui Biro Administrasi Keuangan dan Umum (BAKU).\n\n"
     "Mahasiswa perlu melakukan pembayaran sesuai prosedur yang berlaku dan menyimpan bukti pembayaran.\n\n"
     "Bukti tersebut digunakan sebagai syarat untuk proses administrasi selanjutnya."},

    {"kategori":"UJI_KOMPETENSI","pertanyaan":"cara daftar uji kompetensi",
     "jawaban":
     "Pendaftaran uji kompetensi dilakukan dengan mengisi formulir yang telah disediakan oleh program studi.\n\n"
     "Mahasiswa wajib melengkapi dokumen seperti KTP, transkrip nilai, dan pas foto.\n\n"
     "Setelah pembayaran dilakukan melalui BAKU, bukti pembayaran diserahkan untuk proses verifikasi.\n\n"
     "Jadwal pelaksanaan akan diinformasikan oleh panitia penyelenggara."},

    {"kategori":"KRS","pertanyaan":"cara heregistrasi",
     "jawaban":
     "Heregistrasi merupakan proses wajib yang dilakukan setiap awal semester.\n\n"
     "Mahasiswa harus menyelesaikan pembayaran UKT melalui BAKU serta kewajiban lainnya seperti iuran himpunan.\n\n"
     "Setelah itu, mahasiswa dapat melakukan aktivasi pada sistem akademik."},

    {"kategori":"KRS","pertanyaan":"cara validasi krs",
     "jawaban":
     "Validasi KRS dilakukan setelah mahasiswa mengisi rencana studi pada sistem akademik.\n\n"
     "Mahasiswa perlu melakukan konsultasi dengan dosen wali untuk memastikan kesesuaian mata kuliah.\n\n"
     "KRS dinyatakan sah setelah mendapatkan persetujuan (ACC) dari dosen wali."}
]

questions = [f["pertanyaan"] for f in faq_data]
answers = [f["jawaban"] for f in faq_data]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(questions)

def chatbot(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, faq_vectors)
    idx = similarity.argmax()
    if similarity[0][idx] < 0.3:
        return "Informasi belum tersedia secara spesifik. Silakan menghubungi admin HIMATIP atau bagian terkait (BAA/BAKU/laboratorium) untuk bantuan lebih lanjut."
    return answers[idx]

# =========================
# DATA DOSEN (TETAP)
# =========================
dosen_data = [
    {"nama":"Dr. Lorine Tantalu, S.Pi., M.P., M.Sc","bidang":"Teknologi Lingkungan Agroindustri","deskripsi":"Pengolahan limbah & lingkungan","topik":["limbah","biochar","air limbah"]},
    {"nama":"Prof. Dr. Ir. KGS. Ahmadi, M.P","bidang":"Teknologi Industri Pertanian","deskripsi":"Proses & efisiensi industri","topik":["produksi","mesin","efisiensi"]},
    {"nama":"Razhika Faradilla, S.TP., M.P","bidang":"Teknologi Industri Pertanian","deskripsi":"Pengolahan hasil pertanian","topik":["produksi","industri"]},
    {"nama":"Dr. Ir. Sri Handayani, M.P","bidang":"Manajemen Proses Agroindustri","deskripsi":"Manajemen proses produksi","topik":["efisiensi","proses"]},
    {"nama":"Ir. Endang Rusdiana, M.P","bidang":"Manajemen Proses Agroindustri","deskripsi":"Optimasi sistem industri","topik":["optimasi","manajemen"]},
    {"nama":"Dr. T. Wahyu Mushollaeni, S.Pi., M.P","bidang":"Rekayasa Produk Agroindustri","deskripsi":"Inovasi produk","topik":["produk baru","formulasi"]},
    {"nama":"Dr. T. Budi Santosa, S.P., M.P","bidang":"Rekayasa Produk Agroindustri","deskripsi":"Kualitas & pengembangan produk","topik":["kualitas","produk"]},
    {"nama":"Dr. Atina Rahmawati, S.TP., M.P","bidang":"Rekayasa Produk Agroindustri","deskripsi":"Produk inovatif","topik":["inovasi","pangan"]},
    {"nama":"Pramono Sasongko, S.TP., M.P., M.Sc","bidang":"Multidisiplin","deskripsi":"Lintas bidang","topik":["kombinasi"]},
    {"nama":"Dr. Wirawan, S.TP., MMA","bidang":"Manajemen Agroindustri","deskripsi":"Bisnis & strategi","topik":["bisnis","kelayakan"]},
    {"nama":"Editiya Hendrawarman, S.TP., M.P","bidang":"Manajemen Agroindustri","deskripsi":"Supply chain","topik":["rantai pasok","manajemen"]}
]

# =========================
# UI
# =========================
tab1, tab2, tab3 = st.tabs(["🤖 Assistant", "📚 FAQ", "🎓 Dosen & TA"])

with tab1:
    user_input = st.text_input("💬 Silakan tanyakan informasi akademik...")
    if user_input:
        st.success(chatbot(user_input))

with tab2:
    kategori = st.selectbox("📂 Pilih kategori", ["Semua","PKL","UJIAN","LAB","PEMBAYARAN","UJI_KOMPETENSI","KRS"])
    for f in faq_data:
        if kategori == "Semua" or f["kategori"] == kategori:
            with st.expander(f["pertanyaan"]):
                st.write(f["jawaban"])

with tab3:
    minat = st.selectbox("🎯 Pilih minat", ["Semua","Lingkungan","Produk","Manajemen","Teknik"])
    for d in dosen_data:
        with st.expander(d["nama"]):
            st.write("**Bidang:**", d["bidang"])
            st.write("**Deskripsi:**", d["deskripsi"])
            st.write("**Topik TA:**")
            for t in d["topik"]:
                st.write("-", t)

st.markdown("---")
st.write("📞 Admin HIMATIP: 08xxxxxxxxxx")
