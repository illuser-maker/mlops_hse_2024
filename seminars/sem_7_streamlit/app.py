import streamlit as st
from time import sleep


just_a_num = st.slider("Just a num", -100, 100, 42, 1)


st.scatter_chart([[just_a_num + 10, just_a_num + 10], [just_a_num, just_a_num]], width=200)
