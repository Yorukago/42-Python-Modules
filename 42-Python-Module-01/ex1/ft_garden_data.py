#!/usr/bin/env python3

class Plant:
    """
    Class to make a plant with a name, a height and age (in days)
    init, initializer or better known as a Constructor, takes temporary info
    like: name, height and age...
    And then saves its on a "permament memory" using 'self.'
    """
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    """ Helper class to display info about the plant """
    def display_info(self) -> None:
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")
        print("-" * 20)


def main() -> None:
    """ The main uses the class Plant and we define the plants """
    # Creates a list of objects Plants
    plant1 = Plant("Spider Lily", 75, 30)
    plant2 = Plant("Tulip", 25, 2)
    plant3 = Plant("Sunflower", 300, 95)

    garden_plants = [plant1, plant2, plant3]

    """ We print the things afterwards with the Helper... """
    print("~ Community Garden Plant Information Board ~\n")
    for plant in garden_plants:
        plant.display_info()
    print("~ End of List ~\n")


if __name__ == "__main__":
    main()
