import streamlit as st

st.title("Ultrasound Exam")

mode = st.radio("Choose a mode:", ("Learning", "Evaluation"))

if mode == "Learning":
    st.write("You have selected learning mode. Get ready to learn!")
elif mode == "Evaluation":
    st.write("You have selected evaluation mode. Put your knowledge to the test!")
