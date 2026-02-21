# app.py
import streamlit as st
from dotenv import load_dotenv
from modules.document_processor import process_documents
from modules.vector_index import create_vector_index
from modules.query_engine import get_query_engine, ask_query

load_dotenv()  # loads OPENAI_API_KEY from .env

st.set_page_config(page_title="Annual Report Analyzer", layout="wide")
st.title("Annual Report Analyzer")

uploaded_files = st.file_uploader(
    "Upload PDF Annual Reports", type=["pdf"], accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing documents..."):
        documents = process_documents(uploaded_files)
        index = create_vector_index(documents)
        engine = get_query_engine(index)
    st.success(f"âœ… Indexed {len(documents)} document(s). Ask your questions below.")

    query = st.text_input("Ask a question about the reports:")
    if query:
        with st.spinner("Querying..."):
            answer = ask_query(engine, query)
        st.markdown(f"**Answer:** {answer}")
