from expects import equal, expect
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
        expect(at.selectbox[0].value).to(equal("Spain"))
