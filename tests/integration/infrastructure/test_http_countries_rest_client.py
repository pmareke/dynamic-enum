from expects import be_empty, expect

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory


class TestHttpCountriesClientIntegration:
    def test_find_countries(self) -> None:
        client = HttpCountriesRestClientFactory.make()

        countries = client.find_countries()

        expect(countries).not_to(be_empty)
