import streamlit as st
from app import menu
from agents.Linguist import LangAgent
from agents.document_processor import read_document


# Application Init
st.set_page_config(layout="wide")

# Draw main menu
menu()

st.markdown("""
    <div style="text-align:center">
        <h1>Interact with your document</h1>
    </div>
    """, unsafe_allow_html=True)


# UI with 2 columns
cols = st.columns([2, 0.1, 3])

# Initialize session state
if 'swissknife_vars' not in st.session_state:
    st.session_state.swissknife_vars = {
        'doc': '',
        'translated_formated_content': '',
        'query': ''
    }

language_agent = LangAgent()
button_query = None
current_query = ''

with cols[0]:
    st.write("<h4>Upload the document:</h4>", unsafe_allow_html=True)
    doc = st.file_uploader("Upload document", type=['pdf'])

    if doc and doc.name != st.session_state.swissknife_vars['doc']:
        # New file uploaded
        st.session_state.swissknife_vars['doc'] = doc.name
        # Get Prepared: as soon as the user upload a doc, be prepared to answer any questions
        # Extract text
        raw_content = read_document(doc)
        # Translate (if needed)
        st.session_state.swissknife_vars['translated_formated_content'] = language_agent.translate_text(raw_content)

    if doc and st.session_state.swissknife_vars['doc']:
        st.write("<h4>Interact with your document.</h4>", unsafe_allow_html=True)
        # Query text-box
        current_query = st.text_input("Enter your query")

        # Button: Query
        button_query = st.button('Enter', use_container_width=True)

with cols[2]:
    container1 = st.container(border=True)
    container2 = st.container(border=True)

    if st.session_state.swissknife_vars['translated_formated_content']:
        container2.markdown(st.session_state.swissknife_vars['translated_formated_content'], unsafe_allow_html=True)

    if button_query or current_query != st.session_state.swissknife_vars['query']:
        st.session_state.swissknife_vars['query'] = current_query
        answer = language_agent.answer(current_query, st.session_state.swissknife_vars['translated_formated_content'])

        container1.markdown(f"""
        <span style="font-size: 20px;"> 
        {answer}
        </span>
        """, unsafe_allow_html=True)

