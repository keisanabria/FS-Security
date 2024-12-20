import requests
import geopandas as gpd

# Transpose json file containing population per subdivision to csv
def popPerSubCou():
    # API link that contains variable with population according to age and gender ALONG with other variables
    r = requests.get("https://api.census.gov/data/2023/acs/acs5?get=group(B01001)&ucgid=pseudo(0400000US72$0600000)").json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    popPerSubCou = "data/live_data/popPerSubCou.csv"
    df.transpose().to_csv(popPerSubCou)

def perPerSubCou():
    # API link that contains variable with percentages of populations (Male and Female) ALONG with other variables
    r = requests.get("https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP05)&ucgid=pseudo(0400000US72$0600000)").json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    perPerSubCou = "data/live_data/perPerSubCou.csv"
    df.transpose().to_csv(perPerSubCou)