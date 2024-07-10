import streamlit as st

st.set_page_config(page_title="st.navigation Demo", page_icon="🗺️")

st.title('🗺️ st.navigation Demo App')

def page3():
    import pandas as pd
    import numpy as np

    st.subheader("st.vega_lite_chart")
    st.write("Display a chart using the Vega-Lite library via the `st.vega_lite_chart()` method.")

    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

    st.vega_lite_chart(
       chart_data,
       {
           "mark": {"type": "circle", "tooltip": True},
           "encoding": {
               "x": {"field": "a", "type": "quantitative"},
               "y": {"field": "b", "type": "quantitative"},
               "size": {"field": "c", "type": "quantitative"},
               "color": {"field": "c", "type": "quantitative"},
           },
       },
    )


pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About", icon=":material/local_library:")
    ],
    "Chart Demo" : [
        st.Page("demo/page1.py", title="Demo 1", icon=":material/nutrition:"),
        st.Page("demo/page2.py", title="Demo 2", icon=":material/handyman:"),
        st.Page(page3, title="st.vega_lite_chart", icon=":material/architecture:")
    ]
}

pg = st.navigation(pages)
pg.run()
