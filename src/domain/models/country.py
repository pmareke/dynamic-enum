from enum import Enum

from src.domain.countries_rest_client import CountriesRestClient
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory


def _values(countries_client: CountriesRestClient) -> dict[str, str]:
    countries = countries_client.find_countries()
    names = {}
    for country in sorted(countries):
        names[country.upper()] = country
    return names


countries_client = HttpCountriesRestClientFactory.make()
Country = Enum("Country", _values(countries_client))  # type: ignore
