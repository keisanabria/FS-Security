import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import mapclassify
from total_calories import totalCalories_df

# Variables
dimensions = gpd.read_file("data/dimensions/tl_2022_72_cousub.zip") # Dimensions of Puerto Rico
food = gpd.read_file("data/food/inseguridad por barrio 2022 data.xlsx") # Information of Food Security of Puerto Rico

# Filter the shapefile to include only land areas (ALAND > 0)
land_only = dimensions[dimensions['ALAND'] > 0]

# Save the filtered data to a new shapefile
output_path = "data/dimensions/filtered_land_coordinates.shp"
land_only.to_file(output_path)
dimensions = gpd.read_file(output_path)

# Sort the dimensions to be according to the GEOID in ascending order so that the GEOIDs are in the same order as the Excel sheet
geoID_sorted = dimensions.sort_values(by='GEOID', ascending=True)
dimensions = geoID_sorted

# This is just pre-modifications made for the information to go on par with the Excel sheet
def preMods(dimensions, food):
    # Rename column that has GEOID from "food" to be used as a common key
    food = food.rename(columns = { "GEOID,C,10" : "GEOID"})

    # Cambiar "dimensions" data type to int64
    dimensions["GEOID"] = dimensions["GEOID"].astype('int64')

    # Perform an inner merge to keep only matching rows
    merge = food.merge(dimensions, on=['GEOID'], how='inner')

    # Convert the result back to a GeoDataFrame, using the geometry from dimensions
    merge = gpd.GeoDataFrame(merge, geometry=dimensions.geometry)

    # Change the name of the subbarrios for the 'merge' gpd because they are written incorrectly in the Excel sheet
    merge['NAME,C,100'] = dimensions['NAME']

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
    # Define the hex colors for the legend
    legend_colors = ['#ffffe5', '#f7fcb9', '#d9f0a3', '#addd8e', '#78c679', '#41ab5d', '#238443', '#005a32']
    
    # Create a figure and axes for custom size
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))  # Adjust 'figsize' for map size in the saved image

    # Create the map and color it according to the 'quantile_class' column
    PRmap = merge.assign(cl=q8.yb).plot(
        column="cl", 
        categorical=True, 
        cmap=plt.cm.get_cmap('YlGn', len(legend_colors)),  # Create a colormap with the exact number of colors
        legend=False,  # Turn off the default legend
        linewidth=1.1,
        edgecolor='black',
        ax=ax  # Use the custom axes
    )

    # Create a custom legend with the specified color patches
    legend_handles = []
    for i, label in enumerate(q8.get_legend_classes()):
        # Use the corresponding hex color for each quantile class
        color = legend_colors[i]
        patch = mpatches.Patch(color=color, label=label)  # Create a patch with the corresponding color
        legend_handles.append(patch)

    # Add the custom legend beside the map
    legend = ax.legend(
        handles=legend_handles,  # Use the custom color patches
        loc="upper left",  # Legend location
        bbox_to_anchor=(1, 1),  # Position beside the map
        title="Food Security Classes",  # Add a title for the legend
        frameon=False  # Optional: remove the legend box frame
    )

    # Save the figure as a PNG file with custom DPI for output resolution
    plt.savefig("assets/2022map.png", format="png", dpi=300, bbox_inches='tight')  # dpi controls image resolution

    # Uncomment this when wanting to display the plot (Testing purposes)
    # plt.show()