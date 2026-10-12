
# 1. Import thư viện
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 2. Cấu hình giao diện
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

# Giao dien CSS
st.markdown("""
<style>
/* Nen trang */
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #f5f3ff, #ffffff);
}

/* Noi dung chinh */
.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Co chu to hon */
html, body, [class*="st-"] {
    font-size: 18px;
}

h1 {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #123b70 !important;
}

h2 {
    font-size: 30px !important;
    color: #174a8b !important;
}

h3 {
    font-size: 24px !important;
}

/* The noi */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid #dbeafe;
    border-radius: 18px;
    padding: 22px 20px;
    box-shadow: 0 6px 18px rgba(30, 64, 175, 0.12);
    transition: all 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 25px rgba(30, 64, 175, 0.20);
}

div[data-testid="stMetricLabel"] {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #475569 !important;
}

div[data-testid="stMetricValue"] {
    font-size: 34px !important;
    font-weight: 800 !important;
    color: #1d4ed8 !important;
}

/* Khung bang va bieu do */
div[data-testid="stDataFrame"],
div[data-testid="stPlotlyChart"] {
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.10);
}

/* Hop chon sinh vien */
div[data-baseweb="select"] > div {
    border-radius: 12px;
    border: 1px solid #93c5fd;
    min-height: 48px;
    font-size: 18px;
}

/* Chu mo ta */
[data-testid="stCaptionContainer"] {
    font-size: 16px !important;
    color: #475569 !important;
}

/* Duong phan cach */
hr {
    border-color: #bfdbfe;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

/* Tieu de cac khu vuc */
.section-title {
    font-size: 28px;
    font-weight: 850;
    color: #123b70;
    padding: 16px 22px;
    margin: 18px 0 22px 0;
    background: linear-gradient(120deg, #ffffff, #dbeafe);
    border-left: 7px solid #2563eb;
    border-radius: 14px;
    box-shadow:
        0 5px 0 #bfdbfe,
        0 10px 18px rgba(30, 64, 175, 0.16);
    text-shadow: 1px 1px 1px rgba(15, 23, 42, 0.08);
}

/* The thong ke 3D */
div[data-testid="stColumn"] .metric-card {
    border-radius: 18px;
    padding: 8px;
    margin-bottom: 16px;
    background: #ffffff;
    box-shadow:
        0 6px 0 #cbd5e1,
        0 12px 20px rgba(15, 23, 42, 0.14);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

div[data-testid="stColumn"] .metric-card:hover {
    transform: translateY(-6px);
    box-shadow:
        0 10px 0 #cbd5e1,
        0 20px 28px rgba(15, 23, 42, 0.20);
}

/* Vien mau cho tung the */
.metric-card.blue {
    border-top: 5px solid #2563eb;
}

.metric-card.green {
    border-top: 5px solid #16a34a;
}

.metric-card.red {
    border-top: 5px solid #dc2626;
}

.metric-card.purple {
    border-top: 5px solid #7c3aed;
}

/* Khung noi dung */
.content-card {
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid #dbeafe;
    border-radius: 20px;
    padding: 22px;
    margin: 10px 0 25px 0;
    box-shadow:
        0 7px 0 #dbeafe,
        0 14px 25px rgba(30, 64, 175, 0.13);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.content-card:hover {
    transform: translateY(-3px);
    box-shadow:
        0 10px 0 #bfdbfe,
        0 20px 32px rgba(30, 64, 175, 0.18);
}

/* Ten sinh vien */
.student-name {
    font-size: 30px;
    font-weight: 800;
    color: #1d4ed8;
    padding: 18px;
    margin: 15px 0;
    border-radius: 14px;
    background: linear-gradient(120deg, #eff6ff, #ffffff);
    box-shadow:
        0 5px 0 #bfdbfe,
        0 10px 18px rgba(37, 99, 235, 0.12);
}

/* Nut va hop chon */
.stButton button,
div[data-baseweb="select"] > div {
    border-radius: 12px;
    transition: all 0.2s ease;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 0 #bfdbfe,
                0 9px 15px rgba(37, 99, 235, 0.15);
}

</style>
""", unsafe_allow_html=True)


# 3. Tạo dữ liệu
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

# 4. Tính điểm tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
)

# 5. Xếp loại
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

# 6. Tiêu đề

st.markdown("""
<div style="
    background: linear-gradient(120deg, #123b70, #2563eb, #7c3aed);
    padding: 32px;
    border-radius: 22px;
    box-shadow: 0 10px 28px rgba(37, 99, 235, 0.25);
    margin-bottom: 25px;
">
    <div style="font-size: 42px; font-weight: 800; color: white;">
        🎓 QUẢN LÝ ĐIỂM SINH VIÊN
    </div>
    <div style="font-size: 19px; color: #dbeafe; margin-top: 12px;">
        Hệ thống thống kê và theo dõi kết quả học tập
    </div>
</div>
""", unsafe_allow_html=True)



