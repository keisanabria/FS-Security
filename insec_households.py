# More information about this file on Section 2.2 of README.md

import verifyFile
import pandas as pd
import cleaningData
import acs_year

def getInsecHouseholds():

    acsYear = acs_year.getACS_year()

    verifyFile.verifyFile(f"data/live_data/{acsYear}households.csv", 'households')

    households_df = pd.read_csv(f"data/live_data/{acsYear}households.csv")

    # Categorize the variable names accordingly
    total_households = households_df.iloc[:1].reset_index(drop=True)
    households_income = households_df.iloc[2:].reset_index(drop=True) # Number of households divided by their incomes

    # Percentages per income (disregarding the households)
    per_income = {
        'Menos de $15,000' : 0.57,
        '$15,000 a $24,999' : 0.29,
        '$25,000 a $34,999' : 0.066,
        '$35,000 o más' : 0.075
    }
    per_income_list = list(per_income.values())

    indices = [0,1,2,3,4,5,6,7,8,9] # Indices of data to be extracted from the df
    households_income = cleaningData.cleaningData(households_income, indices)

    index = [0]
    total_households = cleaningData.cleaningData(total_households, index)
    th_transposed = total_households.T

    # Initialize a DataFrame to save the data
    grouping_income = pd.DataFrame(columns=['Menos de $15,000'])

    grouping_income['Menos de $15,000'] = households_income.iloc[0] + households_income.iloc[1]
    grouping_income['$15,000 a $24,999'] = households_income.iloc[2]
    grouping_income['$25,000 a $34,999'] = households_income.iloc[3]
    grouping_income['$35,000 o más'] = households_income.iloc[4] + households_income.iloc[5] + households_income.iloc[6] + households_income.iloc[7] + households_income.iloc[8] + households_income.iloc[9]

    total_households_income = pd.DataFrame(columns=['Hogares menos de $15,000', 'Hogares $15,000 a $24,999', 'Hogares $25,000 a $34,999', 'Hogares $35,000 o más'])

    # Multiply df1 with df2
    multiplier = th_transposed.iloc[2:].reset_index(drop=True)
    grouping_income = grouping_income.iloc[2:].reset_index(drop=True)

    def multiply_data_manually(grouping_income, multiplier):
        # Ensure multiplier is a 1D Series by selecting the appropriate column or row
        if isinstance(multiplier, pd.DataFrame):
            # Select the first column (or another column) if multiplier is a DataFrame
            multiplier = multiplier.iloc[:, 0]  # Select the first column
        
        # Ensure multiplier is a pandas Series (if not already)
        if not isinstance(multiplier, pd.Series):
            raise ValueError("Multiplier should be a pandas Series or a 1D array-like object.")

        # Make sure both DataFrames have the same number of rows
        if len(grouping_income) != len(multiplier):
            raise ValueError("The number of rows in both dataframes must be the same.")

        # Create an empty DataFrame to store results
        result = pd.DataFrame(index=grouping_income.index, columns=grouping_income.columns)

        # Loop through each row and multiply the values
        for idx, row in grouping_income.iterrows():
            result.loc[idx] = row * multiplier[idx]  # Multiply each row with the corresponding multiplier value
        
        return result

    # Assuming grouping_income is a DataFrame and multiplier is a pandas Series or 1D array-like
    result = multiply_data_manually(grouping_income, multiplier)

    def multiply_elements_with_columns(df, multipliers):
        # Ensure the multipliers are a pandas Series (1D array-like)
        if not isinstance(multipliers, pd.Series):
            multipliers = pd.Series(multipliers)
        
        # Check if the number of multipliers matches the number of columns in the DataFrame
        if len(multipliers) != df.shape[1]:
            raise ValueError("The number of multipliers must match the number of columns in the DataFrame.")
        
        # Perform element-wise multiplication across columns
        result = df * multipliers.values
        
        return result

    result = multiply_elements_with_columns(grouping_income, per_income_list)

    per_insec_households = result['Menos de $15,000'] + result['$15,000 a $24,999'] + result['$25,000 a $34,999'] + result['$35,000 o más']

    per_insec_households_df = pd.DataFrame({'per_insec_households': per_insec_households}) # Create a df so that it can be multiplied with the multiplier since it was previously a Series
    esti_insec_households = multiply_data_manually(per_insec_households_df, multiplier)

    # Finished creating the relevant data needed, which are taken from: per_insec_households_df and esti_insec_households

    # Extract the ucgids to be able to merge with the data to make the map
    ucgid = households_df.iloc[12]

    # Take only the rows with the ucgid in them
    ucgid = ucgid.iloc[2:].reset_index(drop=True)

    # Convert to DataFrame with a proper column name
    ucgid = pd.DataFrame({'ucgid': ucgid})

    # Since the indices do not match, reset the index for result_df
    per_insec_households_df = per_insec_households_df.reset_index(drop=True)

    # Add the estimate of households into one df
    per_insec_households_df['esti_insec_households'] = esti_insec_households['per_insec_households']

    # Do the same with the ucgid
    per_insec_households_df['ucgid'] = ucgid['ucgid']

    # Rename the df to make more sense
    insec_households = per_insec_households_df

    # Opt-in to future behavior and suppress "FutureWarning: Downcasting object dtype arrays on .fillna, .ffill, .bfill is deprecated and will change in a future version."
    pd.set_option('future.no_silent_downcasting', True)

    # Replace null values within esti_insec_households and per_insec_households as to not create an error when creating the map
    insec_households = insec_households.infer_objects()  # Convert columns with object dtype to their appropriate types
    insec_households['esti_insec_households'] = insec_households['esti_insec_households'].fillna(0)
    insec_households['per_insec_households'] = insec_households['per_insec_households'].fillna(0)

    # Created a variable called 'insec_households' which will hold all the data needed to (...)
    # (...) make maps of percentage of households with food insecurity and estimate of households with food insecurity  

    return insec_households