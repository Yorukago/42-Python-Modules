import functools
import operator
from typing import List, Callable, Dict, Any


# the spell reducer... it squishes a whole list into one single number
def spell_reducer(spells: List[int], operation: str) -> int:
    # we map the name of the trick to the actual math tool from 'operator'
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    # reduce() is like a snowball, it takes the first two numbers,
    # does the math, then uses that result with the next number, and so on
    return functools.reduce(ops[operation], spells)


# the partial enchanter... for when you're too lazy to type every argument
def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    """
    partial() 'freezes' some arguments so the function is ready to go!
    """
    # we pre-load 'fire' and '50' power into the base spell
    # now the new function only needs to know the 'target'
    return {
        'fire_enchant': functools.partial(base_enchantment, "fire", 50),
        'ice_enchant': functools.partial(base_enchantment, "ice", 50),
        'lightning_enchant': functools.partial
        (base_enchantment, "lightning", 50)
    }


# the memoized fibonacci... a function with a perfect memory
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    # without lru_cache, this would be super slow
    # with it, python saves the answer to every 'n' it's already seen
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# the spell dispatcher...
def spell_dispatcher() -> Callable:
    # singledispatch lets the function change its behavior based on
    # the type of data (int, str, list) you throw at it
    @functools.singledispatch
    def dispatcher(spell_input: Any) -> str:
        return f"unknown spell type: {type(spell_input)}"

    # if we give it a number, it acts like a damage spell
    @dispatcher.register(int)
    def _(spell_input: int) -> str:
        return f"damage spell: dealing {spell_input} damage!"

    # if we give it a string, it acts like an enchantment
    @dispatcher.register(str)
    def _(spell_input: str) -> str:
        return f"enchantment: casting {spell_input}..."

    # if we give it a list, it handles a multi-cast combo
    @dispatcher.register(list)
    def _(spell_input: list) -> str:
        return f"multi-cast: sequential spells {spell_input}"

    return dispatcher


# the main ritual... showing off our library treasures
def main() -> None:

    powers = [10, 20, 30, 40]
    print("testing spell reducer...")
    # sum: 10+20+30+40 = 100
    print(f"sum: {spell_reducer(powers, 'add')}")
    # product: 10*20*30*40 = 240000
    print(f"product: {spell_reducer(powers, 'multiply')}")
    print(f"max: {spell_reducer(powers, 'max')}")

    def base_spell(element: str, power: int, target: str) -> str:
        return f"{element} enchantment ({power} power) on {target}"

    enchanters = partial_enchanter(base_spell)
    print("\ntesting partial enchanter...")
    # we only pass the target because 'element' and 'power' are already frozen
    print(enchanters['fire_enchant']("wooden shield"))
    print(enchanters['ice_enchant']("iron sword"))

    print("\ntesting memoized fibonacci...")
    # this is instant because of the cache!
    print(f"fib(10): {memoized_fibonacci(10)}")
    print(f"fib(15): {memoized_fibonacci(15)}")

    print("\ntesting spell dispatcher...")
    cast = spell_dispatcher()
    # same function name, but three different behaviors
    print(cast(150))
    print(cast("shield of light"))
    print(cast([10, "heal"]))


if __name__ == "__main__":
    main()

"""
functools.partial is creating a new version of a function with some of the args
filled in... a nice way to preconfigure functions so u avoid DRY (dont
repeat yourself) phenomena

lru_cache is nice for recursion because fibonacci (for example) is really slow
cuz it recalculates the same numbers over and over, the cache stores the
results in the memory (memoization (stupid word btw)) so it only does the work
once per number, so its more efficient in the long run

singledispach helps out with one problem we all face, clean code..
or lack thereof
it avoids the messy if/elif/else blocks checking for types and follows
the "single responsability principle" - "a class, module, or function should
have one—and only one—reason to change" (<- taken from google), in more simple
wording: a class shouldnt be responsible for things outside of its scope
"""
