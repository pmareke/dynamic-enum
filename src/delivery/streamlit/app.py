from src.delivery.streamlit.components.form import Form
from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.json import JSON
from src.domain.component import Component
from src.domain.models.form_model import FormModel


class App(Component):
    def render(self) -> None:
        header = Header("Form example for Dynamic Enums")
        header.render()

        form = Form(self._callback, FormModel)
        form.render()

    def _callback(self, data: dict) -> None:
        json = JSON(data)
        json.render()
