#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def display_info(self):
        print(f"Plant name: {self.name}")
        print(f"Height: {self.height_cm}cm")
        print(f"Age: {self.age_days} days old")
        print("-" * 20)


def main() -> None:
    """The 'Factory' that creates and organizes plants efficiently"""
    plant_data = [
        ("Marigold", 18, 12),
        ("Rose", 35, 45),
        ("Daisy", 22, 28),
        ("Lavender", 40, 60),
        ("Orchid", 15, 5)
    ]

    garden_plants = []

    print("=== Plant Factory Output ===")

    """
    This loop acts as the 'Plant Factory'
    1. It loops through raw data (plant_data)
    2. It unpacks the data into variables
    3. It turns that raw data into a real 'Plant' Object
    4. It saves the object into our 'garden_plants' storage list
    """
    for i in range(len(plant_data)):  # step 1
        name, height, age = plant_data[i]  # step 2
        new_plant = Plant(name, height, age)  # step 3
        garden_plants.append(new_plant)  # step 4
        print(f"Created: {name} ({height}cm, {age} days)")  # prints the output

    print(f"\nTotal plants created: {len(garden_plants)}\n")

    print("=== Plant Info Board ===")
    for plant in garden_plants:
        plant.display_info()

    print("=== End of List ===")


if __name__ == "__main__":
    main()
