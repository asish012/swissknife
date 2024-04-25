import streamlit as st
from app import menu
from Linguist import LangAgent
from utility.document_reader import read_document


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

with cols[0]:
    st.write("<h4>Upload the document:</h4>", unsafe_allow_html=True)
    doc = st.file_uploader("Upload document", type=['pdf'])

with cols[2]:
    if doc:
        st.write("<h4>Interact with your document:</h4>", unsafe_allow_html=True)
        # get prepared: as soon as the user upload a doc, be prepared to answer any questions
        language_agent = LangAgent()
        # extract text
        raw_content = read_document(doc)
        # translate (if needed)
        translated_text = language_agent.translate_text(raw_content)

        if translated_text:
            # Query text-box
            query = st.text_input("Enter your query")
            # Button: Query
            button_translate = st.button('Enter', use_container_width=True)

            if button_translate:
                answer = language_agent.answer(query, translated_text)

                container1 = st.container(border=True)
                container1.markdown(f"""
                <span style="font-size: 20px;"> 
                {answer}
                </span>
                """, unsafe_allow_html=True)

