#!/usr/bin/env python3

def main() -> None:
    """ Making a plant with a name, height and age (in days) """
    name: str = "Tulip"
    height: int = 25
    age: int = 2

    print("~ Community Garden Plant Information Board ~\n")
    print(f"Plant name: {name}")
    print(f"Plant height: {height} cm")
    print(f"Plant age: {age} days")
    print("~ End of List ~\n")


"""
This..thing below serves as the program's entry point
Deleting this makes it still work
This is more for...various files and imports, since python reads
every file from top to bottom, this is just a cute lil flag that says
'hey! read me first!!' to avoid messes down the line
"""
if __name__ == "__main__":
    main()
