def perform_security_ops() -> None:
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            # its gonna look for classified data...so again run the data gen
            for line in vault:
                print(line.strip())

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: Access denied. Insufficient clearance for this vault.")
    except Exception as e:
        print(f"ERROR: An unexpected corruption occurred: {e}")
    except OSError as e:
        print(f"Error...thing, heres the thing - {e}")

    print("\nSECURE PRESERVATION:")
    with open("security_log.txt", "w") as log:
        msg = "[CLASSIFIED] New security protocols archived"
        log.write(msg + "\n")
        print(msg)

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security")


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    perform_security_ops()


if __name__ == "__main__":
    main()
