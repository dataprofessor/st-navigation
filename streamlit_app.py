import streamlit as st

st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="🧊")

st.title('🧊 Ex-stream-ly Cool App')

def page3():
    st.write("This is **Demo 3**.")
    
pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About", icon=":material/local_library:")
    ],
    "Resources" : [
        st.Page("resources/page1.py", title="Demo 1", icon=":material/nutrition:"),
        st.Page("resources/page2.py", title="Demo 2", icon=":material/handyman:"),
        st.Page(page3, title="Demo 3", icon=":material/architecture:")
    ]
}

pg = st.navigation(pages)
pg.run()
