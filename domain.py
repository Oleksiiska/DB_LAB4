from dataclasses import dataclass
from datetime import datetime, time
from enum import Enum

DIRECTIONS = "N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW".split()
WindDirection = Enum("WindDirection", {d: d for d in DIRECTIONS}, type=str)


@dataclass
class WeatherRecord:
    country: str
    location_name: str
    last_updated: datetime
    latitude: float
    longitude: float
    wind_kph: float
    wind_degree: int
    wind_direction: WindDirection
    sunrise: time
    # осади (варіант 3)
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
