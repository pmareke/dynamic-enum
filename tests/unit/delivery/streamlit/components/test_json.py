import json

from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestJSON:
    def test_render(self) -> None:
        data = {"message": "Test message"}

        def create_app(data: dict) -> None:
            from src.delivery.streamlit.components.json import JSON

            internal_app = JSON(data)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(data,))

        at = app.run()

        expect(at.json[0].value).to(equal(json.dumps(data)))
