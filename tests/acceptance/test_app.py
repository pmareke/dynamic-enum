import json

from expects import be_none, equal, expect
from streamlit.testing.v1 import AppTest


class TestApp:
    def test_app(self) -> None:
        app = AppTest.from_file("main.py")

        at = app.run()

        header = "Form example for Dynamic Enums"
        expect(at.header[0].value).to(equal(header))
        expect(at.text_input[0].value).to(equal("NAME"))
        expect(at.number_input[0].value).to(equal(18))
        expect(at.text_input[1].value).to(equal("ADDRESS"))
        expect(at.selectbox[0].value).not_to(be_none)

    def test_submit_the_form(self) -> None:
        app = AppTest.from_file("main.py")

        at = app.run()
        at.button[0].click()
        at = app.run()

        data = json.loads(at.json[0].value)
        expect(list(data.keys())).to(equal(["name", "age", "address", "country"]))
        expect(data["name"]).to(equal("NAME"))
        expect(data["age"]).to(equal(18))
        expect(data["address"]).to(equal("ADDRESS"))
        expect(data["country"]).not_to(be_none)
