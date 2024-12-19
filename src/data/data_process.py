from .data_pull import DataPull
import plotly.express as px
import geopandas as gpd
import pandas as pd
import os

class DataGeo(DataPull):

    def __init__(self, saving_dir:str="data/", debug:bool=False) -> None:
        super().__init__(saving_dir=saving_dir, debug=debug)

        # Check if the required data files exist
        if not os.path.exists(f"{self.saving_dir}external/cousub.zip"):
            self.pull_file(url="https://www2.census.gov/geo/tiger/TIGER2024/COUSUB/tl_2024_72_cousub.zip", filename=f"{self.saving_dir}external/cousub.zip")
            self.debug_log("county.zip downloaded")

    def pr_cousub(self) -> gpd.GeoDataFrame:
        gdf = gpd.read_file(f"{self.saving_dir}external/cousub.zip")
        gdf = gdf[gdf["ALAND"] > 0]
        gdf = gdf[["GEOID", "NAME", "geometry"]]
        return gdf

    def pr_food(self) -> pd.DataFrame:
        df = pd.read_excel(f"{self.saving_dir}raw/food_access.xlsx")
        df = df.rename(columns = { "GEOID,C,10" : "GEOID"})
        df = df.drop(["NAME,C,100","barrio", "order"], axis=1)
        df["GEOID"] = df["GEOID"].astype(str)
        return df

    def pr_merge(self) -> gpd.GeoDataFrame:
        cousub = self.pr_cousub()
        food = self.pr_food()
        food = food.merge(cousub, on="GEOID", how="inner", validate="1:1")
        food = gpd.GeoDataFrame(food, geometry="geometry")
        return food

    def pr_map(self) -> px.choropleth_mapbox:
        gdf = self.pr_merge()
        fig = px.choropleth_map(gdf, geojson=gdf.geometry, locations=gdf.index, color='total_calories',
                           color_continuous_scale="Viridis",
                           map_style="carto-positron",
                           range_color=(0,10**7),
                           labels={'total_calories':'Total Calaries'},
                           center={"lat": 18.2606, "lon": -66.3962},
                           zoom=7.5)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        return fig
