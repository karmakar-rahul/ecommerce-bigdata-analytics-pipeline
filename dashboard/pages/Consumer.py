import streamlit as st
from streamlit_autorefresh import st_autorefresh
st.title("Customer Analytics")
st_autorefresh(
    interval=10000,
    key="refresh"
)
st.warning(
    "Customer segmentation KPIs will be enabled in the next analytics refresh."
)

st.markdown("""
### Current Customer Base

- Total Customers: 100,000
- Budget Segment: 60%
- Regular Segment: 30%
- Premium Segment: 10%

### Behaviour Model

**Budget Customers**
- Grocery
- Books
- Beauty

**Regular Customers**
- Fashion
- Home
- Sports

**Premium Customers**
- Electronics
- Fashion
""")

st.info(
    "Future versions will include revenue-by-segment and customer lifetime value analytics."
)
