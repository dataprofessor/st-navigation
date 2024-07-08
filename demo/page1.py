import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Demo 1")

st.write("Draw a chart using the PyDeck library via the `st.pydeck_chart()` method.")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
