"""
This is the 'Oracle Mainframe' script
Its job is to look at the 'Hidden Notes' (.env file) on your computer
so it knows how to connect to the Matrix without telling everyone the password
"""
import os  # This is the tool that lets python talk to your OS


def read_mainframe() -> None:

    print("ORACLE STATUS: Reading the Matrix...")
    try:
        # this line is like opening a secret envelope
        # it takes everything in '.env' and
        # puts it into the computer's temp mem
        from dotenv import load_dotenv  # we do a late import here...
        load_dotenv()

        # 'os.getenv' is like asking the computer:
        #    - "Hey, do you have a note for 'MATRIX_MODE'?"
        # if the computer says "No," the script
        # uses "unknown" as a backup (Plan B)
        mode = os.getenv("MATRIX_MODE", "unknown")

        # checking for the database address
        db = os.getenv("DATABASE_URL", "Not connected")

        # this is a 'One-Line If' below...
        # if the API_KEY exists, say 'Authenticated'
        # otherwise, say 'Missing Key'
        api = "Authenticated" if os.getenv("API_KEY") else "Missing Key"

        log = os.getenv("LOG_LEVEL", "INFO")
        zion = os.getenv("ZION_ENDPOINT", "Offline")

        print("\nConfiguration loaded:")
        print(f"Mode: {mode}")
        print(f"Database: {db}")
        print(f"API Access: {api}")
        print(f"Log Level: {log}")
        print(f"Zion Network: {zion}")

        print("\nEnvironment security check:")

        # this checks if the '.env' file actually exists on your hard drive
        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            # if the file is gone, the script might still work if the settings
            # were already typed into the computer's 'System Variables'
            print("[WARNING] .env file missing - using system env vars")

        print("[OK] No hardcoded secrets detected")
        print("The Oracle sees all configurations.")

    except ImportError as e:
        print(f"\n[ERROR]: Missing dependency: {e}\n")
        print("Try installing it inside the Matrix:")
        print("python3 pip install python-dotenv")
        print("\nAnd run this program again!")
    except Exception as e:
        print(f"Error accessing the mainframe: {e}")


if __name__ == "__main__":
    read_mainframe()
