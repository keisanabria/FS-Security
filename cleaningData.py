import pandas as pd

# Set column values to NaN in the specified rows where the column value contains:
# 1. Non-numerical values
# 2. Values less than 0
def cleaningData(df, indices): 
    # indices = list of indices of the rows that you wish to look in the df
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
                # If the value is a negative number, set it to NaN
                if df.at[index, col] < 0:
                    df.at[index, col] = pd.NA
            except ValueError:
                # If it fails, set it to NaN
                df.at[index, col] = pd.NA
    return df