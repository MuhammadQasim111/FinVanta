import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_financial_trends(documents):
    # Dummy implementation: plot revenue trends if CSV/Excel
    for doc in documents:
        try:
            df = pd.read_csv(pd.compat.StringIO(doc.text))
            if 'Revenue' in df.columns:
                st.line_chart(df['Revenue'])
        except Exception:
            continue
