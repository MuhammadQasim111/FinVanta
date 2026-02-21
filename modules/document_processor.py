# modules/document_processor.py
from PyPDF2 import PdfReader
from llama_index.core import Document  # âœ… correct for llama-index v0.10+


def process_documents(files):
    docs = []
    for file in files:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        if text.strip():
            docs.append(Document(text=text))
    return docs
