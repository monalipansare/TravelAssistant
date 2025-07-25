import streamlit as st
import os
from utils import get_base64

st.set_page_config(page_title="Home", layout="centered")


img_base64 = get_base64("assets/travel.jpg")

image_path = "assets/travel.jpg"
if os.path.exists(image_path):
    img_base64 = get_base64(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;

        
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✈️ Welcome to TravelAssistant 🌍")
st.markdown("#### Your smart travel mate, here to make journeys easier 🧭")
st.markdown("- Plan trips easily 🗺️\n- Get travel suggestions 🧳\n- Chat with our travel bot 🤖")

if st.button("🔐 Login"):
    st.switch_page("pages/login.py")
