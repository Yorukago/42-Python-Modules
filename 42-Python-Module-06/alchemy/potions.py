# we relative import the elements from before
from .elements import create_fire, create_water, create_earth, create_air

"""
A relative import is used with dots!
. - means "same directory as the current file"
.. - means "one level up as the current file"
... - means "two levels up as the current file"
so on...
"""


def healing_potion() -> str:
    # we create the potions with fire and water
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    # we create the potions with earth and fire
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    # we create the potion with air and water
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    # we create the potion with all elements
    res = (f"{create_fire()}, {create_water()}, "
           f"{create_earth()}, {create_air()}")
    return f"Wisdom potion brewed with all elements: {res}"
