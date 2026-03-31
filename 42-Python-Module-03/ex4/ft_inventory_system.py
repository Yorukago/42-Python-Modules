import sys

"""
This is now about another type of "storing data thingggg"
called "dictionaries" (idk how to write that well), but the
cool thing about it is that we can make something called "nested
dictionaries", its just dictionaries inside dictionaries, less
talking more showing.

We could have a BIG dictionary called "inventory" and then we can have
smaller dictionaries that have the "equipment" and/or "potions" and/or
*insert whatever thing u have on an rpg game or smth*

Thats cool!
"""


def get_quantity(item_tuple: tuple[str, int]) -> int:
    # we want the NUMBER (which is on 1) and NOT the name itself
    return item_tuple[1]


def analyze_inventory(inventory: dict[str, int]) -> None:
    if not inventory:
        print("Inventory is empty!")
        return

    total_units: int = sum(inventory.values())
    unique_types: int = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    sorted_items = sorted(
        inventory.items(), key=get_quantity, reverse=True
    )

    for item, qty in sorted_items:
        percentage = (qty / total_units) * 100
        print(f"{item}: {qty} units ({percentage:.1f}%)")

    most_name, most_qty = sorted_items[0]
    least_name, least_qty = sorted_items[-1]

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_name} ({most_qty} units)")
    print(f"Least abundant: {least_name} ({least_qty} units)")

    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for item, qty in inventory.items():
        if qty >= 4:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty

    print("\n=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    restock = [item for item, qty in inventory.items() if qty == 1]
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ", ".join(inventory.keys())
    values_str = ", ".join(str(v) for v in inventory.values())

    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")

    has_sword = "sword" in inventory
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        return

    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
        except ValueError:
            continue

    analyze_inventory(inventory)


if __name__ == "__main__":
    main()
