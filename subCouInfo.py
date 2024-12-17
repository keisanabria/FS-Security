import geopandas as gpd

# 'subCountyInfo' contains the following: 
    # STATEFP [for PR, it is '72'], 
    # COUNTYFP, [County FIPS code]
    # GEOID,
    # GEOIDFQ [the actual GEOID that is used in URLs],
    # etc. 
subCounties = gpd.read_file("data/subCouInfo.zip")

# Save GEOIDFQs
geoidfqCol = subCounties['GEOIDFQ']
geoidfqs = geoidfqCol.tolist()

# Save GEOIDs - needed as FIPS to create the map
geoidCol = subCounties['GEOID']
geoids = geoidCol.tolist()

# print(subCounties.columns)
# print(subCounties['NAME'].iloc[0])
# print(subCounties.iloc[subCounties['COUSUBFP'] == '003'])

def getGeoids():
    return geoids

def getGeoidfqs():
    return geoidfqs