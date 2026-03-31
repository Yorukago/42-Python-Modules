def recover_data(filename: str) -> None:
    print(f"Accessing Storage Vault: {filename}")

    try:
        with open(filename, 'r') as vault:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            content: str = vault.read()
            if not content.strip():
                print("[EMPTY VAULT] No data fragments found.")
            else:
                print(content.strip())

        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:  # if file not found...
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:  # if bad permissions... u should use chmod
        print("ERROR: Access denied. Insufficient clearance for this vault.")
    except Exception as e:  # other errors typashit
        print(f"ERROR: An unexpected corruption occurred: {e}")
    except OSError as e:  # even more sus errors all around
        print(f"Error...thing, heres the thing - {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    # looks for ancient_fragment.txt made with data generator
    target_vault: str = "ancient_fragment.txt"
    recover_data(target_vault)


if __name__ == "__main__":
    main()
