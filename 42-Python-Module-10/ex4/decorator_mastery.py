import functools
import time
from typing import Callable, Any


# the spell timer... our magical stopwatch.
def spell_timer(func: Callable) -> Callable:
    """
    this decorator wraps a function to see how long it takes to finish
    """
    # @functools.wraps is the 'identity spell'. it makes sure the
    # wrapped function still remembers its own name and docs
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"casting {func.__name__}...")
        start_time = time.perf_counter()
        # we execute the actual spell here.
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"spell completed in {duration:.3f} seconds")
        return result
    return wrapper


# the power validator factory... for gatekeeping high-level spells
def power_validator(min_power: int) -> Callable:
    """
    this is a 'decorator factory'—it's a function that returns a decorator
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # logic check: if we are inside a class, 'self' is args[0]
            # we find the 'power' value to see if the mage is strong enough
            p_val = args[0] if not hasattr(args[0], 'cast_spell') else args[2]

            if p_val >= min_power:
                return func(*args, **kwargs)
            # if they are too weak, the spell never even starts
            return "insufficient power for this spell"
        return wrapper
    return decorator


# the retry decorator... for spells that are a bit sus
def retry_spell(max_attempts: int) -> Callable:
    """
    this decorator catches errors and tries again until it hits the limit
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    # try to cast the spell...
                    return func(*args, **kwargs)
                except Exception:
                    # if it fails, we log the attempt and loop again
                    print(f"spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# the mage guild...
class MageGuild:
    """
    a class that uses decorators to keep its mages in check
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        static methods are just utility functions.
        they don't need 'self' because they don't look at instance data.
        """
        if len(name) < 3:
            return False
        # only letters and spaces allowed in our guild
        return all(char.isalpha() or char.isspace() for char in name)

    # we apply our power validator directly to the method
    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"successfully cast {spell_name} with {power} power"


# the final ritual... testing our master-level magic
def main() -> None:

    @spell_timer
    def fireball():
        # we simulate a slow-casting spell
        time.sleep(0.1)
        return "fireball cast!"

    print("testing spell timer...")
    print(f"result: {fireball()}")

    print("\ntesting mageguild...")
    guild = MageGuild()

    # testing our static utility method.
    print(f"is 'gandalf' valid? {guild.validate_mage_name('gandalf')}")
    print(f"is '12' valid? {guild.validate_mage_name('12')}")

    # testing the decorated class method
    print(guild.cast_spell("lightning", 15))
    print(guild.cast_spell("spark", 5))

    print("\ntesting retry decorator...")

    @retry_spell(max_attempts=3)
    def unstable_portal():
        # this spell ALWAYS fails, so we can see the retries in action
        raise ValueError("portal collapsed!")

    print(unstable_portal())


if __name__ == "__main__":
    main()

"""
we made our own custom decorators, and these ones enable something akin to a
"separation of concerns" they let us separate the main logic (like casting
something) from other logics (like timing, checking power..), so this keeps
the code clean and lets us reuse the same decorators on other functions

im gosh darned traumatized, since we didnt use (or at least i didnt) any
more @staticmethod since module 1, so this...after an entire month of pain
and suffering, i have to say, regular methods need "self" to access the objects
data and a static method is just a function that lives inside a class for
organization purposes, it doesnt need to know anything about that specific
object at all...god why didnt they tell us this before man, i hate being a
test subject for this, give me my minis(hell) back

we use @functools.wraps(func) because without it, the function would "lose
its identity" and think its name is a wrapper, @wraps copies over the original
functions name and info, so that tools like help() would still work correctly

im honestly glad that this is over, since half of these modules are absolute
dogwater, most of them are useless at best and a waste of time at worst, just
filler like an anime beach episode, i do feel sorry for my evaluators to read
my code, and my comments, and to the person who will read this on my github,
however, i guess itll be better as the time passes by, i guess i was just
caught in the crossfire, i hope things will be better next time,
thanks for reading my absolutely pointless rambling
"""
