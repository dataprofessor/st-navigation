import streamlit as st

st.info("Demo page for the `st.navigation()` method.")

st.write("""
  `st.navigation()` creates a navigation menu in the sidebar to provide access to available pages of a multi-page app.

  In a nutshell, you'll need to:
  - Create an **entrypoint** file (`streamlit_app.py` in this demo) that acts as a router to direct users to specific pages of interest.
  - This **entrypoint** file makes use of `st.navigation()` to define the hierarchy of **page elements** in the multi-page app.
  - Each **page elements** is defined using `st.Page()` that could either be callable functions or Python `.py` files.
""")

st.page_link("https://docs.streamlit.io/develop/api-reference/navigation/st.navigation", label="st.navigation", icon="📖")
