import mapCreation
from total_calories import calorie_df
from insec_households import insec_households

# Show map 
def main() -> None:
    mapCreation.createMap('Total de calorias')

if __name__ == "__main__":
    main()

import schedule
import time

def run_program():
    # Data-fetching code
    

# Schedule the program for December 1st each year
schedule.every().year.at("2024-12-01 00:00").do(run_program)

while True:
    schedule.run_pending()
    time.sleep(1)
