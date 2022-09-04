import streamlit as st

st.title('计算箱子总体积')

length = st.number_input("长 (厘米)")#, value=0, min_value=0, step=1.0)
width = st.number_input("宽 (厘米)")#, value=0, min_value=0, step=1.0)
height = st.number_input("高 (厘米)")#, value=0, min_value=0, step=1.0)

n_package = st.number_input("箱子个数")#, value=0, min_value=0, step=1.0)

# calculation = st.button("计算总体积")

result = length * width * height * n_package / 1000000 
st.sidebar.markdown(f"{n_package}个箱子的总体积是{result:.2f}立方米。")

# if calculation:
#      st.write(f"{n_package}个箱子的总体积是{result}立方米。")
# else:
#      st.write('')