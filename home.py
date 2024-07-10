import streamlit as st

st.info("Demo page for the `st.navigation()` method.")

st.write("""
  `st.navigation()` creates a navigation menu in the sidebar to provide access to available pages of this multi-page app.

  In a nutshell, you'll need to:
  - Create an **entrypoint** file (`streamlit_app.py` in this demo) that acts as a router to direct users to specific pages of interest
  - Pages as defined by `st.Pages()` could either be callable functions or Python `.py` files.

""")
