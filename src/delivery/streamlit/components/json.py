import streamlit as st

from src.domain.component import Component


class JSON(Component):
    def __init__(self, data: dict) -> None:
        self.data = data

    def render(self) -> None:
        st.json(self.data)
