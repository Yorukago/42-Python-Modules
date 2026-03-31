import importlib  # This is a search tool that looks for other code files


def check_dependencies() -> bool:
    """
    the 'toolbox checker' function
    it goes through a list of names and tries to find them on the computer
    returns: true if everything is found, false if we are missing a tool
    """
    # these are the names of the big 'LEGO sets' we want to use
    packages = ["pandas", "numpy", "matplotlib"]
    all_ok = True

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg in packages:
        try:
            # this is like reaching into a dark closet to see if a box is there
            # unknown here is like a "fallback value" in case stuff...yeah
            module = importlib.import_module(pkg)

            # if we found it, we check the label for a 'Version number'
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - Ready")

        except ImportError:
            print(f"[ERROR] {pkg} is missing!")
            all_ok = False

    return all_ok


def run_analysis() -> None:
    try:
        # we give these big tools 'nicknames' so they are easier to call
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("Analyzing Matrix data...")

        # we are asking 'numpy' to roll a bunch of dice (0s and 1s) for us
        data = np.random.randint(0, 2, size=(100, 3))

        # we put those dice results into a nice 'Excel-style' table
        dataframe = pd.DataFrame(data, columns=['Neo', 'Trinity', 'Morpheus'])

        print(f"Processing {len(dataframe)} data points...")

        # we tell 'matplotlib' to draw a pretty picture of these numbers
        dataframe.cumsum().plot()
        plt.title("Matrix Synchronization")

        # we save that drawing as a real file on our computer
        plt.savefig("matrix_analysis.png")
        print("Analysis complete! Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    if check_dependencies():
        run_analysis()
    else:
        print("\nTo fix missing dependencies, run:")
        print("pip install -r requirements.txt or...")
        print("poetry run")
