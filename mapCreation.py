import geopandas as gpd
import matplotlib.pyplot as plt
import mapclassify

# Variables
dimensions = gpd.read_file("data/dimensions/tl_2022_72_cousub.zip") # Dimensions of Puerto Rico
food = gpd.read_file("data/food/inseguridad por barrio 2022 data.xlsx") # Information of Food Security of Puerto Rico

def preMods(dimensions, food):
    # Sort the Geographic IDs in ascending order
    geoID_sorted = dimensions.sort_values(by='GEOID', ascending=True) 

    # Rename column that has GEOID from "food" to be used as a common key
    food = food.rename(columns = { "GEOID,C,10" : "GEOID"})

    # Cambiar "dimensions" data type to int64
    dimensions["GEOID"] = dimensions["GEOID"].astype('int64')

    # Merge con GEOID as the common key
    merge = food.merge(dimensions, on=["GEOID"], how="left")

    # Convert the result back to a GeoDataFrame, using the geometry from dimensions
    merge = gpd.GeoDataFrame(merge, geometry=dimensions.geometry)

    return merge

merge = preMods(dimensions, food)

# Classify the percentages in 8 quantiles
q8 = mapclassify.Quantiles(merge['isec_percentage_hosedolds'], k=8)

# Create the mapping for the legend
mapping = dict([(i, s) for i, s in enumerate(q8.get_legend_classes())])

# Replace the default legend items to Quantiles of 8 classes
def replace_legend_items(legend, mapping):
    if legend:
        for txt in legend.texts:
            for k, v in mapping.items():
                if txt.get_text() == str(k):
                    txt.set_text(v)

# ----------------------------------------------------------------------------------------------

# Space reserved for code of the interaction with CENSUS API

# ----------------------------------------------------------------------------------------------

def createMap():
    # Create the map and color it according to the 'quantile_class' column
    PRmap = merge.assign(cl=q8.yb).plot(
        column = "cl", 
        categorical = True, 
        cmap='Greens', 
        legend=True)
    
    # Replace the legend items with the custom mapping
    replace_legend_items(PRmap.get_legend(), mapping)
    
    plt.show()