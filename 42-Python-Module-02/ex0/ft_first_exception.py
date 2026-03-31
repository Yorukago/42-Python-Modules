def check_temperature(temp_str) -> None:
    try:
        temp = int(temp_str)

        if 0 <= temp <= 40:
            return temp
        else:
            print(f"Error: {temp} is out of safe plant range (0-40).")
            return None

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number.")
        return None


def test_temperature_input() -> None:
    print("--- Starting Temperature Validation Tests ---")

    test_data = ["25", "abc", "100", "-50"]

    for data in test_data:
        print(f"\nTesting input: {data}")
        result = check_temperature(data)

        if result is not None:
            print(f"Success: {result} is a valid temperature.")
        print("\n" + "-" * 20)

    print("\nTest complete. System is still running smoothly!")


if __name__ == "__main__":
    test_temperature_input()
