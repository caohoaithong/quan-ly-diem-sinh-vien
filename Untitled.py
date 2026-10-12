
# =====================================================
# 1. IMPORT THU VIEN
# =====================================================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# 2. CAU HINH GIAO DIEN
# =====================================================
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# 3. CSS: BACKGROUND, CHU, THE NOI 3D
# =====================================================
st.markdown("""
<style>

/* Nen trang */
.stApp {
    background: linear-gradient(
        135deg,
        #dbeafe 0%,
        #f5f3ff 50%,
        #ffffff 100%
    );
}

/* Gioi han chieu rong noi dung */
.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Kich thuoc chu */
.stApp {
    font-size: 18px;
}

h1 {
    font-size: 40px !important;
}

h2 {
    font-size: 30px !important;
    color: #174a8b !important;
}

h3 {
    font-size: 24px !important;
}

/* Tieu de dau trang */
.hero {
    background: linear-gradient(
        120deg,
        #123b70,
        #2563eb,
        #7c3aed
    );
    padding: 32px;
    border-radius: 22px;
    margin-bottom: 28px;
    box-shadow:
        0 8px 0 #94a3b8,
        0 16px 28px rgba(30, 64, 175, 0.28);
    transition: 0.25s ease;
}

.hero:hover {
    transform: translateY(-3px);
    box-shadow:
        0 11px 0 #94a3b8,
        0 22px 35px rgba(30, 64, 175, 0.30);
}

.hero-title {
    color: white;
    font-size: 38px;
    font-weight: 850;
    line-height: 1.4;
}

.hero-subtitle {
    color: #dbeafe;
    font-size: 19px;
    margin-top: 10px;
}

/* Tieu de cac khu vuc */
.section-title {
    color: #123b70;
    font-size: 27px;
    font-weight: 800;
    padding: 15px 20px;
    margin: 20px 0;
    background: linear-gradient(120deg, #ffffff, #dbeafe);
    border-left: 7px solid #2563eb;
    border-radius: 14px;
    box-shadow:
        0 5px 0 #bfdbfe,
        0 10px 18px rgba(30, 64, 175, 0.14);
}

/* The thong ke noi 3D */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.97);
    padding: 22px 18px;
    border-radius: 18px;
    border: 1px solid #dbeafe;
    box-shadow:
        0 6px 0 #bfdbfe,
        0 12px 22px rgba(30, 64, 175, 0.16);
    transition: transform 0.25s ease,
                box-shadow 0.25s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    box-shadow:
        0 10px 0 #bfdbfe,
        0 20px 30px rgba(30, 64, 175, 0.22);
}

div[data-testid="stMetricLabel"] {
    font-size: 17px !important;
    font-weight: 700 !important;
    color: #475569 !important;
}

div[data-testid="stMetricValue"] {
    font-size: 32px !important;
    font-weight: 850 !important;
    color: #1d4ed8 !important;
}

/* Bang diem */
div[data-testid="stDataFrame"] {
    border: 1px solid #dbeafe;
    border-radius: 16px;
    overflow: hidden;
    box-shadow:
        0 7px 0 #bfdbfe,
        0 14px 25px rgba(30, 64, 175, 0.16);
}

/* Bieu do */
div[data-testid="stImage"],
div[data-testid="stPlotlyChart"] {
    border-radius: 16px;
}

/* Hop chon sinh vien */
div[data-baseweb="select"] > div {
    background: white;
    border: 1px solid #93c5fd;
    border-radius: 12px;
    min-height: 48px;
    box-shadow: 0 4px 0 #dbeafe;
    font-size: 18px;
}

/* Thong tin sinh vien */
.student-name {
    color: #1d4ed8;
    font-size: 29px;
    font-weight: 850;
    padding: 18px;
    margin: 15px 0 22px 0;
    background: linear-gradient(120deg, #eff6ff, #ffffff);
    border-radius: 15px;
    border-left: 6px solid #2563eb;
    box-shadow:
        0 5px 0 #bfdbfe,
        0 10px 20px rgba(37, 99, 235, 0.14);
}

/* Hop thong bao */
div[data-testid="stAlert"] {
    border-radius: 14px;
    box-shadow: 0 5px 0 #dbeafe,
                0 10px 18px rgba(15, 23, 42, 0.10);
}

/* Chu mo ta */
[data-testid="stCaptionContainer"] {
    font-size: 16px !important;
}

/* Duong phan cach */
hr {
    border-color: #bfdbfe;
    margin-top: 25px;
    margin-bottom: 25px;
}

/* Chan trang */
.footer {
    color: #64748b;
    text-align: center;
    font-size: 15px;
    padding: 22px;
    margin-top: 30px;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 16px;
    box-shadow:
        0 5px 0 #dbeafe,
        0 10px 20px rgba(30, 64, 175, 0.12);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 4. TAO DU LIEU 10 SINH VIEN
# =====================================================
data = {
    "Họ và tên": [
        "An", "Bình", "Cường", "Dũng", "Hà",
        "Lan", "Minh", "Nam", "Phúc", "Linh"
    ],
    "Chuyên cần": [9, 8, 7, 10, 6, 8, 9, 5, 7, 10],
    "Giữa kỳ": [8, 7, 6, 9, 5, 8, 7, 4, 6, 9],
    "Cuối kỳ": [9, 8, 7, 8, 6, 9, 8, 5, 7, 10]
}

df = pd.DataFrame(data)

# =====================================================
# 5. TINH DIEM TONG KET
# =====================================================
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

# =====================================================
# 6. XEP LOAI SINH VIEN
# =====================================================
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# =====================================================
# 7. TIEU DE TRANG WEB
# =====================================================
st.markdown("""
<div class="hero">
    <div class="hero-title">
        🎓 QUẢN LÝ ĐIỂM SINH VIÊN
    </div>
    <div class="hero-subtitle">
        Hệ thống thống kê, tra cứu và theo dõi kết quả học tập
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# 8. THONG KE TONG QUAN
# =====================================================
diem_tb = df["Tổng kết"].mean()
sv_cao = df.loc[df["Tổng kết"].idxmax()]
sv_thap = df.loc[df["Tổng kết"].idxmin()]
so_dat = (df["Tổng kết"] >= 5).sum()

st.markdown("""
<div class="section-title">
    📊 TỔNG QUAN KẾT QUẢ
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📈 Điểm trung bình", f"{diem_tb:.2f}/10")

with c2:
    st.metric("🏆 Điểm cao nhất", f"{sv_cao['Tổng kết']:.2f}")

with c3:
    st.metric("📉 Điểm thấp nhất", f"{sv_thap['Tổng kết']:.2f}")

with c4:
    st.metric("🎯 Sinh viên đạt", f"{so_dat}/{len(df)}")

st.info(
    f"🏆 Sinh viên cao điểm nhất: **{sv_cao['Họ và tên']}** "
    f"({sv_cao['Tổng kết']:.2f} điểm)"
)

st.info(
    f"📌 Sinh viên thấp điểm nhất: **{sv_thap['Họ và tên']}** "
    f"({sv_thap['Tổng kết']:.2f} điểm)"
)

st.divider()

# =====================================================
# 9. BANG DIEM CHI TIET
# =====================================================
st.markdown("""
<div class="section-title">
    📋 BẢNG ĐIỂM CHI TIẾT
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df.style.format({
        "Chuyên cần": "{:.1f}",
        "Giữa kỳ": "{:.1f}",
        "Cuối kỳ": "{:.1f}",
        "Tổng kết": "{:.2f}"
    }).background_gradient(
        subset=["Tổng kết"],
        cmap="RdYlGn",
        vmin=0,
        vmax=10
    ),
    use_container_width=True,
    hide_index=True,
    height=420
)

st.caption("💡 Cột Tổng kết được tô màu để dễ nhận biết kết quả học tập.")

st.divider()

# =====================================================
# 10. TRA CUU THONG TIN SINH VIEN
# =====================================================
st.markdown("""
<div class="section-title">
    👤 TRA CỨU THÔNG TIN SINH VIÊN
</div>
""", unsafe_allow_html=True)

ten = st.selectbox(
    "🔎 Chọn sinh viên cần tra cứu",
    df["Họ và tên"]
)

sv = df[df["Họ và tên"] == ten].iloc[0]

st.markdown(
    f"<div class='student-name'>🎓 {sv['Họ và tên']}</div>",
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    st.metric("📘 Điểm chuyên cần", f"{sv['Chuyên cần']:.1f}/10")

with b:
    st.metric("📗 Điểm giữa kỳ", f"{sv['Giữa kỳ']:.1f}/10")

with c:
    st.metric("📕 Điểm cuối kỳ", f"{sv['Cuối kỳ']:.1f}/10")

x, y = st.columns(2)

with x:
    st.metric("⭐ ĐIỂM TỔNG KẾT", f"{sv['Tổng kết']:.2f}/10")

with y:
    st.metric("🎯 XẾP LOẠI", sv["Xếp loại"])

st.divider()

# =====================================================
# 11. BIEU DO DIEM TONG KET CO BONG 3D
# =====================================================
st.markdown("""
<div class="section-title">
    📈 PHÂN TÍCH KẾT QUẢ HỌC TẬP
</div>
""", unsafe_allow_html=True)

# Cau hinh font tieng Viet
plt.rcParams["font.family"] = "DejaVu Sans"

fig, ax = plt.subplots(figsize=(12, 5))

fig.patch.set_facecolor("#f8fafc")
ax.set_facecolor("#f8fafc")

ten_sv = df["Họ và tên"].tolist()
diem = df["Tổng kết"].tolist()
x_pos = list(range(len(df)))
do_rong = 0.62

# Mau sac theo xep loai
mau = [
    "#16A34A" if d >= 8.5
    else "#2563EB" if d >= 7
    else "#F59E0B" if d >= 5
    else "#DC2626"
    for d in diem
]

# Tao bong lech phia sau cac cot
ax.bar(
    [x + 0.07 for x in x_pos],
    diem,
    width=do_rong,
    color="#64748b",
    alpha=0.25,
    zorder=2
)

# Ve cac cot chinh
cot = ax.bar(
    x_pos,
    diem,
    width=do_rong,
    color=mau,
    edgecolor="white",
    linewidth=1.8,
    zorder=3
)

# Hien thi diem tren dau cot
ax.bar_label(
    cot,
    fmt="%.2f",
    padding=5,
    fontsize=10,
    fontweight="bold"
)

# Duong diem trung binh
ax.axhline(
    diem_tb,
    color="#7C3AED",
    linestyle="--",
    linewidth=2.5,
    label=f"Điểm trung bình: {diem_tb:.2f}",
    zorder=4
)

ax.set_xticks(x_pos)
ax.set_xticklabels(ten_sv, fontsize=11)

ax.set_ylim(0, 11)
ax.set_ylabel("Điểm số", fontsize=13)
ax.set_xlabel("Họ và tên sinh viên", fontsize=13)

ax.set_title(
    "SO SÁNH ĐIỂM TỔNG KẾT",
    fontsize=17,
    fontweight="bold",
    color="#123b70",
    pad=20
)

ax.grid(
    axis="y",
    linestyle=":",
    alpha=0.35,
    zorder=1
)

ax.legend(fontsize=11)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.markdown("""
<div style="
    text-align:center;
    padding:14px;
    background:#ffffff;
    border-radius:12px;
    box-shadow:0 4px 0 #dbeafe, 0 8px 15px rgba(30,64,175,0.10);
">
    🟢 <b>Giỏi</b>
    &nbsp;&nbsp; 🔵 <b>Khá</b>
    &nbsp;&nbsp; 🟠 <b>Trung bình</b>
    &nbsp;&nbsp; 🔴 <b>Yếu</b>
</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# 12. CHAN TRANG
# =====================================================
st.markdown("""
<div class="footer">
    <b>🎓 QUẢN LÝ ĐIỂM SINH VIÊN</b><br><br>
    Người tạo: HỌ TÊN CỦA BẠN<br>
    Mã số sinh viên: MSSV CỦA BẠN<br><br>
    <span>Ứng dụng thực hành Python, Pandas và Streamlit</span>
</div>
""", unsafe_allow_html=True)
