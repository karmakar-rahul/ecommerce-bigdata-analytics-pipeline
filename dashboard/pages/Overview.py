import streamlit as st
import plotly.express as px

from utils import load_csv

st.title("Executive Overview")

payment = load_csv(
    "payment_summary.csv"
)

total_orders = int(
    payment["total_transactions"].sum()
)

success_orders = int(
    payment.loc[
        payment["payment_status"] == "Success",
        "total_transactions"
    ].iloc[0]
)

refund_orders = int(
    payment.loc[
        payment["payment_status"] == "Refunded",
        "total_transactions"
    ].iloc[0]
)

refund_rate = (
    refund_orders / total_orders
) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Orders",
    f"{total_orders:,}"
)

col2.metric(
    "Successful Payments",
    f"{success_orders:,}"
)

col3.metric(
    "Refunded Orders",
    f"{refund_orders:,}"
)

col4.metric(
    "Refund Rate",
    f"{refund_rate:.2f}%"
)

st.divider()

st.subheader("Payment Status Distribution")

fig = px.pie(
    payment,
    names="payment_status",
    values="total_transactions",
    hole=0.45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Dataset Statistics")

c1, c2, c3 = st.columns(3)

c1.success("100,000 Customers")

c2.success("10,000 Products")

c3.success("1,000,000 Orders")
