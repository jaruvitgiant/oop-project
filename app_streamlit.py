import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import diffusers

sidebar = st.sidebar
image_file = sidebar.file_uploader("อัปโหลดไฟล์ภาพสินค้า", type=["png", "jpg", "jpeg"])
if image_file is not None:
    bytes_data = image_file.read()
    sidebar.image(bytes_data)
    with st.sidebar:
        name = st.text_input("ชื่อสินค้า")
    number_input_value = st.sidebar.number_input("ราคา", min_value=0, max_value=100, value=50)
    button = sidebar.button("บันทึก")
    if button:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.container().style.background_color = "white"
            # แสดงรูปที่อัปโหลด
            st.container().style.background_color = "white"
            st.image(bytes_data, use_column_width=True)
            st.markdown(f"""<span style="background-color: white;">{name}
                        <br> {number_input_value}$
                        </span>""", unsafe_allow_html=True)
            st.button("เพิ่มลงในรายการ")
        

st.sidebar.title("เพศ")
people = st.sidebar.radio("Choose", ["ชาย", "หญิง",])
if people == "ชาย":
    col1, col2, col3 = st.columns(3)
    for col in [col1, col2, col3]:
        col.container().style.background_color = "white"
    with col1:
        st.container().style.background_color = "white"
        st.image("img/man2 (1).jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงยีนชาย** 
                    <br> 2000$
                    </span>""", unsafe_allow_html=True)
        st.button("เพิ่มลงในรายการ1")
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col2:
        st.container().style.background_color = "white"
        st.image("img/man2 (2).jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงผู้ชายสีขาว** 
                    <br> 2100$
                    </span>""", unsafe_allow_html=True)
        st.button("เพิ่มลงในรายการ2")
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col3:
        st.container().style.background_color = "white"
        st.image("img/man2 (3).jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงสีน้ำเงิน** 
                    <br> 1999$
                    </span>""", unsafe_allow_html=True)
        st.button("เพิ่มลงในรายการ3")
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)


elif people == "หญิง":
    st.title("หญิง")
    col1, col2, col3 = st.columns(3)
    for col in [col1, col2, col3]:
        col.container().style.background_color = "white"
    with col1:
        st.container().style.background_color = "white"
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงสีดำ** 
                    <br> 2000$
                    </span>""", unsafe_allow_html=True)
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)

    with col2:
        st.container().style.background_color = "white"
        st.image("img/img2.jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงสีน้ำตาล** 
                    <br> 2100$
                    </span>""", unsafe_allow_html=True)
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col3:
        st.container().style.background_color = "white"
        st.image("img/img3.jpg", use_column_width=True)
        st.markdown("""<span style="background-color: white;">**กางเกงสีน้ำเงิน** 
                    <br> 1999$
                    </span>""", unsafe_allow_html=True)
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)




st.sidebar.title("เลือกซื้อตามราคา")
price = st.sidebar.radio("Choose", ["ต่ำกว่า2000$", "2000-4000$",])
if price == "ต่ำกว่า2000$":
    pass
elif price == "2000-4000$":
    pass
st.sidebar.title("ลดราคา&ข้อเสนอ")
price_offer = st.sidebar.radio("Choose", ["ล้างสต๊อก",])
st.sidebar.title("สี")
col1, col2 = st.sidebar.columns(2)
checked1 = col1.checkbox("สีเเดง", key="checkbox_1")
checked2 = col2.checkbox("สีเขียว", key="checkbox_2")

checked3 = col1.checkbox("สีดำ", key="checkbox_3")
checked4 = col2.checkbox("สีขาว", key="checkbox_4")
col1.markdown(
    f"""<style>
     {{
        background-color: {'#00ff00' if checked1 or checked3 else '#33CC33'};
    }}
    </style>""",
    unsafe_allow_html=True,
)
col2.markdown(
    f"""<style>
     {{
        background-color: {'#00ff00' if checked2 or checked4 else '#33CC33'};
    }}
    </style>""",
    unsafe_allow_html=True,
)
#body
youtube_url = "https://youtu.be/xAciowWaCIc?si=EqlvUmHNB9BU9WHI"
st.video(youtube_url)
st.markdown(
    f"""
    <div style="float: right;">
        <video width="640" height="360" autoplay controls style="display:none;">
            <source src="{youtube_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """,
    unsafe_allow_html=True
)

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20230616/pngtree-3d-mountain-landscape-with-a-serene-lake-background-image_3626132.jpg");
# background-size: cover;
# background-position: center center;
# background-repeat: no-repeat;
# background-attachment: local;
# }}
# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)
    

