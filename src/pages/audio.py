import streamlit as st
from app import menu
from Linguist import LangAgent


# Application Init
st.set_page_config(layout="wide")

# Draw main menu
menu()

st.markdown("""
    <div style="text-align:center">
        <h1>Audio Translator</h1>
    </div>
    """, unsafe_allow_html=True)


# UI with 2 columns
cols = st.columns([2, 0.1, 3])

with cols[0]:
    st.write("<h4>Upload the audio file:</h4>", unsafe_allow_html=True)
    audio_file = st.file_uploader("Upload Audio", type=['mp3', 'mp4'])

    # Button: Translate
    _, button_cell, _ = st.columns(3)
    with button_cell:
        button_translate = st.button('Translate', use_container_width=True)

with cols[2]:
    if audio_file and button_translate:
        st.write("<h4>The translated text will appear here shortly ...</h4>", unsafe_allow_html=True)

        language_agent = LangAgent()
        translated_text = language_agent.translate_audio(audio_file)
        result = language_agent.fix_grammar(translated_text)

        # Display translated text
        container1 = st.container(border=True)
        container1.markdown(f"""
        <span style="font-size: 20px;"> 
        {result}
        </span>
        """, unsafe_allow_html=True)

    else:
        st.write("<h4>Upload the audio file to translate.</h4>", unsafe_allow_html=True)

