import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import diffusers
import io
from app_sell import show_data
st.sidebar.title("เพิ่มสินค้า")
def display_uploaded_image(uploaded_files, name, price):
    """Displays the uploaded images on the Streamlit app."""
    col1, col2, col3 = st.columns(3)
    for idx, uploaded_file in enumerate(uploaded_files):
        if uploaded_file is not None:
            # Check if the file is empty
            if uploaded_file.size == 0:
                st.warning(f"Skipping empty file: Image {idx + 1}")
                continue
            # Read the image as bytes
            image_data = uploaded_file.read()
            # Use BytesIO to create an in-memory binary stream
            image_stream = io.BytesIO(image_data)
            # Open the image using Pillow (PIL)
            image = Image.open(image_stream)

            # Display the image in the corresponding column
            with col1 if idx == 0 else col2 if idx == 1 else col3:
                st.image(image, use_column_width=True)
                st.markdown(f"""<span style="background-color: white;">***{name}***  
                                    <br> ${price:.2f}$ $  
                                    </span>""",
                            unsafe_allow_html=True)
                st.button(f"เพิ่มลงในรายการ {idx+1}")
            
            if 'selected_data' in st.session_state:
                selected_data = st.session_state.selected_data
                st.write("ข้อมูลจากหน้าก่อนหน้า:")
                st.write(selected_data)
                
def display_saved_image(image_path):
    if image_path is not None:
        # Open the saved image using Pillow (PIL)
        try:
            saved_image = Image.open(image_path)
            # Display the image using Streamlit st.image
            st.image(saved_image, caption='Saved Image', use_column_width=True)
        except FileNotFoundError:
            st.error(f"File not found: {image_path}")

def form_callback():
    if 'my_checkbox' not in st.session_state:
        st.session_state.my_checkbox = False
    st.write("Checkbox:", st.session_state.my_checkbox)
    uploaded_files = st.session_state.uploaded_files
    name = st.session_state.name
    price = st.session_state.price
    display_uploaded_image(uploaded_files, name, price) 
    
with st.sidebar.form(key='my_form'):
    uploaded_files = st.file_uploader("Upload Images (PNG, JPG)", type=['png', 'jpg'], key='uploaded_files', accept_multiple_files=True)
    name = st.text_input(label="ชื่อ", key="name")
    price = st.number_input(label="ราคา", key="price", min_value=0, step=1)
    globals()['uploaded_files'] = uploaded_files
    globals()['name'] = name
    globals()['price'] = price
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

st.sidebar.title("เพศ")
people = st.sidebar.radio("Choose", ["ชาย", "หญิง",])
if people == "ชาย":
    col1, col2, col3 = st.columns(3)
    for col in [col1, col2, col3]:
        col.container().style.background_color = "white"
    with col1:
        st.container().style.background_color = "white"
        st.image("img/man2 (1).jpg", use_column_width=True)
        st.markdown(f"""<span style="background-color: white;">**กางเกงยีนชาย** 
                    <br> ${2000.00}$ $  
                    </span>""", unsafe_allow_html=True)
        if st.button("เพิ่มลงในรายการ1"):
            # Redirect to another page or perform other actions
            st.page_link("app_sell.py")
            
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col2:
        st.container().style.background_color = "white"
        st.image("img/man2 (2).jpg", use_column_width=True)
        st.markdown(f"""<span style="background-color: white;">**กางเกงผู้ชายสีขาว** 
                    <br> ${2000.00}$ $  
                    </span>""", unsafe_allow_html=True)
        st.button("เพิ่มลงในรายการ2")
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col3:
        st.container().style.background_color = "white"
        st.image("img/man2 (3).jpg", use_column_width=True)
        st.markdown(f"""<span style="background-color: white;">**กางเกงสีน้ำเงิน** 
                    <br> ${2000.00}$ $  
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
        st.markdown(f"""<span style="background-color: white;">**กางเกงสีดำ** 
                    <br> ${2000.00}$ $  
                    </span>""", unsafe_allow_html=True)
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col2:
        st.container().style.background_color = "white"
        st.image("img/img2.jpg", use_column_width=True)
        st.markdown(f"""<span style="background-color: white;">**กางเกงสีน้ำตาล** 
                    <br> ${2000.00}$ $  
                    </span>""", unsafe_allow_html=True)
        st.image("img/img1.jpg", use_column_width=True)
        st.markdown("""**คำอธิบายภาพ 1** <br> <span style="background-color: white;">เพิ่มเติม</span>""", unsafe_allow_html=True)
    with col3:
        st.container().style.background_color = "white"
        st.image("img/img3.jpg", use_column_width=True)
        st.markdown(f"""<span style="background-color: white;">**กางเกงสีน้ำเงิน** 
                    <br> ${2000.00}$ $ 
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
    

