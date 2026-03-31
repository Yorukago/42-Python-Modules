def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as vault:
            content = vault.read().strip()
            if "CORRUPTION" in content or "ERROR" in content:
                print(f"RESPONSE: Data corruption dectected - {content}")
                print("STATUS: Crisis handled, data recovery attempted\n")
            else:
                print(f"SUCCESS: Archive recovered - {content}")
                print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly: {e}")
        print("STATUS: Emergency protocols engaged")

    except OSError as e:
        print(f"Error...thing, heres the thing - {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    # looks for these files in here... u have to chmod the classified
    # data for it to work tho...
    scenarios = [
        "lost_archive.txt",  # should be FileNotFound...
        "classified_data.txt",  # should be PermissionError...
        "corrupted_archive.txt",  # should like...say an error
        "standard_archive.txt"  # Should be okay
    ]

    for archive in scenarios:
        crisis_handler(archive)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
