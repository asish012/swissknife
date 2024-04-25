import fitz


def read_document(uploaded_file):
    content = uploaded_file.read()
    text = ""
    with fitz.open(stream=content) as doc:
        for page in doc:
            text += page.get_text()
    return text
