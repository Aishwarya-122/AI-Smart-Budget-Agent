import pandas as pd
from categories import categorize

def analyze(df):
    df["Category"] = df["Description"].apply(categorize)

    expenses = df[df["Amount"] < 0]
    income = df[df["Amount"] > 0]

    total_spent = abs(expenses["Amount"].sum())
    total_received = income["Amount"].sum()

    category_summary = abs(expenses.groupby("Category")["Amount"].sum())

    return total_spent, total_received, category_summary, df