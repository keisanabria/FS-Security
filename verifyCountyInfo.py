from mapCreation import gpd

# 'countyInfo' contains the following: 
    # STATEFP [for PR, it is '72'], 
    # COUNTYFP,
    # GEOID,
    # GEOIDFQ [the actual GEOID that is used in URLs],
    # etc. 
counties = gpd.read_file("data/countyInfo.zip")

indexPRcounties = [   5,   80,  204,  255,  259,  278,  381,  408,  409,  427,  430,  463,
        476,  486,  508,  529,  539,  541,  875,  904,  905,  928,  956,  966,
        970, 1100, 1102, 1144, 1182, 1202, 1239, 1282, 1320, 1405, 1406, 1407,
       1439, 1440, 1500, 1517, 1542, 1543, 1570, 1646, 1667, 1773, 1786, 1794,
       1802, 1884, 1885, 1905, 1984, 2122, 2162, 2220, 2278, 2294, 2305, 2362,
       2364, 2365, 2387, 2448, 2462, 2499, 2567, 2568, 2573, 2589, 2701, 2715,
       2716, 2754, 2787, 2831, 2832, 3015]

    # To check where county '147' is mentioned
# indices = counties[counties['COUNTYFP'] == '147'].index
# print(indices)

    # Print all the lines where 'STATEFP' is '72' [Puerto Rico]
# print(counties[counties['STATEFP'] == '72'].index)

    # Print a row
# print(counties.loc[80])

    # Check if a specific value exists in the column 'your_column'
# value_to_find = 12345  # Replace with your value
# exists = value_to_find in gdf['your_column'].values
# print(f"Exists: {exists}")