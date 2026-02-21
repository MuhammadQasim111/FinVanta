import streamlit as st
from modules.document_processor import process_documents
from modules.vector_index import create_vector_index
from modules.query_engine import get_query_engine, ask_query
from modules.insights_parser import parse_insights
from modules.visualization import plot_financial_trends
import os

st.set_page_config(page_title="FinVanta", layout="wide", page_icon="💰")

st.title("💰 FinVanta – Financial Insights Platform")
st.sidebar.header("Upload Financial Documents")

# Upload documents
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF/Excel/CSV files",
    type=["pdf", "csv", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Processing documents..."):
        docs = process_documents(uploaded_files)
        st.session_state.vector_index = create_vector_index(docs)
    st.success("Documents processed successfully!")

query = st.text_input("Ask FinVanta anything about your financial documents:")

if query and 'vector_index' in st.session_state:
    engine = get_query_engine(st.session_state.vector_index)
    response = ask_query(engine, query)
    insights = parse_insights(response)
    
    st.subheader("📊 Generated Insights")
    for section, content in insights.items():
        st.markdown(f"### {section}")
        st.write(content)

    st.subheader("📈 Financial Trends")
    plot_financial_trends(docs)
