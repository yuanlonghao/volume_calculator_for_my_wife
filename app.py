import streamlit as st

st.title('计算箱子总体积')

length = st.number_input("长 (厘米)", value=0, min_value=0, step=1)
width = st.number_input("宽 (厘米)", value=0, min_value=0, step=1)
height = st.number_input("高 (厘米)", value=0, min_value=0, step=1)

n_package = st.number_input("箱子个数", value=0, min_value=0, step=1)

result = length * width * height * n_package / 1000000 
st.markdown(f"## {n_package}个箱子的总体积是**{result:.2f}**立方米。")
