import mapCreation
from total_calories import calorie_df
from insec_households import insec_households
import schedule
import time
import subprocess
import os
from apscheduler.schedulers.background import BackgroundScheduler

# Show map 
# def main() -> None:
#     mapCreation.createMap('Total de calorias')

# if __name__ == "__main__":
#     main()

def run_program():
    try:
        # Check the operating system
        if os.name == "nt":  # Windows
            python_path = r".venv\Scripts\python.exe"
        else:  # macOS/Linux
            python_path = ".venv/bin/python.exe"

        # Verify if the Python executable exists
        if not os.path.isfile(python_path):
            raise FileNotFoundError(f"Python executable not found at {python_path}")
        
        print(f"Running total_calories.py and insec_households.py with Python at {python_path}...")
        # Data-fetching code is located in total_calories.py and insec_households.py
        subprocess.run([python_path, "total_calories.py"])
        subprocess.run([python_path, "insec_households.py"])

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Ensure the virtual environment is properly set up and the script is being run from the correct location.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

run_program()

# # Set up the scheduler
# scheduler = BackgroundScheduler()
# # Schedule the job for every year on December 31st each year
# scheduler.add_job(run_program, 'cron', month=12, day=31, hour=00, minute=00)

# scheduler.start()

# # Keep the script running
# try:
#     while True:
#         time.sleep(1)
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()