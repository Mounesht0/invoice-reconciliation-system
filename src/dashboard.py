import os
import streamlit as st
import pandas as pd

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "results", "reconciliation_results.csv")

df = pd.read_csv(file_path)

matched = (df["status"] == "MATCHED").sum()
mismatch = (df["status"] == "MISMATCH").sum()
duplicate = (df["status"] == "DUPLICATE PAYMENT").sum()
unpaid = (df["status"] == "UNPAID").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Matched", matched)
col2.metric("Mismatch", mismatch)
col3.metric("Duplicate", duplicate)
col4.metric("Unpaid", unpaid)

st.title("Invoice Reconciliation Dashboard")

st.dataframe(df)

st.bar_chart(df["invoice_amount"])

st.subheader("Invoice Status Distribution")

status_counts = df["status"].value_counts()

st.bar_chart(status_counts)