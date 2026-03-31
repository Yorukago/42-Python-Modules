def garden_operations() -> None:
    print("\nTesting ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing_garden_data.txt", "r")
    except FileNotFoundError as e:
        print(
            f"Caught FileNotFoundError: [Errno 2] "
            f"{e.strerror} 'missing.txt'"
        )

    print("\nTesting KeyError...")
    try:
        garden_inventory = {"roses": 5}
        print(garden_inventory["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        result = 1 / 0
        print(result)
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but the program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
