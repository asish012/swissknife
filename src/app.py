import streamlit as st
import json
import re
from Translator import Translator, FinancialAdvisor


# Application Init
# st.set_page_config(layout="wide")
st.markdown("""
    <div style="text-align:center">
        <h1>AI Resume Creator</h1>
    </div>
    """, unsafe_allow_html=True)


# UI with 4 columns
# col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

st.write("<h4>Upload the audio file:</h4>", unsafe_allow_html=True)
audio_file = st.file_uploader("Upload Audio", type=['mp3', 'mp4'])

# Button - Translate
_, button_cell, _ = st.columns(3)
with button_cell:
    button_translate = st.button('Translate', use_container_width=True)

if audio_file and button_translate:
    st.write("<h4>The translated text will appear here shortly ...</h4>", unsafe_allow_html=True)

    translator = Translator()
    translated_text = translator.translate(audio_file)
    advisor = FinancialAdvisor()
    result = advisor.describe(translated_text)

    # Display translated text
    container1 = st.container(border=True)
    container1.markdown(f"""
    <span style="font-size: 20px;"> 
    {result}
    </span>
    """, unsafe_allow_html=True)

else:
    st.write("<h4>Upload the audio file to translate.</h4>", unsafe_allow_html=True)
