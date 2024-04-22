import streamlit as st


def menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio_translator.py", label="Audio Translator")
    st.sidebar.page_link("pages/text_translator.py", label="Text Translator")


if __name__ == '__main__':
    menu()
