import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Demo 1")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
