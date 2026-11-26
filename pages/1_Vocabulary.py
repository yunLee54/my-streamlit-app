import streamlit as st

st.title("📝 Vocabulary Practice")

word = st.text_input("Enter an English word")

if word:
    st.write("You entered:", word)
