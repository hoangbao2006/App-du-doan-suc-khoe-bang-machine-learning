import streamlit as st
import pickle
import numpy as np

# --- Load model (nếu có model.pkl thì load, còn không thì tính BMI trực tiếp) ---
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    use_model = True
except:
    model = None
    use_model = False

st.title("Ứng dụng Dự đoán Sức khỏe 🩺")

st.write("Nhập các thông số cơ bản để dự đoán tình trạng sức khỏe:")

# --- Input ---
height = st.number_input("Chiều cao (cm)", min_value=100, max_value=220, value=165)
weight = st.number_input("Cân nặng (kg)", min_value=30, max_value=150, value=60)
age = st.number_input("Tuổi", min_value=1, max_value=120, value=20)

if st.button("Dự đoán"):
    if use_model:
        # Nếu có model đã train
        features = np.array([[height, weight, age]])
        prediction = model.predict(features)
        st.success(f"Kết quả dự đoán: {prediction[0]}")
    else:
        # Nếu chưa có model thì dùng công thức BMI cơ bản
        height_m = height / 100
        bmi = weight / (height_m**2)

        if bmi < 18.5:
            result = "Thiếu cân"
        elif 18.5 <= bmi < 25:
            result = "Bình thường"
        elif 25 <= bmi < 30:
            result = "Thừa cân"
        else:
            result = "Béo phì"

        st.success(f"Chỉ số BMI = {bmi:.2f} → Tình trạng: {result}")
