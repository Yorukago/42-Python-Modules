import time
from collections.abc import Iterator


"""
This below me is called the "event generator" or smth like that
We have our players, we can add more i guess......but i just followed
the subject and we have our actions, since nothing to a computer is random
we do a bit of "randomizing magic" and then we have the key piece of this gen
called "yield", yield returns a tuple with the player, level and the action
every time, like a chef making a pizza...
"""


def event_generator(count: int) -> Iterator[tuple]:
    players = ["alice", "bob", "charlie", "david"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i * 7) % 20 + 1
        yield i, player, level, action


def fibonacci_gen(n: int):
    """
    the fib sequence goes on for infinity... but with a generator
    things are easier to do, since we have yield!!
    """
    a, b = 0, 1
    for _ in range(n):  # this goes on for infinity
        yield a  # this always pauses for each number so no kaboom
        a, b = b, a + b


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_gen(n: int) -> Iterator[int]:
    """
    same for prime numbers, they go on to infinity, but yield always returns
    their number, and then resumes work again and again...
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    high_level_count = 0
    treasure_count = 0
    level_up_count = 0

    start_time = time.time()

    for i, player, level, action in event_generator(event_count):
        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {action}")
        elif i == 4:
            print("...")

        if level >= 10:
            high_level_count += 1
        if "treasure" in action:
            treasure_count += 1
        if "leveled up" in action:
            level_up_count += 1

    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_list = [str(num) for num in fibonacci_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(num) for num in prime_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    main()


"""
Generators are good at this kind of thing cuz they are memory efficient
since they dont store anything on an array, they "stream" like a river
it gives the things you want at this point in time and unloads the things
generated in the past...
"""
