import pandas as pd

# Load data
invoices = pd.read_csv("../data/invoices.csv")
payments = pd.read_csv("../data/payments.csv")

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

print(df)

df.to_csv("../results/reconciliation_results.csv", index=False)