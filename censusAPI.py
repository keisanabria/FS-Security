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

def households():
    # API link that contains variables of households according to their income in the subBarrios
    r = requests.get("https://api.census.gov/data/2023/acs/acs5/profile?get=DP03_0051E,DP03_0051PE,DP03_0052PE,DP03_0053PE,DP03_0054PE,DP03_0055PE,DP03_0056PE,DP03_0057PE,DP03_0058PE,DP03_0059PE,DP03_0060PE,DP03_0061PE&ucgid=pseudo(0400000US72$0600000)").json()
    df = gpd.GeoDataFrame(r)
    # Transpose the variables to a csv file
    households = "data/live_data/households.csv"
    df.transpose().to_csv(households)