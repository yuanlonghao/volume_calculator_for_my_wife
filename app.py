import streamlit as st

st.title('计算箱子总体积')

length = st.number_input("长 (厘米)")
width = st.number_input("宽 (厘米)")
height = st.number_input("高 (厘米)")

n_package = st.number_input("箱子个数")

clicked = st.button("计算总体积")