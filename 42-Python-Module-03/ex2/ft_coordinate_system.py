import math
import sys

"""
God i hated this one with a passion, so this is the "euclidian
distance" thing, ill comment stuff a lot in here since i HATE MATH.
AND i have pity on my future evaluators, im sorryyyy
"""


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    """
    This is the so called "euclidian distance" which is the
    pythagorean theorem with a fresh coat of pain(t) and
    suffering.
    Dont ask me how this works, i just copied it from the subject
    """
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt(
        (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    )
    return round(distance, 2)


def parse_coords(coord_str: str) -> tuple[int, int, int]:
    """
    Remember to handle the classic "I typed 'abc' instead of
    '123'" error gracefully! - Said 42, the wise overlords
    """
    clean_str = coord_str.strip("() ")
    parts = clean_str.split(",")

    if len(parts) != 3:
        raise ValueError("Coordinates must have exactly 3 values (x,y,z)")

    return tuple(int(p.strip()) for p in parts)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)

    pos1: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {pos1}")
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1}\n")

    coord_input = "3,4,0"
    print(f'Parsing coordinates: "{coord_input}"')
    try:
        pos2 = parse_coords(coord_input)
        print(f"Parsed position: {pos2}")
        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2}\n")

        print("Unpacking demonstration:")
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}\n")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    if len(sys.argv) > 1:
        print(f"Processing Terminal Argument: {sys.argv[1]}")
        try:
            user_pos = parse_coords(sys.argv[1])
            print(f"Parsed from argv: {user_pos}")
            print(f"Distance from origin: {calculate_distance(origin,
                  user_pos)}")
        except ValueError as e:
            print(f"Argv Error: {e}")
    else:
        print("No terminal arguments found. Try: python3 script.py 3,4,0")

    invalid_input = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_input}"')
    try:
        parse_coords(invalid_input)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


if __name__ == "__main__":
    main()


"""
The subject asks for what "unpacking" is, idfk where to put it so here:
unpacking is like... a really good way to read code i guess??
how easier is to read this
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    vs
this?
    distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
yeah....i guess thats unpacking for ya
and why tuples? the subject wants us to use tuples but theyre good with this
tuples cannot be modified (in obvious ways at least) so coords can stay
consistent without any hiccups
"""
