import io
from pypdf import PdfReader
import docx


def extract_text(uploaded_file):
    """Takes a Streamlit UploadedFile and returns plain text, regardless of format."""
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    elif name.endswith(".docx"):
        document = docx.Document(io.BytesIO(uploaded_file.read()))
        return "\n".join(p.text for p in document.paragraphs)

    elif name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    else:
        raise ValueError("Unsupported file type. Upload a PDF, DOCX, or TXT file.")