import os
import streamlit as st
import pandas as pd

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "results", "reconciliation_results.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame()

if df.empty:
    st.info("Upload invoice and payment files to start reconciliation.")

st.title("Invoice Reconciliation Dashboard")

st.subheader("Upload Invoice and Payment Files")

invoice_file = st.file_uploader("Upload Invoices CSV", type=["csv"])
payment_file = st.file_uploader("Upload Payments CSV", type=["csv"])

#If files are uploaded → run reconciliation
if invoice_file and payment_file:

    invoices = pd.read_csv(invoice_file)
    payments = pd.read_csv(payment_file)

    results = []

    for index, inv in invoices.iterrows():

        matched_payment = payments[payments["reference"] == inv["invoice_id"]]

        if matched_payment.empty:
            status = "UNPAID"
            payment_amount = 0

        elif len(matched_payment) > 1:
            status = "DUPLICATE PAYMENT"
            payment_amount = matched_payment["amount"].sum()

        else:
            payment_amount = matched_payment.iloc[0]["amount"]

            if payment_amount == inv["amount"]:
                status = "MATCHED"
            else:
                status = "MISMATCH"

        results.append({
            "invoice_id": inv["invoice_id"],
            "invoice_amount": inv["amount"],
            "payment_amount": payment_amount,
            "status": status
        })

    df = pd.DataFrame(results)

#Updated KPI Metrics
if not df.empty:

    matched = (df["status"] == "MATCHED").sum()
    mismatch = (df["status"] == "MISMATCH").sum()
    duplicate = (df["status"] == "DUPLICATE PAYMENT").sum()
    unpaid = (df["status"] == "UNPAID").sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Matched", matched)
    col2.metric("Mismatch", mismatch)
    col3.metric("Duplicate", duplicate)
    col4.metric("Unpaid", unpaid)

#Display results
if not df.empty:

    st.subheader("Reconciliation Results")
    st.dataframe(df)

    st.subheader("Invoice Amount Distribution")
    st.bar_chart(df["invoice_amount"])

    st.subheader("Invoice Status Distribution")
    status_counts = df["status"].value_counts()
    st.bar_chart(status_counts)