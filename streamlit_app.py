import streamlit as st

st.title('🎈 App Name')

def page1():
    st.write("Page 1")
def page2():
    st.write("Page 2")
def resource1():
    st.write("Resource 1")
def resource2():
    st.write("Resource 2")
    
pages = {
    "Main" : [
        st.Page("home.py", title="Home", icon=":material/home"),
        st.Page("about.py", title="About")
    ],
    "Resources" : [
        st.Page("resources/page1.py", title="Resource 1"),
        st.Page("resources/page2.py", title="Resource 2")
    ]
}

pg = st.navigation(pages)
pg.run()
