from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("Testing Abstract Base Class Design:")
    print(f"CreatureCard Info:\n{dragon.get_card_info()}")

    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print(f"\n{dragon.name} attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
