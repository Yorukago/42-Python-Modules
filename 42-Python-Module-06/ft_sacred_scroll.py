import alchemy

"""
Demo script to show how to import things from other files
We can import libraries but we can also import files that we
made too...
'import alchemy' is the name of the folder/module
'alchemy.elements.<function>' is a direct module access,
basically we literally "call" the function to work with
"""


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    fire_msg = alchemy.elements.create_fire()
    water_msg = alchemy.elements.create_water()
    earth_msg = alchemy.elements.create_earth()
    air_msg = alchemy.elements.create_air()

    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {fire_msg}")
    print(f"alchemy.elements.create_water(): {water_msg}")
    print(f"alchemy.elements.create_earth(): {earth_msg}")
    print(f"alchemy.elements.create_air(): {air_msg}")

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError "
              "- not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError "
              "- not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
