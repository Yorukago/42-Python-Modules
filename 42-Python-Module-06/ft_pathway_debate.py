import alchemy.transmutation as trans
import alchemy

"""
Basically we do the same thing over and over again...
Yeah boring
"""


def main() -> None:

    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {trans.lead_to_gold()}")
    print(f"stone_to_gem(): {trans.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {trans.philosophers_stone()}")
    print(f"elixir_of_life(): {trans.elixir_of_life()}")

    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work!")
    print("Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
