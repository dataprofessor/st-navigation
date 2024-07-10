import streamlit as st

st.info("Demo page for the `st.navigation()` method.")

st.write("""
  `st.navigation()` creates a navigation menu in the sidebar to provide access to available pages of a multi-page app.

  Here's what is happening under the hood:

  1. Create an entrypoint file (`streamlit_app.py` in this example). This file will serve as a router, directing users to specific pages of interest.
  2. Use `st.navigation()` in the entrypoint file to define the page hierarchy for a multi-page app. This functionality was previously unavailable in multi-page apps.
  3. Define each page using `st.Page()`. Pages can be callable functions or Python `.py` files.
  4. Streamlit runs the entrypoint file on every app rerun, applying the `.run()` method to the page object returned by `st.navigation()`.

""")

st.page_link("https://docs.streamlit.io/develop/api-reference/navigation/st.navigation", label="Streamlit Docs on st.navigation", icon="📖")
