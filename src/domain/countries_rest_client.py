from abc import ABC, abstractmethod


class CountriesRestClient(ABC):
    @abstractmethod
    def find_countries(self) -> list[str]:
        raise NotImplementedError
