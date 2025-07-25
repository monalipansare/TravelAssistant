import json
import os
import streamlit as st

# Path to the JSON file
DATA_FILE = "data/user_data.json"

# Load existing users
def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"users": []}

# Save users back to the file
def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Streamlit UI
st.title("📝 Register for TravelAssistant")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
username = st.text_input("Email (Username)")
password = st.text_input("Password", type="password")

if st.button("Register"):
    try:
        if not first_name or not last_name or not username or not password:
            st.error("All fields are required!")
        else:
            data = load_users()
            users = data.get("users", [])

            # Check if user already exists
            if any(user["username"] == username for user in users):
                st.error("User already exists!")
            else:
                new_user = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "password": password
                }
                users.append(new_user)
                data["users"] = users  # Update the dict
                save_users(data)
                st.success("Registration successful! Redirecting to login...")
                st.switch_page("pages/login.py")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
