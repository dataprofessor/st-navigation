import streamlit as st

st.info("Demo page for the `st.navigation()` method.")

st.write("""
  `st.navigation()` creates a navigation menu in the sidebar to provide access to available pages of a multi-page app.

  In a nutshell, you'll need to:
  - Create an **entrypoint** file (`streamlit_app.py` in this demo) that acts as a router to direct users to specific pages of interest.
  - This **entrypoint** file makes use of `st.navigation()` to define the page hierarchy in a multi-page app (previously not possible in a multi-page app)
  - Each **page** is defined using `st.Page()` that could either be callable functions or Python `.py` files.
  - Streamlit executes the entrypoint file with every app rerun where the `.run()` method is applied on the page object returned by `st.navigation()`.
""")

st.page_link("https://docs.streamlit.io/develop/api-reference/navigation/st.navigation", label="Streamlit Docs on st.navigation", icon="📖")
