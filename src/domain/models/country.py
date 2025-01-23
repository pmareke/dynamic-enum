from enum import Enum

from src.domain.countries_rest_client import CountriesRestClient
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory


def _countries(countries_rest_client: CountriesRestClient) -> dict:
    countries = countries_rest_client.find_countries()
    return {country.upper(): country for country in sorted(countries)}


countries_rest_client = HttpCountriesRestClientFactory.make()
Country = Enum("Country", _countries(countries_rest_client))  # type: ignore
