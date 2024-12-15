import requests
from mapCreation import gpd

# Transpose json file containing population per subdivision to csv
def popPerSubCou():
    # API link that contains variable with population according to age and gender ALONG with other variables
    r = requests.get("https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP05)&ucgid=pseudo(0400000US72$0600000)").json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    popPerSubCou = "data/live_data/popPerSubCou.csv"
    df.transpose().to_csv(popPerSubCou)