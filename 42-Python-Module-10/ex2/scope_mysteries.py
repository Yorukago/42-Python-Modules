from typing import Callable, Any, Dict


# counts how many times it has been called
def mage_counter() -> Callable[[], int]:
    # this variable lives in the 'outer' room
    count = 0

    def counter() -> int:
        # 'nonlocal' is the magic key.. it lets us reach out of
        # this inner room and change the count in the hallway
        nonlocal count
        count += 1
        return count

    return counter


# the power accumulator... a piggy bank for mana
def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    # we start with whatever power you give us
    total_power = initial_power

    def accumulator(amount: int) -> int:
        # again, we need 'nonlocal' to update the running total
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


# the enchantment factory... making custom name tags
def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    # we don't need 'nonlocal' here because we are just reading
    # the enchantment_type, not trying to change what it is
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


# the memory vault... a private safe for your secrets
def memory_vault() -> Dict[str, Callable]:
    # 'vault' is private, nobody outside this function can touch it
    vault: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        # we're adding stuff to the dict, so the dict itself stays
        # the same 'box', we're just putting stuff inside it
        vault[key] = value

    def recall(key: str) -> Any:
        # if the key isn't there, we give a friendly 'not found' message
        return vault.get(key, "memory not found")

    # we give back a dictionary of 'tools' instead of the data itself
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:

    print("testing mage counter...")
    # every time we call 'counter()', it remembers the last number
    counter = mage_counter()
    print(f"call 1: {counter()}")
    print(f"call 2: {counter()}")
    print(f"call 3: {counter()}")

    print("\ntesting spell accumulator...")
    # this starts at 100 and just keeps growing
    acc = spell_accumulator(100)
    print(f"adding 50: {acc(50)}")
    print(f"adding 25: {acc(25)}")

    print("\ntesting enchantment factory...")
    # we make one factory for fire and one for ice
    fire_factory = enchantment_factory("flaming")
    ice_factory = enchantment_factory("frozen")
    print(fire_factory("sword"))
    print(ice_factory("shield"))

    print("\ntesting memory vault...")
    # we use the 'store' and 'recall' tools we got back
    vault = memory_vault()
    vault["store"]("secret_code", "1234")
    print(f"recalling code: {vault['recall']('secret_code')}")
    print(f"recalling unknown: {vault['recall']('missing_key')}")


if __name__ == "__main__":
    main()

"""
a closure here is when a function remembers the variables from its
env, even after the parent function has finished its tasks, so its like
the function has a lil backpack with its own private data

whats nonlocal? and why use nonlocal? by default, python thinks variables
that live inside a function are brand new, nonlocal tells python "hey dont make
a new variable, cuz we already have one, go find it so i can update it"

using a memory_vault here follows one of the principles of OOP - encapsulation
the dict is totally hidden and the only way to interact with it is through the
"store" and "recall" functions we provided, better than a global variable here
"""
