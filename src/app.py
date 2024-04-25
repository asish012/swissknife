import streamlit as st


def menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio.py", label="Audio")
    st.sidebar.page_link("pages/text.py", label="Text")


if __name__ == '__main__':
    menu()
