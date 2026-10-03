import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi tiền gửi tiết kiệm_ HÀ TRUNG KIÊN",
    page_icon="💰",
    layout="centered"
)
st.image("logo.jpg")

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("💰 APP TÍNH LÃI TIỀN GỬI TIẾT KIỆM_HÀ TRUNG KIÊN")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

st.divider()

# ==============================
# NHẬP THÔNG TIN
# ==============================

# Số tiền gửi
so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=500_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=3,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# NÚT TÍNH TOÁN
# ==============================

if st.button("🧮 TÍNH TIỀN LÃI", use_container_width=True):

    # Đổi lãi suất từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Quy đổi kỳ hạn từ tháng sang năm
    so_nam = ky_han / 12

    # --------------------------------
    # TRƯỜNG HỢP NHẬN LÃI CUỐI KỲ
    # --------------------------------
    if hinh_thuc == "Cuối kỳ":

        # Lãi đơn
        tong_tien_lai = so_tien_gui * lai_suat_nam * so_nam

        # Lãi định kỳ = toàn bộ tiền lãi cuối kỳ
        tien_lai_dinh_ky = tong_tien_lai

    # --------------------------------
    # TRƯỜNG HỢP NHẬN LÃI HÀNG THÁNG
    # --------------------------------
    elif hinh_thuc == "Hàng tháng":

        # Lãi mỗi tháng
        tien_lai_dinh_ky = (
            so_tien_gui * lai_suat_nam / 12
        )

        # Tổng tiền lãi
        tong_tien_lai = tien_lai_dinh_ky * ky_han

    # --------------------------------
    # TRƯỜNG HỢP NHẬN LÃI HÀNG QUÝ
    # --------------------------------
    else:

        # Lãi mỗi quý
        tien_lai_dinh_ky = (
            so_tien_gui * lai_suat_nam / 4
        )

        # Số quý
        so_quy = ky_han / 3

        # Tổng tiền lãi
        tong_tien_lai = tien_lai_dinh_ky * so_quy

    # Tổng tiền nhận được
    tong_tien = so_tien_gui + tong_tien_lai

    # ==============================
    # HIỂN THỊ KẾT QUẢ
    # ==============================

    st.success("✅ TÍNH TOÁN THÀNH CÔNG!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💵 Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.divider()

    st.subheader("💰 Tổng số tiền nhận được")

    st.metric(
        "Gốc + Lãi",
        f"{tong_tien:,.0f} VNĐ"
    )

    # ==============================
    # THÔNG TIN CHI TIẾT
    # ==============================

    st.divider()

    st.subheader("📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
