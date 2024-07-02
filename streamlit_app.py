import streamlit as st

st.title('🎈 App Name')

def page3():
    st.write("This is **Resources Page 3**.")
    
pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home:"),
        st.Page("about.py", title="About", icon=":material/local_library:")
    ],
    "Resources" : [
        st.Page("resources/page1.py", title="Resource 1"),
        st.Page("resources/page2.py", title="Resource 2"),
        st.Page(page3, title="Resource 3")
    ]
}

pg = st.navigation(pages)
pg.run()
