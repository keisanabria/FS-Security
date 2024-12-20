# More information about this file on Section 2.2 of README.md

import verifyFile
import pandas as pd
import cleaningData
import total_calories

households = 'data/live_data/households.csv'
verifyFile.verifyFile(households)

households_df = pd.read_csv(households)

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
# esti_insec_households = multiply_data_manually(per_insec_households, multiplier)

print(per_insec_households)
print(multiplier)