#!/usr/bin/env python3

class Plant:
    """
    Mostly the same from the other exercises, this is the inheritance part
    """
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, amount: int = 1) -> None:
        self.height_cm += amount
        print(f"{self.name} grew {amount}cm")

    def display_info(self) -> None:
        print(f"- {self.name}: {self.height_cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, h: int, a: int, color: str) -> None:
        super().__init__(name, h, a)
        self.color = color

    def bloom(self) -> str:
        return "(blooming)"

    def display_info(self) -> None:
        print(f"- {self.name}: {self.height_cm}cm, "
              f"{self.color} flowers {self.bloom()}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, h: int, a: int, c: str, pts: int) -> None:
        super().__init__(name, h, a, c)
        self.prize_points = pts

    def display_info(self) -> None:
        print(f"- {self.name}: {self.height_cm}cm, "
              f"{self.color} flowers {self.bloom()}, "
              f"Prize points: {self.prize_points}")


class GardenManager:
    """
    And this is the garden manager part that i hate
    """
    total_gardens = 0

    class GardenStats:
        """
        This helper class (required by the damn subject) is used to calculate
        the score of all the plants, and checks if the height is valid
        """
        def __init__(self, plants: list) -> None:
            self.plants = plants

        def calculate_plant_types(self):
            reg = sum(1 for p in self.plants if type(p) is Plant)
            flow = sum(1 for p in self.plants if type(p) is FloweringPlant)
            prz = sum(1 for p in self.plants if type(p) is PrizeFlower)
            return reg, flow, prz

        def get_total_score(self):
            score = sum(p.height_cm for p in self.plants)
            score += sum(getattr(p, 'prize_points', 0) for p in self.plants)
            return score

        def check_height_validation(self):
            return all(p.height_cm > 0 for p in self.plants)

    """
    And this is to initialize the "gardener", add plants, make them grow
    and then showing a small report like the flowers each gardener has,
    how much they grew, their total score for each plant...
    """
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.stats_helper = self.GardenStats(self.plants)
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"\n{self.owner} is helping all plants grow...\n")
        for plant in self.plants:
            plant.grow(1)
            self.total_growth += 1

    def report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display_info()

        reg, flow, prz = self.stats_helper.calculate_plant_types()
        valid = self.stats_helper.check_height_validation()

        print(f"\nPlants added: {len(self.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, "
              f"{prz} prize flowers\n")
        print(f"Height validation test: {valid}")

    @classmethod
    def create_garden_network(cls):
        """
        This is a 'Factory Worker' method
        It doesn't belong to one person (self), it belongs to the Class (cls)
        It uses the 'Garden Blueprint' (cls) to build two new gardens!

        So we create Alice and Bob as 'Instances'-independent gardens
        that follow the same rules but have their own separate data.
        """
        return cls("Alice"), cls("Bob")

    @staticmethod
    def get_system_status():
        """
        A static method is just a normal function that lives inside a class.
        It doesn't get 'self' or 'cls' handed to it.
        It CAN return values (like this string), it just doesn't
        need to 'touch' any specific garden to do its job.
        """
        return f"Total gardens managed: {GardenManager.total_gardens}"


def main() -> None:
    print("\n=== Garden Management System Demo ===\n")
    alice_g, bob_g = GardenManager.create_garden_network()

    alice_g.add_plant(Plant("Oak Tree", 100, 365))
    alice_g.add_plant(FloweringPlant("Rose", 25, 40, "red"))
    alice_g.add_plant(PrizeFlower("Sunflower", 50, 90, "yellow", 10))

    bob_g.add_plant(Plant("Small Bush", 92, 10))

    alice_g.grow_all()
    alice_g.report()

    a_score = alice_g.stats_helper.get_total_score()
    b_score = bob_g.stats_helper.get_total_score()

    print(f"Garden scores - Alice: {int(a_score)}, Bob: {int(b_score)}")
    print(GardenManager.get_system_status())


if __name__ == "__main__":
    main()
