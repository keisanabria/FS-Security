import mapCreation
from total_calories import calorie_df
from insec_households import insec_households
import schedule
import time
import subprocess

# Show map 
# def main() -> None:
#     mapCreation.createMap('Total de calorias')

# if __name__ == "__main__":
#     main()

# ---------------------------------------------------------------------------

# def run_program():
#     # Data-fetching code
#     print("Running total_calories.py as a separate script...")
#     subprocess.run(["python", "total_calories.py"])

# run_program()

import os
import subprocess
import sys

try:
    # Check the operating system
    if os.name == "nt":  # Windows
        python_path = "./env/Scripts/python"
    else:  # macOS/Linux
        python_path = "./env/bin/python"

    # Verify if the Python executable exists
    if not os.path.isfile(python_path):
        raise FileNotFoundError(f"Python executable not found at {python_path}")

    print(f"Running total_calories.py with Python at {python_path}...")
    subprocess.run([python_path, "total_calories.py"])

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Ensure the virtual environment is properly set up and the script is being run from the correct location.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# ---------------------------------------------------------------------------

# # Schedule the program for December 1st each year
# schedule.every().year.at("2024-12-01 00:00").do(run_program)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
