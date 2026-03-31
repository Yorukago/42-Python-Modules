import sys

"""
Basically, this is just an argument counter...
like argc argv, the ac 0 is the program name and it
counts starting on 1 to...whatever args you put in there
"""


def display_quest_info(args: list[str]) -> None:

    total_count: int = len(sys.argv)
    program_name: str = sys.argv[0]

    print("=== Command Quest ===\n")

    if not args:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_count}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {len(args)}")

        for i, value in enumerate(args, 1):
            print(f"Argument {i}: {value}")

        print(f"Total arguments: {total_count}")


def main() -> None:
    display_quest_info(sys.argv[1:])


if __name__ == "__main__":
    main()
