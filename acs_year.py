from datetime import datetime

def getACS_year():
    # Get the current year
    current_year = datetime.now().year

    # API requires the previous year's data (as ACS releases lag by one year)
    acs_year = current_year - 1

    # Uncomment below for testing purposes
    acs_year = 2023

    return acs_year