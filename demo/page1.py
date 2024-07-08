import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Demo 1")

st.write("Display an area chart using the `st.area_chart()` method.")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
