import requests
import geopandas as gpd
from update_data import popPerSubCou_url, households_url, acs_year

# Transpose json file containing population per subdivision to csv
def popPerSubCou():
    # API link that contains variable with population according to age and gender ALONG with other variables
    r = requests.get(popPerSubCou_url).json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    popPerSubCou = f"data/live_data/{acs_year}popPerSubCou.csv"
    df.transpose().to_csv(popPerSubCou)

def households():
    # API link that contains variables of households according to their income in the subBarrios
    r = requests.get(households_url).json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    households = f"data/live_data/{acs_year}households.csv"
    df.transpose().to_csv(households)