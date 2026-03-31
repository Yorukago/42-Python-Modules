"""
This is the bane of my existence, mostly cuz...yeah, this kinda sucked
i also tried some weird implementations but i tried my best to keep it
a bit more simple/bearable now
This now instead of tuples, we use sets, sets are good for this cuz we
avoid something pretty common, called dupes, sets HATE duplicates!!
And its also pretty easy to look at and compare which collections overlap

Overlap = Intersections (things that are common to 2 people)
Leftovers = Difference (things that are different...)
"""


def analyze_achievements(a: set[str], b: set[str], c: set[str]) -> None:
    print("\n=== Achievement Analytics ===\n")

    # total unique
    all_unique = a | b | c
    print(f"All unique achievements: {sorted(all_unique)}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    # common to all
    common_all = a & b & c
    print(f"Common to all players: {common_all}")

    # we find who has it exclusively vs EVERYONE else
    a_only = a - b - c
    b_only = b - a - c
    c_only = c - a - b
    rare = a_only | b_only | c_only
    print(f"Rare achievements (1 player): {sorted(rare)}\n")

    # comparisons
    print(f"Alice vs Bob common: {a & b}")

    # "alice unique" here means alice minus bob
    print(f"Alice unique: {a - b}")

    # "bob unique" here means bob minus alice
    print(f"Bob unique: {b - a}")


def main() -> None:
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    analyze_achievements(alice, bob, charlie)


if __name__ == "__main__":
    main()