# 7. Thống kê tổng quan
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
    st.markdown('<div class="metric-card blue">', unsafe_allow_html=True)
    st.metric("📈 Điểm trung bình", f"{diem_tb:.2f}/10")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="metric-card green">', unsafe_allow_html=True)
    st.metric("🏆 Điểm cao nhất", f"{sv_cao['Tổng kết']:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.markdown('<div class="metric-card red">', unsafe_allow_html=True)
    st.metric("📉 Điểm thấp nhất", f"{sv_thap['Tổng kết']:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

with c4:
    st.markdown('<div class="metric-card purple">', unsafe_allow_html=True)
    st.metric("🎯 Sinh viên đạt", f"{so_dat}/{len(df)}")
    st.markdown('</div>', unsafe_allow_html=True)

st.info(
    f"🏅 Sinh viên có điểm cao nhất: **{sv_cao['Họ và tên']}** "
    f"({sv_cao['Tổng kết']:.2f} điểm)"
)

st.divider()


# 8. Bảng điểm
st.markdown("""
<div class="section-title">
    📋 BẢNG ĐIỂM CHI TIẾT
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-card">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
st.caption("💡 Điểm tổng kết được tô màu để dễ nhận biết kết quả.")
st.divider()


# 9. Tra cứu sinh viên
st.markdown("""
<div class="section-title">
    👤 TRA CỨU THÔNG TIN SINH VIÊN
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-card">'

ten = st.selectbox("🔎 Chọn sinh viên cần tra cứu", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten].iloc[0]

st.markdown(
    f"<div class='student-name'>🎓 {sv['Họ và tên']}</div>",
    unsafe_allow_html=True
)

a, b, c = st.columns(3)
a.metric("📘 Điểm chuyên cần", f"{sv['Chuyên cần']:.1f}/10")
b.metric("📗 Điểm giữa kỳ", f"{sv['Giữa kỳ']:.1f}/10")
c.metric("📕 Điểm cuối kỳ", f"{sv['Cuối kỳ']:.1f}/10")

x, y = st.columns(2)

x.metric("⭐ ĐIỂM TỔNG KẾT", f"{sv['Tổng kết']:.2f}/10")
y.metric("🎯 XẾP LOẠI", sv["Xếp loại"])

st.markdown('</div>', unsafe_allow_html=True)
st.divider()
, unsafe_allow_html=True)


# 10. Biểu đồ
st.markdown("""
<div class="section-title">
    📈 PHÂN TÍCH KẾT QUẢ HỌC TẬP
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="content-card">', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor("#f8fafc")
ax.set_facecolor("#f8fafc")

mau = [
    "#16A34A" if d >= 8.5
    else "#2563EB" if d >= 7
    else "#F59E0B" if d >= 5
    else "#DC2626"
    for d in df["Tổng kết"]
]

cot = ax.bar(
    df["Họ và tên"],
    df["Tổng kết"],
    color=mau,
    width=0.65,
    edgecolor="white",
    linewidth=2,
    zorder=3
)

# Tạo bóng đổ lệch nhẹ cho từng cột
for bar in cot:
    x = bar.get_x()
    y = bar.get_height()
    w = bar.get_width()

    ax.bar(
        x + 0.035, y,
        width=w,
        color="#94a3b8",
        alpha=0.22,
        zorder=2
    )

ax.axhline(
    diem_tb,
    color="#7C3AED",
    linestyle="--",
    linewidth=2.5,
    label=f"Điểm trung bình: {diem_tb:.2f}",
    zorder=4
)

ax.bar_label(cot, fmt="%.2f", padding=5, fontsize=10, fontweight="bold")

ax.set_ylim(0, 11)
ax.set_ylabel("Điểm số", fontsize=12)
ax.set_xlabel("Sinh viên", fontsize=12)
ax.set_title(
    "SO SÁNH ĐIỂM TỔNG KẾT",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax.grid(axis="y", linestyle=":", alpha=0.3, zorder=1)
ax.legend(fontsize=11)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.markdown('</div>', unsafe_allow_html=True)

st.caption("🟢 Giỏi  |  🔵 Khá  |  🟠 Trung bình  |  🔴 Yếu")
st.divider()

# 11. Chân trang
st.markdown(
    "<div style='text-align:center; color:gray; font-size:12px;'>"
    "QUẢN LÝ ĐIỂM SINH VIÊN<br>"
    "Người tạo: HỌ TÊN CỦA BẠN | MSSV: MÃ SỐ CỦA BẠN"
    "</div>",
    unsafe_allow_html=True
)
