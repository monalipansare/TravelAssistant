# import streamlit as st

# st.set_page_config(page_title="TravelAssistant ChatBot", layout="centered")
# st.title("🤖 TravelAssistant ChatBot")

# st.markdown("🚀 Coming soon: Talk with your AI travel assistant! ✈️🗺️🏖️")

# if st.button("🔙 Logout"):
#     st.switch_page("home")

import streamlit as st
from utils import get_suggestions

st.title("🧳 Travel Assistant")

if "stage" not in st.session_state:
    st.session_state.stage = "greet"
    st.session_state.city = ""
    st.session_state.preference = ""

if "chat" not in st.session_state:
    st.session_state.chat = []

def add_bot_message(msg):
    st.session_state.chat.append(("bot", msg))

def add_user_message(msg):
    st.session_state.chat.append(("user", msg))

for sender, msg in st.session_state.chat:
    if sender == "bot":
        st.chat_message("assistant").write(msg)
    else:
        st.chat_message("user").write(msg)

user_input = st.chat_input("What would you like to ask?")

if user_input:
    add_user_message(user_input)

    if st.session_state.stage == "greet":
        add_bot_message("Hi there! 👋 Where do you want to head today?")
        st.session_state.stage = "ask_city"

    elif st.session_state.stage == "ask_city":
        st.session_state.city = user_input.strip()
        add_bot_message(f"Great! What kind of places do you prefer in {st.session_state.city.title()}? ✨\nOptions: holy, historic, shopping, food, nature")
        st.session_state.stage = "ask_preference"

    elif st.session_state.stage == "ask_preference":
        st.session_state.preference = user_input.strip().lower()
        suggestions = get_suggestions(st.session_state.city, st.session_state.preference)

        if suggestions:
            add_bot_message(f"Here are some top {st.session_state.preference} places in {st.session_state.city.title()}:\n• " + "\n• ".join(suggestions))
            st.session_state.stage = "done"
        else:
            add_bot_message(f"Sorry, I couldn't find any {st.session_state.preference} places in {st.session_state.city.title()}. Try another category.")
            st.session_state.stage = "ask_preference"

    else:
        add_bot_message("Want to explore another city? Just say the name!")

    st.rerun()

