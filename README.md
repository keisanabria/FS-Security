# FS-Security

## Section 1

<!-- STEPS ON HOW TO ACCESS CENSUS API [2] -->
1. Get access to a key (request a key)
2. 

<!-- TO DO -->
1. LOW - Change the size of the edges of the map for it to be thin around the map
2. HIGH - Get the data that is supposed to be in the map (URLs, keys, etc.)
3. Make the data that is being extracted for the map to update progressively as the years come
4. Make the map interactive so that it updates the map according to the data extracted from step 3
5. HIGH - Pass the maps to Wordpress

Recmmended by Ouslam:
*   Read: 158 a 172 lines of https://github.com/ouslan/mov/blob/main/src/data/data_pull.py
    Note: The key in line 172 is not neccesary

Priority of tasks: 
LOW - Not required, but a preference
HIGH - Must be done and it takes a lot of effort to complete

<!-- In progress -->
- In step 2, doing Total_Calories of the steps that professor sent me through e-mail and annotations I made
    * Agrupando los grupos de calorias en los age intervals (Me quede verificando la respuesta de ChatGPT para saber si hacer el promedio de las calorias o buscar
    otro approach que sea mas exacto [if just to sumar las calorias])
    * Verificando los nombres de variables en Section 2.1 para ver cuales son de hombres y mujeres para cada county subdivision

Personal notes:
API User Guide [1] - Guidelines
    - Page 22 is to guide on use of UCGID
    - Page 16 includes instructions of the last step on how to handle the URL of the API
- Page 35-36 [2] contains information of all the common ACS API Variables
- Total population group name: P1_001N

<!-- Requirements -->
- Have python 3.12.5
- Install geopandas, matplotlib, mapclassify, requests

<!-- Requirements for Windows when activating .venv  -->
- Run $Set-ExecutionPolicy Unrestricted -Scope Process

Note: To run this code, it is recommended to install and activate .venv for a smoother run of the program

<!-- References -->
[1] https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-user-guide.pdf
[2] https://www2.census.gov/about/training-workshops/2020/2020-07-22-cedsci-presentation.pdf
[3] https://portal.nifa.usda.gov/web/crisprojectpages/1029124-food-security-and-agricultural-research-data-center.html 

## Section 2

### Section 2.1
Variable names that are being used for the population:
- DP05_0005E	Estimate!!SEX AND AGE!!Total population!!Under 5 years
- DP05_0006E	Estimate!!SEX AND AGE!!Total population!!5 to 9 years
- DP05_0007E	Estimate!!SEX AND AGE!!Total population!!10 to 14 years
- DP05_0008E	Estimate!!SEX AND AGE!!Total population!!15 to 19 years
- DP05_0009E	Estimate!!SEX AND AGE!!Total population!!20 to 24 years
- DP05_0010E	Estimate!!SEX AND AGE!!Total population!!25 to 34 years
- DP05_0011E	Estimate!!SEX AND AGE!!Total population!!35 to 44 years
- DP05_0012E	Estimate!!SEX AND AGE!!Total population!!45 to 54 years
- DP05_0013E	Estimate!!SEX AND AGE!!Total population!!55 to 59 years
- DP05_0014E	Estimate!!SEX AND AGE!!Total population!!60 to 64 years
- DP05_0015E	Estimate!!SEX AND AGE!!Total population!!65 to 74 years
- DP05_0016E	Estimate!!SEX AND AGE!!Total population!!75 to 84 years
- DP05_0017E	Estimate!!SEX AND AGE!!Total population!!85 years and over