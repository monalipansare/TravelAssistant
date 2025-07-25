import streamlit as st
from utils import authenticate_user, is_valid_email

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Login to TravelAssistant")

with st.form("login_form"):
    username = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        if not is_valid_email(username):
            st.error("Invalid email format.")
        elif authenticate_user(username, password):
            st.success("Login successful! Redirecting to ChatBot 🤖...")
            st.switch_page("pages/chatbot.py")
        else:
            st.error("Incorrect username or password.")

if st.button("🔙 Back to Home"):
    st.switch_page("home.py")

st.markdown("Not registered yet? 👉 [Register here](register)")
