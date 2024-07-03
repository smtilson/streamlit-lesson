import streamlit as st

class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=""
        )

    # app here is for appending pages
    def app_page(self, title, function) -> None:
        self.pages.append({"title":title, "function":function})

    # this is for executing the views I guess?
    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio("Menu",self.pages, format_func=lambda page: page["title"])
        page['function']()

    
