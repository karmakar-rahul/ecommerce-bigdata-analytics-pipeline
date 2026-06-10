from streamlit_autorefresh import st_autorefresh
import streamlit as st
from datetime import datetime

st.write("Last refresh:", datetime.now())
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    layout="wide"
)
st_autorefresh(
    interval=10000,
    key="dashboard_refresh"
)
st.title("E-Commerce Big Data Analytics Dashboard")

st.markdown("""
This dashboard was built using:

- Python
- Hadoop HDFS
- Apache Spark
- Hive
- Streamlit
""")
