import streamlit as st
import pandas as pd
import numpy as np
import torch
from diffusers import DiffusionPipeline as DP
from PIL import Image, ImageDraw, ImageFont

#sidebar
st.sidebar.title("เพศ")
people = st.sidebar.radio("Choose", ["ชาย", "หญิง",])
if people == "ชาย":
    st.title("ชาย")
elif people == "หญิง":
    st.title("หญิง")
st.sidebar.title("เลือกซื้อตามราคา")
price = st.sidebar.radio("Choose", ["ต่ำกว่า2000$", "2000-4000",])
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
def text_to_image(text, diffuser_model):
    #diffuser = diffusers.load_diffuser(diffuser_model)
    #image_data = df.generate(text)
    #image = Image.fromarray(image_data)
    #image.show()
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5", 
                            torch_dtype=torch.float16)
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    image.show()

if __name__ == "__main__":
    input_text = "Hello, World!"
    diffuser_model = "example_diffuser_model"
    text_to_image(input_text, diffuser_model)

col1, col2, col3 = st.columns(3)
with col1:
   st.image("https://static.streamlit.io/examples/cat.jpg")
   st.caption("This is a cat.")
   st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   st.image("https://static.streamlit.io/examples/dog.jpg")
   st.image("https://static.streamlit.io/examples/cat.jpg")
with col3:
   st.image("https://static.streamlit.io/examples/owl.jpg")
   st.image("https://static.streamlit.io/examples/cat.jpg")

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
    

