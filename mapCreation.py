import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import mapclassify
from subCouInfo import geoidfqCol
import acs_year

# Variables
dimensions = gpd.read_file("data/dimensions/tl_2022_72_cousub.zip") # Dimensions of Puerto Rico
# food = gpd.read_file("data/food/inseguridad por barrio 2022 data.xlsx") # Information of Food Security of Puerto Rico

# Add GEOIDFQs to dimensions to be able to merge with data
dimensions['ucgid'] = geoidfqCol

# Filter the shapefile to include only land areas (ALAND > 0)
land_only = dimensions[dimensions['ALAND'] > 0]

# Save the filtered data to a new shapefile
output_path = "data/dimensions/filtered_land_coordinates.shp"
land_only.to_file(output_path)
dimensions = gpd.read_file(output_path)

# According to the data given, create the map and the title
def createMap(mapName, data):

    # Perform an inner merge to keep only matching rows
    merge = data.merge(dimensions, on=['ucgid'], how='inner')

    # Convert the result back to a GeoDataFrame, using the geometry from dimensions
    merge = gpd.GeoDataFrame(merge, geometry=dimensions.geometry)

    # Classify the percentages in 8 quantiles
    q8 = mapclassify.Quantiles(merge[mapName], k=8)

    # Create the mapping for the legend
    mapping = dict([(i, s) for i, s in enumerate(q8.get_legend_classes())])

    # Replace the default legend items to Quantiles of 8 classes
    def replace_legend_items(legend, mapping):
        if legend:
            for txt in legend.texts:
                for k, v in mapping.items():
                    if txt.get_text() == str(k):
                        txt.set_text(v)

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
        title=mapName,  # Add a title for the legend
        frameon=False  # Optional: remove the legend box frame
    )

    acsYear = str(acs_year.getACS_year())

    # Save the figure as a PNG file with custom DPI for output resolution
    plt.savefig(f"assets/{acsYear}map.png", format="png", dpi=300, bbox_inches='tight')  # dpi controls image resolution

    # Uncomment this when wanting to display the plot (Testing purposes)
    # plt.show()