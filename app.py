import streamlit as st
from agent import handle_input

st.title("🍽️ FoodieSpot AI Reservation Agent")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask me to reserve, recommend, or check restaurants!")

if user_input:
    st.session_state.chat.append({"role": "user", "text": user_input})
    response = handle_input(user_input, st.session_state)  # This should now work
    st.session_state.chat.append({"role": "ai", "text": response})

for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["text"])
    else:
        st.chat_message("assistant").markdown(msg["text"])
