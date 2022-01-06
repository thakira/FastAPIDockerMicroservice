from typing import List
from pydantic import BaseModel


class WeatherModel(BaseModel):
    name: str
    description: str
    temp: float



