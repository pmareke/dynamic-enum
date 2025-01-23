from collections.abc import Callable

import streamlit_pydantic as sp
from pydantic import BaseModel

from src.domain.component import Component


class Form(Component):
    def __init__(self, callback: Callable, model: type[BaseModel]) -> None:
        self.callback = callback
        self.model = model

    def render(self) -> None:
        data = sp.pydantic_form(key=__name__, model=self.model)
        if data:
            self.callback(data.model_dump())
