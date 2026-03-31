#!/usr/bin/env python3

class SecurePlant:
    """
    Same plant class, but now we follow one of the principles of OOP,
    encapsulation! In python we have single underscores, that mean "hey this
    variable is meant to be private, but you can touch it" while double
    underscores mean "hey, this is PRIVATE! HANDS OFF!!"
    """
    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        # double underscore here to say that its PRIVATE
        self.__height_cm = 0
        self.__age_days = 0

        self.set_height(height_cm)
        self.set_age(age_days)

    def get_height(self):
        # This is a getter, it gives a safe way to read data
        return self.__height_cm

    def get_age(self):
        return self.__age_days

    def set_height(self, new_height: int) -> None:
        # And this is a setter, it checks if the data someone inputs is valid
        if new_height < 0:
            print("Error: Height cannot be negative!")
        else:
            self.__height_cm = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Error: Age cannot be negative!")
        else:
            self.__age_days = new_age

    def display_info(self) -> None:
        print(f"SecurePlant: {self.name}")
        print(f"Height: {self.__height_cm}cm")
        print(f"Age: {self.__age_days} days")


def main():
    plant = SecurePlant("Lavender", 30, 20)
    plant.display_info()

    print("\nTrying some invalid updates...\n")

    plant.set_height(-10)
    plant.set_age(-5)

    plant.set_height(42)
    plant.set_age(25)

    plant.display_info()


if __name__ == "__main__":
    main()
