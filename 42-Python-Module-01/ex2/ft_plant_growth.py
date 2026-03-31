#!/usr/bin/env python3

class Plant:
    """
    Same as before, we make the Plant class with the arguments needed
    but now we make it have actions
    """
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    """ This makes it grow 1cm each time its called """
    def grow(self) -> None:
        self.height_cm += 1

    """ And this makes it one day older each time its called """
    def age(self) -> None:
        self.age_days += 1

    """ This was needed for the subject but this sucks ass """
    def get_info(self) -> None:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"

    """ This is my way to do it lmao, ignore the get_info """
    def display_info(self) -> None:
        print(self.get_info())
        print("-" * 20)


def main() -> None:
    """ Creates the plants from before, and simulates growth over a week """
    garden_plants = [
        Plant("Spider Lily", 75, 30),
        Plant("Tulip", 25, 2),
        Plant("Sunflower", 300, 95)
    ]

    print("~ Community Garden Plant Information Board ~\n")
    for plant in garden_plants:
        plant.display_info()

    print("\nSimulating 7 days of growth...\n")

    """
    '_' is used because we dont really need the number, we just care
    about the repition...
    """
    for _ in range(7):
        for plant in garden_plants:
            plant.grow()
            plant.age()

    print("~ After 1 Week ~\n")
    for plant in garden_plants:
        plant.display_info()

    print("~ End of List ~\n")


if __name__ == "__main__":
    main()
