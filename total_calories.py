import pandas as pd
import geopandas as gpd
import verifyFile
import acs_year

def getTotalCalories():
    # !!! More information about this module in Section 2.1 of README.md

    acsYear = acs_year.getACS_year()

    verifyFile.verifyFile(f"data/live_data/{acsYear}popPerSubCou.csv", 'popPerSubCou')

    pop_df = pd.read_csv(f"data/live_data/{acsYear}popPerSubCou.csv") # Read the CSV file into a DataFrame

    varGroup = {  
        1: "B01001_"
    }

    # Generate variable names programmatically
    popVarNames = [
        f"{varGroup[1]}{str(i).zfill(3)}E"
        for i in range(3, 50)
        if i != 26  # Exclude 026
    ]

    def getIndices(df, varNames):
        # Get the indices for the varNames from df
        indexVarNames = {} # Key: varName, Value: Index
        varNamesCol = df.iloc[:, 1]
        index = 0
        for var in df.iloc[:, 1]:
            if var in varNames:
                indexVarNames[var] = index
            index += 1
        
        return indexVarNames

    # Dictionary with indices of varNames
    indicesPopVar = getIndices(pop_df, popVarNames)

    # TESTING ---------------------------------------------------------------------------------------------------------------

    def verifyData(df, varNames, indexVarNames):
        pass

        # Comment the line above and uncomment the next lines if you want to verify the data being displayed:

        # Go through list of elements to make sure I get the information I need per lists (subCous) within the list
        # for varName in varNames:
        #     index = indexVarNames[varName]
        #     if __name__ == "__main__":
        #         print(df.iloc[index]) # Print rows of the variable names that I need

    verifyData(pop_df, popVarNames, indicesPopVar)

    # -----------------------------------------------------------------------------------------------------------------------

    # Set column values to NaN in the specified rows where the column value contains:
    # 1. Non-numerical values
    # 2. Values less than 0
    def cleaningData(df, indicesDict):
        indices = list(indicesDict.values())
        for index in indices:
            var_df = df.iloc[index]
            count = 0
            for col, value in var_df.items():  # Iterate through the columns and their values
                count += 1
                if count <= 2:  # Skip the first two rows (index and name)
                    continue

                try:
                    # Try to convert the value to float
                    df.at[index, col] = float(value)
                    # If the value is a negative number, set it to 0
                    if df.at[index, col] < 0:
                        df.at[index, col] = 0
                except ValueError:
                    # If it fails, set it to 0
                    df.at[index, col] = 0
        return df

    cleanedPop = cleaningData(pop_df, indicesPopVar)

    # CREATION OF DATA TO BE PRESENTED ----------------------------------------------------------------------------------------------------

    cal_file = gpd.read_file('data/Calorias por edad.xlsx')
    # Dictionary of groups by Age of calories. Key: Age group and gender, Value: Calories (float)
    calByAge = {col: round(float(cal_file[col][0]), 2) for col in cal_file.columns[3:]} 
    list_calByAge = list(calByAge.values())

    # Drop rows not in the specified indices
    relevantRows = list(indicesPopVar.values())

    malePopIndices = []
    femalePopIndices = []

    maleCals = []
    femaleCals = [] 

    for i in range(len(relevantRows)):
        if i <= 22:
            malePopIndices.append(relevantRows[i])
            maleCals.append(list_calByAge[i])
        else:
            femalePopIndices.append(relevantRows[i])
            femaleCals.append(list_calByAge[i])

    df_malePop = cleanedPop.loc[malePopIndices].reset_index(drop=True) # Dataframe of male population per Age and subBarrios
    df_femalePop = cleanedPop.loc[femalePopIndices].reset_index(drop=True) # Dataframe of female population per Age and subBarrios

    # Create deep copies of the dataframes to be able to replace each value with its multiplication with their corresponding calories
    cal_malePop = df_malePop.copy(deep=True)
    cal_femalePop = df_femalePop.copy(deep=True)

    def calSexAge(cal_list, sexAge_df):
        for index in range(len(cal_list)):
            var_df = sexAge_df.iloc[index]   
            count = 0
            for col, value in var_df.items():  # Iterate through the columns and their values
                count += 1
                if count <= 2:  # Skip the first two rows (index and name)
                    continue

                sexAge_df.at[index, col] = value * cal_list[index]
        
        return sexAge_df

    cal_malePop = calSexAge(maleCals, cal_malePop)
    cal_femalePop = calSexAge(femaleCals, cal_femalePop)

    # Deep copy the dataframe with the calories per male population
    totalCalories_df = cal_malePop.copy(deep=True)

    for index in range(len(cal_malePop)):
            var_df = totalCalories_df.iloc[index]   
            count = 0
            for col, value in var_df.items():  # Iterate through the columns and their values
                count += 1
                if count <= 2:  # Skip the first two rows (index and name)
                    continue

                totalCalories_df.at[index, col] = value + cal_femalePop.at[index, col]

    # Take only the calories to be added
    totalCalories_df = totalCalories_df.iloc[:, 2:].reset_index(drop=True)

    # Sum for each subbarrio
    result = totalCalories_df.sum()
    calorie_df = pd.DataFrame({'total_calories': result})

    # Extract the ucgids to be able to merge with the data to make the map
    ucgid = pop_df.iloc[198]

    # Take only the rows with the ucgid in them
    ucgid = ucgid.iloc[2:].reset_index(drop=True)

    # Convert to DataFrame with a proper column name
    ucgid = pd.DataFrame({'ucgid': ucgid})

    # Since the indices do not match, reset the index for calorie_df
    calorie_df = calorie_df.reset_index(drop=True)
                        
    calorie_df['ucgid'] = ucgid['ucgid']

    pop_df = pop_df.T.iloc[1:].reset_index(drop=True)

    column_with_value = pop_df.iloc[0][pop_df.iloc[0] == 'NAME']

    subCouNames = pd.DataFrame(pop_df[column_with_value.index[0]]).iloc[1:].reset_index(drop=True)

    calorie_df['NAME'] = subCouNames

    return calorie_df