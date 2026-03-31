from enum import Enum
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """The Hierarchy: From the greenest Cadet to the legendary Commander!!!"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    The Mission Model: This 'wraps' the CrewMember model
    Pydantic will validate every single person in the 'crew' list
    before it even checks the mission rules
    """

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)

    # The 'crew' field is a list of our previous model
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        """The Safety Protocol: Ensuring the mission isn't a suicide run."""

        # 1. Mission ID check
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # 2. Leadership check (Need a Captain or Commander)
        leaders = [c for c in self.crew if c.rank in
                   [Rank.CAPTAIN, Rank.COMMANDER]]
        if not leaders:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # 3. Status check: No slackers allowed
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        # 4. Experience check for deep space (Long missions)
        if self.duration_days > 365:
            # We filter for 'Vets' with 5+ years
            exp_crew = [c for c in self.crew if c.years_experience >= 5]
            # If less than half the crew are vets, it's too dangerous
            if len(exp_crew) < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    # Valid
    try:
        # We create the crew members first
        crew_list = [
            CrewMember(
                member_id="CM01", name="Sarah Connor",
                rank=Rank.COMMANDER, age=45,
                specialization="Mission Command", years_experience=20
            ),
            CrewMember(
                member_id="CM02", name="John Smith",
                rank=Rank.LIEUTENANT, age=30,
                specialization="Navigation", years_experience=8
            ),
            CrewMember(
                member_id="CM03", name="Alice Johnson",
                rank=Rank.OFFICER, age=25,
                specialization="Engineering", years_experience=3
            )
        ]

        # We take them to a mission or smth
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-12-01T08:00:00",
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Unexpected Error: {e.errors()[0]['msg']}")

    print("=" * 41)

    # The 'No Captain' Failure
    print("Expected validation error:")
    try:
        # This crew only has Cadets
        fail_crew = [
            CrewMember(
                member_id="BAD1", name="Noob 1",
                rank=Rank.CADET, age=19,
                specialization="Cleaning", years_experience=0
            )
        ]
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Doomed Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=fail_crew,
            budget_millions=5.0
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()


"""
i mean sure u have some questions and wth but here

pydantic works recursively. When i initialize SpaceMission, pydantic
first goes into the crew list and validates every CrewMember object
against its own rules (age, rank, etc.).. only if every crew member is
valid does it move on to check the SpaceMission's own model_validator

what if it goes wrong???? the entire SpaceMission fails to initialize.
Pydantic will raise a ValidationError that actually tells you exactly
which index in the list failed... cuz it does that
For example, it might say crew.0.age: Input should be
greater than or equal to 18
"""
