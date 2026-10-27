
import streamlit as st
from estimator import estimate_price

st.set_page_config(
    page_title="House Price Estimator",
    page_icon="🏠"
)

st.title("House Price Estimator")
st.write("Mini project for the DevOps practical")

area = st.number_input(
    "Area (sq. ft.)",
    min_value=100,
    value=1000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=2
)

price = estimate_price(area, bedrooms)

st.metric("Estimated price", f"₹{price:,.0f}")
st.caption("Demo estimate using a formula, not a trained ML model.")
