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
        st.Page("page1", title="Page 1"),
        st.Page("page2", title="Page 2")
    ],
    "Resources" : [
        st.Page("resource1", title="Resource 1"),
        st.Page("resource2", title="Resource 2")
    ]
}

pg = st.navigation(pages)
pg.run()
