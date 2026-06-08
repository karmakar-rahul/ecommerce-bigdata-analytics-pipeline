import streamlit as st
import plotly.express as px

from utils import load_csv

st.title("Product Analytics")

products = load_csv(
    "top_products.csv"
)

products = products.sort_values(
    "orders",
    ascending=False
)

st.subheader("Top Products")

fig = px.bar(
    products.head(15),
    x="orders",
    y="product_name",
    orientation="h",
    color="orders"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("Product Ranking")

st.dataframe(
    products,
    use_container_width=True
)
