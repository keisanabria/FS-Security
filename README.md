# FS-Security

## Section 1

### STEPS ON HOW TO ACCESS CENSUS API [2]:
1. Get access to a key (request a key)
2. [...]

### TO-DO:
<!-- 1. LOW - Change the size of the edges of the map for it to be thin around the map -->
* !!! Haven't reorganized the number of steps because step 4 and maybe others rely on the number of the steps
2. HIGH - Get the data that is supposed to be in the map (URLs, keys, etc.)
3. Make the data that is being extracted for the map to update progressively as the years come and take the data from the years before (check if there is a better method to do this than having to save the information to a csv file because it will take a lot of data as the years come)
    * One method is explained in the last two responses of ChatGPT [5].

        * Make sure to check that the data for that year is available and THEN update the map according to that
            - This might be able to be done with the following (provided by ChatGPT [5]):
                ```response = requests.get(base_url, params=params)
                        if response.status_code == 200:
                            return response.json()
                        else:
                            raise Exception(f"Error {response.status_code}: {response.text}")```

        * Make sure that for the step of updating according to the release date is scheduled according to the following website: https://www.census.gov/programs-surveys/acs/news/data-releases/2021/release-schedule.html

4. Make the map interactive so that it updates the map according to the data extracted from step 3
5. HIGH - Pass the maps to Wordpress. More information about this on reference link [6]
6. AFTER - Fix README.md to be readable in GitHub
7. LOW - Verify if .venv can be activated when the user runs the program so that it can run smoothly
8. LOW - Change this line (gdf.to_file("data/dimensions/geometry.geojson", driver="GeoJSON") # Export to GeoJSON) in mapCreation.py to check if that file exists. If it does, then don't recreate it.
9. HIGH - Put an order of which modules have to be executed so that the map can be created
    mapCreation.py > main.py
    imageListGenerator.py > dashInteraction.py

Recommended by Ouslam:
*   Read: 158 a 172 lines of https://github.com/ouslan/mov/blob/main/src/data/data_pull.py
    - Note: The key in line 172 is not neccesary

Priority of tasks: 
- LOW - Not required, but a preference
- HIGH - Must be done and it takes a lot of effort to complete
- AFTER - Task to be done after finishing the project

### In progress:
- Check how to pass what is being hosted on Dash to Wordpress
    * Uninstall the libraries I don't need anymore and put back the ones I was using before
- Change total calories population information to be taken from (https://data.census.gov/table/ACSDT5Y2023.B01001?q=B01001:%20Sex%20by%20Age&g=040XX00US72$0600000) instead. So as to not do Section 2.2.
- Construct the code that will implement the json url links to come to have it set up antes de implementing the data
    * mapCreation will be called by a function where the user chooses what map to show up 
- Change total_calories' last code block to start from the first line intead of the name of the variable
- Implement the data into the map

Personal notes:
API User Guide [1] - Guidelines
    - Page 22 is to guide on use of UCGID
    - Page 16 includes instructions of the last step on how to handle the URL of the API
- Page 35-36 [2] contains information of all the common ACS API Variables
- Total population group name: P1_001N
- Reference [7] gave a lot of details about how to work with Dash when the image does not show.

### Requirements
- Have python 3.12.5+
- Install geopandas, mapclassify, requests, pandas, pathlib, plotly*, shapely*, plotly-geo*, pyshp*, dash, json, openpyxl*
    * Libraries with asterik were only installed for the Plotly map, which currently won't be used

### Command to activate .venv - for a smoother run experience
$.venv/Scripts/activate 

### Requirements for Windows when activating .venv 
- Run $Set-ExecutionPolicy Unrestricted -Scope Process

Note: To run this code, it is recommended to install and activate .venv for a smoother run of the program

<!-- References -->
[1] https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-user-guide.pdf
[2] https://www2.census.gov/about/training-workshops/2020/2020-07-22-cedsci-presentation.pdf
[3] https://portal.nifa.usda.gov/web/crisprojectpages/1029124-food-security-and-agricultural-research-data-center.html 
[4] https://data.census.gov/table/ACSDP5Y2023.DP05?q=DP05:%20ACS%20Demographic%20and%20Housing%20Estimates&g=040XX00US72$0600000 
[5] https://chatgpt.com/share/675f46fe-9334-8011-aba7-b02d3ffad84a (Chat named: Sorting GeoDataFrame Column)
[6] https://chatgpt.com/share/675f4648-ca64-8011-8120-ee3d45e2ef63 (Chat named: Display Map from GitHub)
[7] https://chatgpt.com/share/67630cf7-12b8-8011-a192-5ba70e7abe4c

## Section 2

### Section 2.1
Variable names that are being used for the population:
1. DP05_0005E	Estimate!!SEX AND AGE!!Total population!!Under 5 years
2. DP05_0006E	Estimate!!SEX AND AGE!!Total population!!5 to 9 years
3. DP05_0007E	Estimate!!SEX AND AGE!!Total population!!10 to 14 years
4. DP05_0008E	Estimate!!SEX AND AGE!!Total population!!15 to 19 years
5. DP05_0009E	Estimate!!SEX AND AGE!!Total population!!20 to 24 years
6. DP05_0010E	Estimate!!SEX AND AGE!!Total population!!25 to 34 years
7. DP05_0011E	Estimate!!SEX AND AGE!!Total population!!35 to 44 years
8. DP05_0012E	Estimate!!SEX AND AGE!!Total population!!45 to 54 years
9. DP05_0013E	Estimate!!SEX AND AGE!!Total population!!55 to 59 years
10. DP05_0014E	Estimate!!SEX AND AGE!!Total population!!60 to 64 years
11. DP05_0015E	Estimate!!SEX AND AGE!!Total population!!65 to 74 years
12. DP05_0016E	Estimate!!SEX AND AGE!!Total population!!75 to 84 years
13. DP05_0017E	Estimate!!SEX AND AGE!!Total population!!85 years and over
14. DP05_0002PE	Percent!!SEX AND AGE!!Total population!!Male
15. DP05_0003PE	Percent!!SEX AND AGE!!Total population!!Female

### Section 2.2
Hubieron cambios que se tuvieron que hacer para que la poblacion por edad cayera dentro de los generos porque esta data no se encuentra en
el CENSUS API [4]. Los cambios que se hicieron en los pasos que proveyo el profesor fue anadir un paso extra:
    Numero de hombres en X rango de edades = Poblacion en X rango de edades * (Porcentaje de hombres/100)
    Numero de feminas en X rango de edades = Poblacion en X rango de edades * (Porcentaje de feminas/100)

## Information on syntaxes:

### Geopandas
.columns = returns df's columns
.rows = returns df's rows

### Python
- if __name__ == "__main__":
    This is used to prevent a code block from being executed when importing that code block's module to another module.