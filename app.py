import streamlit as st
from parser import extract_transactions
from analyzer import analyze
from charts import plot_category
from agent import get_budget_plan

st.title("💰 AI Smart Budget Agent")

uploaded_file = st.file_uploader("Upload PhonePe PDF", type=["pdf"])

if uploaded_file:
    # ✅ Step 1: Extract data
    df = extract_transactions(uploaded_file)

    # 🔍 DEBUG
    st.write("DEBUG RAW DATA:", df.head(20))

    # ✅ Step 2: Analyze
    total_spent, total_received, summary, full_df = analyze(df)

    # 🔍 DEBUG
    st.write("DEBUG SUMMARY:", summary)

    # ✅ Step 3: Overview
    st.subheader("📊 Overview")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Spent", f"₹{total_spent:,.0f}")
    col2.metric("Total Received", f"₹{total_received:,.0f}")
    col3.metric("Transactions", len(full_df))

    # ✅ Step 4: Category Chart (Streamlit built-in)
    st.subheader("📂 Category-wise Spending")
    st.bar_chart(summary)

    # ✅ Step 5: Matplotlib Chart
    st.subheader("📈 Chart")
    fig = plot_category(summary)

    if fig:
        st.pyplot(fig)
    else:
        st.warning("⚠️ No expense data found in PDF")

    # ✅ Step 6: AI Budget Plan
    if st.button("Generate AI Budget Plan"):
        with st.spinner("AI analyzing..."):
            advice = get_budget_plan(summary.to_string())
            st.subheader("🤖 AI Suggestions")
            st.write(advice)