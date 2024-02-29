import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("เพศ")
page = st.sidebar.radio("Choose", ["ชาย", "หญิง",])
if page == "ชาย":
    st.title("ชาย")
elif page == "หญิง":
    st.title("หญิง")

add_selectbox = st.sidebar.selectbox(
    "เลือกซื้อตามราคา",
    ("2000$", "30000$")
)
for idx, img in enumerate(filteredImages): 
        cols = st.beta_columns(4) 
        
        cols[0].image("https://static.streamlit.io/examples/cat.jpg",[idx], use_column_width=True)
        idx+=1
        cols[1].image("https://static.streamlit.io/examples/cat.jpg",[idx], use_column_width=True)
        idx+=idx
        cols[2].image("https://static.streamlit.io/examples/cat.jpg",[idx], use_column_width=True)
        idx+=idx
        cols[3].image("https://static.streamlit.io/examples/cat.jpg",[idx], use_column_width=True)
        idx+=idx

# col1, col2, col3 = st.columns(3)
# image_size = (300, 300)
# with col2( width=image_size[0], height=image_size[1]):
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")
# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")
# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230616/pngtree-3d-mountain-landscape-with-a-serene-lake-background-image_3626132.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
    

