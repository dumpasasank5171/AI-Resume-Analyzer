from pypdf import PdfReader

def extract_text(uploaded_file):
    try:
        reader=PdfReader(uploaded_file)
        text=""
        for page in reader.pages:
            page_text=page.extract_text()
            if page_text:
                text+=page_text+"\n"
        return text.strip()
    except Exception:
        return ""
