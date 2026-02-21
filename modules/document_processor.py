from PyPDF2 import PdfReader
import pandas as pd
from llama_index import Document

def process_documents(files):
    docs = []
    for file in files:
        if file.type == "application/pdf":
            reader = PdfReader(file)
            text = "".join([page.extract_text() for page in reader.pages])
            docs.append(Document(text=text))
        elif file.type in ["text/csv", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
            df = pd.read_excel(file) if file.type.endswith("sheetml") else pd.read_csv(file)
            docs.append(Document(text=df.to_csv(index=False)))
    return docs
