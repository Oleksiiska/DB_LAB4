import csv
from dataclasses import asdict
from datetime import datetime, time

from sqlalchemy import String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from domain import WeatherRecord, WindDirection

URL = "postgresql+psycopg://weather:weather@localhost:5432/weather"


def connect():
    return Session(create_engine(URL))


class Base(DeclarativeBase):
    pass


class Weather(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(primary_key=True)
    country: Mapped[str | None] = mapped_column(String(100))
    location_name: Mapped[str | None] = mapped_column(String(100))
    last_updated: Mapped[datetime | None]
    latitude: Mapped[float | None]
    longitude: Mapped[float | None]
    wind_kph: Mapped[float | None]
    wind_degree: Mapped[int | None]
    wind_direction: Mapped[WindDirection | None]
    sunrise: Mapped[time | None]
    precip_mm: Mapped[float | None]
    precip_in: Mapped[float | None]
    humidity: Mapped[int | None]
    cloud: Mapped[int | None]


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            yield WeatherRecord(
                country=row["country"],
                location_name=row["location_name"],
                last_updated=datetime.strptime(row["last_updated"], "%Y-%m-%d %H:%M"),
                latitude=float(row["latitude"]),
                longitude=float(row["longitude"]),
                wind_kph=float(row["wind_kph"]),
                wind_degree=int(row["wind_degree"]),
                wind_direction=WindDirection(row["wind_direction"]),
                sunrise=datetime.strptime(row["sunrise"], "%I:%M %p").time(),
                precip_mm=float(row["precip_mm"]),
                precip_in=float(row["precip_in"]),
                humidity=int(row["humidity"]),
                cloud=int(row["cloud"]),
            )


def save(session, records):
    session.add_all(Weather(**asdict(r)) for r in records)


def count(session):
    return session.scalar(select(func.count(Weather.id)))


def stats(session):
    return {
        "rows": count(session),
        "countries": session.scalar(select(func.count(func.distinct(Weather.country)))),
    }
