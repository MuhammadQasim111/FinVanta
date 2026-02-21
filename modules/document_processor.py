# modules/document_processor.py
import pandas as pd
from PyPDF2 import PdfReader
from llama_index import Document

def process_documents(files):
    docs = []
    for file in files:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        docs.append(Document(text=text))
    return docs
