

import streamlit as st
import time

placeholder = st.empty()
for i in range(5):
    placeholder.write(f"Loading data... {i*20}% complete")
    time.sleep(1)
placeholder.write("Data loading complete. Displaying business insights.")


business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(2)
