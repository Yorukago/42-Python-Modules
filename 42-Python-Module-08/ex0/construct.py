import sys
import os
import site


def get_env_info() -> None:
    """
    Detects the current Python environment and prints status/info
    basically a pretty simple way to check if u are in the venv or not
    """
    try:
        is_venv = sys.prefix != sys.base_prefix
        if not is_venv:  # if u didnt do source matrix_env/bin/activate....
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows")
            print("\nThen run this program again.")
        else:  # if u are inside the venv!
            venv_name = os.path.basename(sys.prefix)
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")

            pkg_path = site.getsitepackages()[0]
            print(f"\nPackage installation path:\n {pkg_path}")

    except Exception as e:
        print(f"An error occurred while reading system info: {e}")


if __name__ == "__main__":
    get_env_info()
