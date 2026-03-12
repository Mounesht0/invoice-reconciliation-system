import os
import streamlit as st
import pandas as pd

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "results", "reconciliation_results.csv")

df = pd.read_csv(file_path)

st.title("Invoice Reconciliation Dashboard")

st.dataframe(df)

st.bar_chart(df["invoice_amount"])