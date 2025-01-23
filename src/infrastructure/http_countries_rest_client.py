import requests

from src.domain.countries_rest_client import CountriesRestClient


class HttpCountriesRestClient(CountriesRestClient):
    API_URL = "https://restcountries.com/v3.1/all"

    def find_countries(self) -> list[str]:
        response = requests.get(f"{self.API_URL}?fields=name")
        json_response = response.json()
        countries = []
        for country in json_response:
            countries.append(country["name"]["common"])
        return countries


class HttpCountriesRestClientFactory:
    @staticmethod
    def make() -> HttpCountriesRestClient:
        return HttpCountriesRestClient()
