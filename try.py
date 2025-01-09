import streamlit as st
import pandas as pd
import plotly.express as px

# Dummy data
data = {
    'Date': pd.date_range(start="2025-01-01", periods=30, freq='D'),
    'Category': ['Groceries', 'Rent', 'Entertainment', 'Utilities', 'Salary'] * 6,
    'Amount': [50, 500, 100, 200, 1500] * 6
}
df = pd.DataFrame(data)

# Sidebar
st.sidebar.title("Finance Tracker")
page = st.sidebar.selectbox("Navigate", ["Overview", "Income & Expenses", "Savings Goals"])

# Overview Page
if page == "Overview":
    st.title("Finance Tracker Overview")
    total_income = df[df['Category'] == 'Salary']['Amount'].sum()
    total_expense = df[df['Category'] != 'Salary']['Amount'].sum()
    st.metric("Total Income", f"${total_income}")
    st.metric("Total Expenses", f"${total_expense}")
    st.metric("Net Savings", f"${total_income - total_expense}")

    # Line Graph
    fig = px.line(df, x="Date", y="Amount", color="Category", title="Daily Transactions")
    st.plotly_chart(fig)

# Income & Expenses Page
elif page == "Income & Expenses":
    st.title("Income & Expenses Breakdown")
    category = st.selectbox("Select Category", df['Category'].unique())
    filtered_data = df[df['Category'] == category]
    st.write(f"Transactions for {category}")
    st.dataframe(filtered_data)

    # Pie Chart
    expense_data = df[df['Category'] != 'Salary']
    fig = px.pie(expense_data, values="Amount", names="Category", title="Expense Categories")
    st.plotly_chart(fig)

# Savings Goals Page
elif page == "Savings Goals":
    st.title("Savings Goals")
    goal = st.slider("Set Your Savings Goal", 0, 5000, 1000)
    current_savings = total_income - total_expense
    st.progress(min(current_savings / goal, 1.0))
    st.write(f"Your current savings: ${current_savings} / ${goal}")
