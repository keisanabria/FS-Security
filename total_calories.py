import censusAPI
from pathlib import Path
import pandas as pd

# !!! More information about this module in Section 2.1 of README.md

popPerSubCou = "data/live_data/popPerSubCou.csv"

# Verify if the data to be used is already a CSV file
def verifyData(fileName):
    file_path = Path(fileName)

    # Checking if the file exists
    if file_path.exists():
        fileExists = True
        return fileExists
    else:
        # If it doesn't, create the csv file for the data to be used
        censusAPI.popPerSubCou()

df = pd.read_csv(popPerSubCou) # Read the CSV file into a DataFrame

varGroup = {  
    1: "DP05_"
}

# Generate variable names programmatically
varNames = [f"{varGroup[1]}{str(i).zfill(4)}E" for i in range(5, 18)] + [
    f"{varGroup[1]}0002PE",
    f"{varGroup[1]}0003PE"
]

# Get the indices for the varNames from df
indexVarNames = {} # Key: varName, Value: Index
varNamesCol = df.iloc[:, 1]
index = 0
for var in df.iloc[:, 1]:
    if var in varNames:
        indexVarNames[var] = index
    index += 1

# Go through list of elements to make sure I get the information I need per lists (subCous) within the list
for varName in varNames:
    index = indexVarNames[varName]
    print(df.iloc[index])