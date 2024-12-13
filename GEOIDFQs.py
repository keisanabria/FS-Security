from mapCreation import gpd

# 'subCountyInfo' contains the following: 
    # STATEFP [for PR, it is '72'], 
    # COUNTYFP,
    # GEOID,
    # GEOIDFQ [the actual GEOID that is used in URLs],
    # etc. 
subCounties = gpd.read_file("data/subCouInfo.zip")

# Save GEOIDFQs
values = subCounties['GEOIDFQ']
geoidfqs = values.tolist()