from doublex import Spy
from doublex_expects import have_been_called_with
from expects import equal, expect
from pydantic import BaseModel, Field
from streamlit.testing.v1 import AppTest


class TestForm:
    NAME = "ANY_NAME"
    AGE = 18

    def test_submit_form(self) -> None:
        callback = Spy()

        class MyModel(BaseModel):  # type: ignore
            name: str = Field(self.NAME)
            age: int = Field(self.AGE)

        def create_app(callback, model) -> None:  # type: ignore
            from src.delivery.streamlit.components.form import Form

            internal_app = Form(callback.call, model)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(callback, MyModel))

        at = app.run()

        expect(at.text_input[0].value).to(equal(self.NAME))
        expect(at.number_input[0].value).to(equal(self.AGE))

        at.button[0].click()

        app.run()

        payload = {"name": self.NAME, "age": self.AGE}
        expect(callback.call).to(have_been_called_with(payload))
