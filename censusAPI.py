import requests
from mapCreation import gpd

# More information of this module in Section 2.1 of README.md

# API link that contains variable with population according to age and gender ALONG with other variables
r = requests.get("https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP05)&ucgid=pseudo(0400000US72$0600000)").json()
df = gpd.GeoDataFrame(r)
# Transpose the variables to a csv file
df.transpose().to_csv("data/live_data/popPerAge_Gender.csv")

# Go through list of elements to make sure I get the information I need per lists (subCous) within the list
varGroup = {  
    1: "DP05_"
}

# Generate variable names programmatically
varNames = [f"{varGroup[1]}{str(i).zfill(4)}E" for i in range(5, 18)] + [
    f"{varGroup[1]}0002PE",
    f"{varGroup[1]}0003PE"
]

print(varNames)

# print(variableNames[varResults.index("312")])