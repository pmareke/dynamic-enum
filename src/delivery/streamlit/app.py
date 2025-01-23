import streamlit as st

from src.delivery.streamlit.components.form import Form
from src.delivery.streamlit.components.header import Header
from src.domain.component import Component
from src.domain.models.form_model import FormModel


class App(Component):
    def render(self) -> None:
        header = Header("Form example for Dynamic Enums")
        header.render()

        form = Form(self._callback, FormModel)
        form.render()

    def _callback(self, data: dict) -> None:
        st.json(data)
