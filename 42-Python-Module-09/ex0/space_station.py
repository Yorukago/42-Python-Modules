from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """
    this is our blueprints for a space station
    pydantic will automatically yell at us if we try to build a station
    that doesn't fit these rules!
    """
    # string, must be 3 to 10 characters long
    station_id: str = Field(min_length=3, max_length=10)

    # string, 1 to 50 characters
    name: str = Field(min_length=1, max_length=50)

    # int, 1 to 20 people
    crew_size: int = Field(ge=1, le=20)

    # float from 0.0 to 100.0
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    # pydantic is smart enough to turn a string like
    # '2026-01-01' into a real date object so we can use datetime
    last_maintenance: datetime

    # bool starts as true if we don't say otherwise
    is_operational: bool = True

    # this one is allowed to be empty, but max 200 characters if it's there
    notes: Optional[str] = Field(None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-24T12:00:00",
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Last Maintenance: {valid_station.last_maintenance}")

        status = "Operational" if valid_station.is_operational else "Down"
        print(f"Status: {status}")

    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("=" * 40)

    # what is crew is over 20?
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="BAD-01",
            name="Crowded Station",
            crew_size=100,  # This is way too many people!
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )
        # I hate this, this is to stop flakie to complain
        print(f"Crew: {invalid_station.crew_size} people")
    except ValidationError as e:
        # pydantic gives us a list of errors
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
