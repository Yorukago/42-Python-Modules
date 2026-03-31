from typing import Callable, Any, List, Tuple


# combines spells
def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    # it makes a new double-spell that happens at the same time
    def combined_spell(*args, **kwargs) -> Tuple[Any, Any]:
        # returns both spells with the keyword args
        # kwargs is a dict that catches everything, u can see it below
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined_spell


# makes power more like POWER
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args, **kwargs) -> Any:
        return base_spell(*args, **kwargs) * multiplier

    return amplified_spell


# checks if u have enough mana to cast a spell
def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    # it only lets the magic through if the rules say yes
    def gated_spell(*args, **kwargs) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        # if not, the magic goes poof and fizzles out
        return "spell fizzled"

    return gated_spell


# spam spells u insignificant newbie
def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence_caster(*args, **kwargs) -> List[Any]:
        # makes a list of all the cool things that happened
        return [s(*args, **kwargs) for s in spells]

    return sequence_caster


def main() -> None:

    def fireball(target: str) -> str:
        return f"fireball hits {target}"

    def heal(target: str) -> str:
        return f"heals {target}"

    # dmg counter
    def damage_calc(val: int) -> int:
        return val

    print("testing spell combiner...")
    # sticking fireball and heal together
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("dragon")
    print(f"combined spell result: {res1}, {res2}")

    print("\ntesting power amplifier...")
    # making a spell three times stronger
    mega_spell = power_amplifier(lambda x: x, 3)
    print(f"original: 10, amplified: {mega_spell(10)}")

    print("\ntesting conditional caster...")

    # no friendly fire allowed
    def is_enemy(target: str) -> bool:
        return target != "ally"

    pvp_spell = conditional_caster(is_enemy, fireball)

    print(f"targeting orc: {pvp_spell('orc')}")
    print(f"targeting ally: {pvp_spell('ally')}")

    print("\ntesting spell sequence...")

    # casting three fireballs in a row for a big combo
    combo = spell_sequence([fireball, fireball, fireball])
    print(f"triple cast: {combo('slime')}")


if __name__ == "__main__":
    main()

"""
functions are like "first class citizens", they are treated
like any other object like ints or strs, i can assign them to a
variable, pass it as an argument to another function..return as a value
or even store them in a list or a dict, fun right?

"high-order" functions allow us to create "templates" for behavior, instead
of writing a bazillion "amplified" spells, i can write one "power_amp" that
can enhance any spell i so desire and "composition" lets me build a more
"complex" logic by chaining more simpler, single purpose functions together
like in spell_squence

**kwargs (KeyWord ARGuments) and *args are used in the nested functions i did
they are "catch-all" arguments, meaning that my combines/amplified spells
can take any number of arguments, making functions more flexible

closures...more on the next exercise, are present in here, when u define
a function inside another, the inner function remembers the variables from
the outer function like a backpack that stores things
"""
