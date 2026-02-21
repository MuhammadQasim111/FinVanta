# app.py
import streamlit as st
from modules.document_processor import process_documents
from modules.vector_index import create_vector_index
from modules.query_engine import get_query_engine, ask_query
from modules.insights_parser import (
    parse_insights,
    FiscalYearHighlights,
    StrategyOutlookFutureDirection,
    RiskManagement,
    InnovationRnD,
)

st.title("Finvanta - AI Financial Insights")

if "index" not in st.session_state:
    st.session_state.index = None
if "processed" not in st.session_state:
    st.session_state.processed = False

uploaded_files = st.file_uploader("Upload PDF Annual Reports", accept_multiple_files=True)

if st.button("Process Documents") and uploaded_files:
    with st.spinner("Processing..."):
        documents = process_documents(uploaded_files)
        st.session_state.index = create_vector_index(documents)
        st.session_state.processed = True
    st.success("Documents processed!")

if st.session_state.processed:
    engine = get_query_engine(st.session_state.index)
    
    st.header("Analyze Insights")
    if st.button("Generate Fiscal Year Highlights"):
        fyh = parse_insights(engine, "Fiscal Year Highlights", FiscalYearHighlights)
        st.json(fyh.dict())

    if st.button("Generate Strategy & Outlook"):
        strategy = parse_insights(engine, "Strategy Outlook and Future Direction", StrategyOutlookFutureDirection)
        st.json(strategy.dict())

    if st.button("Generate Risk Management Insights"):
        risk = parse_insights(engine, "Risk Management", RiskManagement)
        st.json(risk.dict())

    if st.button("Generate Innovation & R&D Insights"):
        rnd = parse_insights(engine, "Innovation and R&D", InnovationRnD)
        st.json(rnd.dict())        st.write(content)

    st.subheader("📈 Financial Trends")
    plot_financial_trends(docs)
