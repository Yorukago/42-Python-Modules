from .basic import lead_to_gold
from ..potions import healing_potion
# and here is a relative import


def philosophers_stone() -> str:
    res = f"{lead_to_gold()} and {healing_potion()}"
    return f"Philosopher's stone created using {res}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
