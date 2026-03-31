def create_archive(filename: str) -> None:
    print(f"Initializing new storage unit: {filename}")

    """
    writeable content inside the new_discovery.txt
    its going to create a file..and write shit there
    """
    entries: list[str] = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]

    try:
        with open(filename, 'w') as vault:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            for i, entry in enumerate(entries, 1):
                formatted_entry: str = f"[ENTRY {i:03}] {entry}"
                # format specifier ^ to do "000" until "003"
                print(formatted_entry)
                vault.write(formatted_entry + "\n")

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except PermissionError:
        print(f"ERROR: No permission to create vault '{filename}'.")
    except Exception as e:
        print(f"ERROR: Archive initialization failed: {e}")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except OSError as e:
        print(f"Error...thing, heres the thing - {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM === \n")

    # makes a new file called new_discovery.txt
    target_file: str = "new_discovery.txt"
    create_archive(target_file)


if __name__ == "__main__":
    main()
