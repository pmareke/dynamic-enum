from pydantic import BaseModel, Field

from src.domain.models.country import Country


class FormModel(BaseModel):  # type: ignore
    name: str = Field("NAME")
    age: int = Field(18)
    address: str = Field("ADDRESS")
    country: Country
