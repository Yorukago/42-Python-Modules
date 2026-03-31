from typing import List, Dict, Any


# this is our artifact sorter..
def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    we use a tiny lambda 'key' to tell the sorter:
    'hey, don't look at the whole bag, just look at the power number!'
    """
    # sorted() gives us a fresh new list
    # and leaves the old one alone. no messy mutation here
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)
    # basically lambda is        lambda(1) x(2) : x['power'](3)
    # 1 - lambda being the "magic word, like an "if/elif/else"
    # 2 - is the input, like this time its looking at the dict i gave
    # 3 - is the output, it returns the number INSIDE power :3


# the power filter... keeping the weak mages out of the club
def power_filter(mages: List[Dict[str, Any]],
                 min_power: int) -> List[Dict[str, Any]]:
    """
    this lambda is just a gatekeeper
    if the mage's power is high enough, it says 'true' and lets them in
    """
    # filter() gives us a 'ghost list' (iterator),
    # so we use list() to turn it back into real data.
    return list(filter(lambda m: m['power'] >= min_power, mages))


# the spell transformer... adding some sparkles up in here
def spell_transformer(spells: List[str]) -> List[str]:
    """
    map() is like a conveyor belt
    every spell that goes through gets stars stuck on both ends
    """
    return list(map(lambda s: f"* {s} *", spells))


# the mage stats.. the oracle's calculator
def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    we use a map to grab all the power levels first,
    then we let math do the rest of the heavy lifting
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    # we extract the numbers so max() and min() don't get confused by dicts
    powers = list(map(lambda m: m['power'], mages))

    max_p = max(powers)
    min_p = min(powers)
    # average power is just the total divided by how many mages we have
    avg_p = round(sum(powers) / len(powers), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


def main() -> None:
    # our victims today
    artifacts = [
        {'name': 'crystal orb', 'power': 85, 'type': 'focus'},
        {'name': 'fire staff', 'power': 92, 'type': 'weapon'}
    ]
    spells = ["fireball", "heal", "shield"]
    mages = [
        {'name': 'merlin', 'power': 95, 'element': 'arcane'},
        {'name': 'morgana', 'power': 88, 'element': 'shadow'},
        {'name': 'apprentice', 'power': 20, 'element': 'water'}
    ]

    print("testing artifact sorter...")
    sorted_art = artifact_sorter(artifacts)
    # the fire staff is usually the winner here
    print(f"{sorted_art[0]['name']} ({sorted_art[0]['power']} power) "
          f"comes before {sorted_art[1]['name']} "
          f"({sorted_art[1]['power']} power)")

    print("\ntesting spell transformer...")
    # turning a list into a string with spaces in between
    print(" ".join(spell_transformer(spells)))

    print("\ntesting mage stats...")
    stats = mage_stats(mages)
    print(f"max: {stats['max_power']}, min: {stats['min_power']}, "
          f"avg: {stats['avg_power']}")


if __name__ == "__main__":
    main()

"""
lambda makes code more concise and easy to read because they
eliminate the use of a full 3-liner function, instead of writing for a def
and then calling it manually, i can write the logic where i need it, you
dont really need to write it down always, its just..there
(although i really hate using lambda this is torture)

although lambdas are nice (not) sometimes not using one is better than using
it, lambdas are nice for "one line transformations" (like a map or filter) that
i wouldnt really use anywhere else, and using lambda on a more complex function
that might need multiple lines then its not worth it at all, good rule of
thumb is:
"if you need to comment on what a lambda is doing,
then u shouldnt be using one at all" - friend said it, i trust him. i hate this

map and filter always return iterators, u should wrap them in list() to see the
good stuff, or else ull see something like "<map object at 0x...>" when u try
to print it out

and another good thing to do, ww dont use .sort() we use sorted(), we dont
change the original lists in anything, we return a new one instead
"""
