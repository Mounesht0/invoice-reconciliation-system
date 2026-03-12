# Automated Invoice Reconciliation System

A Python-based financial reconciliation tool that automatically matches invoices with payments and detects discrepancies.

## Features

- Detects duplicate payments
- Identifies mismatched payment amounts
- Flags unpaid invoices
- Generates reconciliation reports
- Interactive financial dashboard using Streamlit

## Tech Stack

- Python
- Pandas
- Streamlit

## Project Structure

fintech-reconciliation-system

data/
- invoices.csv
- payments.csv

src/
- reconcile.py
- dashboard.py

results/
- reconciliation_results.csv

## How to Run

Install dependencies:

pip install -r requirements.txt

Run reconciliation engine:

python src/reconcile.py

Launch dashboard:

python -m streamlit run src/dashboard.py

## Dashboard

Displays reconciliation results and financial analytics.

## Author

Mounesh