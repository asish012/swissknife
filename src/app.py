import streamlit as st


# Application Init
st.set_page_config(layout="wide")

# Sidebar Menu
def menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/audio.py", label="Audio")
    st.sidebar.page_link("pages/text.py", label="Text")


if __name__ == '__main__':
    menu()
