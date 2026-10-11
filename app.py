
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
st.title("🎓 QUẢN LÝ ĐIỂM SINH VIÊN")
st.caption("Hệ thống thống kê và theo dõi kết quả học tập")
st.divider()

# 7. Thống kê tổng quan
diem_tb = df["Tổng kết"].mean()
sv_cao = df.loc[df["Tổng kết"].idxmax()]
sv_thap = df.loc[df["Tổng kết"].idxmin()]
so_dat = (df["Tổng kết"] >= 5).sum()

st.subheader("📊 Tổng quan kết quả")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{diem_tb:.2f}/10")
c2.metric("Điểm cao nhất", f"{sv_cao['Tổng kết']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_thap['Tổng kết']:.2f}")
c4.metric("Số sinh viên đạt", f"{so_dat}/10")

st.caption(
    f"🏆 Điểm cao nhất: {sv_cao['Họ và tên']} | "
    f"📌 Điểm thấp nhất: {sv_thap['Họ và tên']}"
)

st.divider()

# 8. Bảng điểm
st.subheader("📋 Bảng điểm chi tiết")

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
    hide_index=True
)

st.divider()

# 9. Tra cứu sinh viên
st.subheader("👤 Tra cứu thông tin sinh viên")

ten = st.selectbox("Chọn sinh viên", df["Họ và tên"])
sv = df[df["Họ và tên"] == ten].iloc[0]

a, b, c = st.columns(3)

a.metric("Điểm chuyên cần", f"{sv['Chuyên cần']:.1f}")
b.metric("Điểm giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c.metric("Điểm cuối kỳ", f"{sv['Cuối kỳ']:.1f}")

x, y = st.columns(2)

x.metric("ĐIỂM TỔNG KẾT", f"{sv['Tổng kết']:.2f}/10")
y.metric("XẾP LOẠI", sv["Xếp loại"])

st.divider()

# 10. Biểu đồ
st.subheader("📈 Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(11, 4))

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
    edgecolor="white",
    width=0.7
)

ax.axhline(
    diem_tb,
    color="#7C3AED",
    linestyle="--",
    label=f"Điểm trung bình: {diem_tb:.2f}"
)

ax.bar_label(cot, fmt="%.2f", padding=3, fontsize=9)
ax.set_ylim(0, 11)
ax.set_ylabel("Điểm số")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_title("SO SÁNH ĐIỂM TỔNG KẾT")
ax.grid(axis="y", linestyle=":", alpha=0.4)
ax.legend()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption(
    "🟢 Giỏi | 🔵 Khá | 🟠 Trung bình | 🔴 Yếu"
)

st.divider()

# 11. Chân trang
st.markdown(
    "<div style='text-align:center; color:gray; font-size:12px;'>"
    "QUẢN LÝ ĐIỂM SINH VIÊN<br>"
    "Người tạo: HỌ TÊN CỦA BẠN | MSSV: MÃ SỐ CỦA BẠN"
    "</div>",
    unsafe_allow_html=True
)
