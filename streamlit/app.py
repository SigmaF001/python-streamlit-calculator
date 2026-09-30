import streamlit as st

st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 โปรแกรมเครื่องคิดเลข")
st.write("สร้างด้วย Python และ Streamlit")

# รับค่าตัวเลข
num1 = st.number_input("กรอกตัวเลขที่ 1", value=0.0)

operation = st.selectbox(
    "เลือกเครื่องหมาย",
    ["+", "-", "×", "÷", "^", "%"]
)

num2 = st.number_input("กรอกตัวเลขที่ 2", value=0.0)

# ปุ่มคำนวณ
if st.button("คำนวณ", use_container_width=True):

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "×":
        result = num1 * num2

    elif operation == "÷":
        if num2 == 0:
            st.error("ไม่สามารถหารด้วย 0 ได้")
            result = None
        else:
            result = num1 / num2

    elif operation == "^":
        result = num1 ** num2

    elif operation == "%":
        if num2 == 0:
            st.error("ไม่สามารถหารเอาเศษด้วย 0 ได้")
            result = None
        else:
            result = num1 % num2

    if result is not None:
        st.success(f"ผลลัพธ์ = {result}")