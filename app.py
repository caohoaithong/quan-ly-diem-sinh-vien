
# 1. Import thu vien
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 2. Tao du lieu
data = {
    "Ho_ten": ["An", "Binh", "Cuong", "Dung", "Ha",
               "Lan", "Minh", "Nam", "Phuc", "Linh"],
    "Chuyen_can": [9, 8, 7, 10, 6, 8, 9, 5, 7, 10],
    "Giua_ky": [8, 7, 6, 9, 5, 8, 7, 4, 6, 9],
    "Cuoi_ky": [9, 8, 7, 8, 6, 9, 8, 5, 7, 10]
}

df = pd.DataFrame(data)

# 3. Tinh diem
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# 4. Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tieu de va bang diem
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm")
st.dataframe(df)

# 6. Thong ke
st.subheader("Thống kê")

st.write("Điểm trung bình:", round(df["Tong_ket"].mean(), 2))
st.write("Cao nhất:", df.loc[df["Tong_ket"].idxmax(), "Ho_ten"])
st.write("Thấp nhất:", df.loc[df["Tong_ket"].idxmin(), "Ho_ten"])
st.write("Số sinh viên đạt:", (df["Tong_ket"] >= 5).sum())

# 7. Chon sinh vien
st.subheader("Thông tin sinh viên")

ten = st.selectbox("Chon sinh vien", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Chuyen can:", sv["Chuyen_can"])
st.write("Giua ky:", sv["Giua_ky"])
st.write("Cuoi ky:", sv["Cuoi_ky"])
st.write("Tong ket:", round(sv["Tong_ket"], 2))
st.write("Xep loai:", sv["Xep_loai"])

# 8. Bieu do
st.subheader("Bieu do diem tong ket")

fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Ho ten")
ax.set_ylabel("Diem")
ax.set_ylim(0, 10)

st.pyplot(fig)

# 9. Thong tin nguoi tao
st.caption("Nguoi tao: Cao Hoai Thong | MSSV: 052208010748")
