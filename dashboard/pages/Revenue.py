import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_csv

st.title("Revenue Analytics")

category = load_csv(
    "revenue_by_category.csv"
)

state = load_csv(
    "revenue_by_state.csv"
)

st.subheader("Revenue by Category")

fig1 = px.bar(
    category,
    x="category",
    y="revenue",
    color="revenue",
    title="Revenue by Product Category"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.divider()

st.subheader("Top Revenue States")

top_states = state.nlargest(
    10,
    "revenue"
)

fig2 = px.bar(
    top_states,
    x="state",
    y="revenue",
    color="revenue",
    title="Top 10 States by Revenue"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
