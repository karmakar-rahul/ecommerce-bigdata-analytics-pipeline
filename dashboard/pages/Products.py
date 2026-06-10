
import streamlit as st
import plotly.express as px

from utils import load_csv
from streamlit_autorefresh import st_autorefresh
st.title("Product Analytics")
st_autorefresh(
    interval=10000,
    key="refresh"
)
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
