import streamlit as st

def show_data():
   price = st.number_input(label="ราคา", key="price", min_value=0, step=1)