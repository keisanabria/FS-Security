
from .data_pull import DataPull
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

    def pr_map(self):
        pass
