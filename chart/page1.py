import streamlit as st
import pandas as pd
import numpy as np

st.subheader("st.area_chart")

st.write("Display an area chart using the `st.area_chart()` method.")

with st.echo():
  chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
  
  st.area_chart(chart_data)
