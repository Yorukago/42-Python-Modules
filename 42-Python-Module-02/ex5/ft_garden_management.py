class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, name) -> None:
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(name)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water!")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name, water, sun) -> None:
        try:
            if water > 10:
                raise GardenError(
                    f"Water level {water} is too high (max 10)"
                )
            if sun < 2:
                raise GardenError(
                    f"Sunlight hours {sun} is too low (min 2)"
                )
            print(f"{name}: healthy (water: {water}, sun: {sun})")
        except GardenError as e:
            print(f"Error checking {name}: {e}")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    gm = GardenManager()

    print("Adding plants to garden...")
    gm.add_plant("tomato")
    gm.add_plant("lettuce")
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_plants()

    print("\nChecking plant health...")
    gm.check_health("tomato", 5, 8)
    gm.check_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nSystem recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
