import geopandas as gpd
import plotly.express as px
import mapclassify
import numpy as np
import pandas as pd
import json

# Variables
dimensions = gpd.read_file("data/dimensions/tl_2022_72_cousub.zip") # Dimensions of Puerto Rico
food = gpd.read_file("data/food/inseguridad por barrio 2022 data.xlsx") # Information of Food Security of Puerto Rico

# Sort the dimensions to be according to the GEOID in ascending order
geoID_sorted = dimensions.sort_values(by='GEOID', ascending=True)
dimensions = geoID_sorted

def preMods(dimensions, food):
    # Rename column that has GEOID from "food" to be used as a common key
    food = food.rename(columns = { "GEOID,C,10" : "GEOID"})

    # Cambiar "dimensions" data type to int64
    dimensions["GEOID"] = dimensions["GEOID"].astype('int64')

    # Merge con GEOID as the common key
    merge = food.merge(dimensions, on=["GEOID"], how="left")

    # Convert the result back to a GeoDataFrame, using the geometry from dimensions
    merge = gpd.GeoDataFrame(merge, geometry=dimensions.geometry)

    # Change the name of the subbarrios for the 'merge' gpd because they are written incorrectly in the Excel sheet
    merge['NAME,C,100'] = dimensions['NAME']

    return merge

merge = preMods(dimensions, food)

# TESTING PURPOSES
# ----------------------------------------------------------------------------
merge['STATE&COUNTYFP'] = dimensions['STATEFP'] + dimensions['COUNTYFP']
merge['COUSUBFP'] = dimensions['COUSUBFP']
merge['COUNTYFP'] = dimensions['COUNTYFP']
merge['NAME'] = dimensions['COUSUBFP']+'-'+dimensions['NAME']
# Changed line 82,100
# ----------------------------------------------------------------------------

# Classify the percentages in 8 quantiles
q8 = mapclassify.Quantiles(merge['isec_percentage_hosedolds'], k=8)
merge['quantile_class'] = q8.yb # Add quantile classes to the GeoDataFrame 

# Shade for each quantile class (8)
colorscale = [[0, '#98FF98'],[1, '#98FB98'],[2, '#90EE90'],[3, '#3CB371'],[4, '#228B22'],[5, '#556B2F'],[6, '#006400'],[7, '#013220']]

# Assign a color to each row in merge['color'] based on quantile_class
merge['color'] = merge['quantile_class'].apply(lambda x: colorscale[x])

endpts = list(np.linspace(0, q8.bins[len(q8.bins)-1], len(colorscale) - 1))
values = merge['isec_percentage_hosedolds'].astype(int).tolist()

# Convert GEOID in merge to string for consistency with GeoJSON
merge['GEOID'] = merge['GEOID'].astype(str)

# Convert to WGS84 CRS for compatibility
merge = merge.to_crs(epsg=4326)

# Creating a GeoJSON structure for specific regions
geojson_data = {
    "type": "FeatureCollection",
    "features": []
}

# Since the data of geoid will be extracted from the CENSUS API, (...)
# (...) the GEOID in "properties" of the geojson will eventually be changed to this
import subCouInfo
geoids = subCouInfo.getGeoids()

# Loop through each region and add it to the GeoJSON structure
for index, row in merge.iterrows():
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": row['geometry'].__geo_interface__['coordinates']
        },
        "properties": {
            "GEOID": str(row['COUSUBFP']),
            "name": row['NAME'],
            "food_insecurity": row['isec_percentage_hosedolds'],
            "color": row['color']
        }
    }
    geojson_data["features"].append(feature)

# Write GeoJSON to a file
with open("data/dimensions/mapInfo.geojson", "w") as f:
    json.dump(geojson_data, f)

# print(colorscale)
# print(merge['color'])
# print(merge['quantile_class'])

def createMap():
    
    # Create a DataFrame from geoids, values, and quantile classes
    df = pd.DataFrame({
        'geoid': merge['COUSUBFP'],
        'value': values,
        'quantile_class': merge['quantile_class'],
        'color' : merge['color'],
        'name' : merge['NAME']
    })

    # color_map = {
    #     values : merge['color']
    # }
    
    # Create choropleth map
    fig = px.choropleth(
        data_frame=df, 
        geojson=geojson_data,  # Path to GeoJSON for Puerto Rico regions
        locations='geoid',  # The column from df that contains the geoids
        # locationmode='geojson-id',
        # lat=18.2208,
        # lon=-66.5901,
        featureidkey="properties.geoid",
        color="value", # Changed to int64 for testing purposes
        # colorscale=colorscale,
        # autocolorscale=False,
        # color_continuous_scale="Greens",
        # color_discrete_sequence=colorscale,  # Set a discrete green color scale
        projection='mercator',
        range_color=[df['value'].min(), df['value'].max()]
        # center = {"lat": 18.2208, "lon": -66.5901}, # Puerto Rico's longitude and latitude
        # title="Test",  # Title for the map
        # labels={'value': 'Test values'}  # Set legend label for the values
    )
    
    # Adjust layout and show the map
    fig.update_geos(
        fitbounds="locations", 
        visible=False
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # Show the figure
    fig.show()