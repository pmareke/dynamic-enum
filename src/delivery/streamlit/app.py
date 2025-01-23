import streamlit as st

from src.domain.component import Component


class App(Component):
    def render(self) -> None:
        st.title("Hello World!")
