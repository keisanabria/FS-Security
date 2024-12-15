# FS-Security

## Section 1

### STEPS ON HOW TO ACCESS CENSUS API [2]:
1. Get access to a key (request a key)
2. [...]

### TO-DO:
1. LOW - Change the size of the edges of the map for it to be thin around the map
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
5. HIGH - Pass the maps to Wordpress
6. AFTER - Fix README.md to be readable in GitHub

Recommended by Ouslam:
*   Read: 158 a 172 lines of https://github.com/ouslan/mov/blob/main/src/data/data_pull.py
    - Note: The key in line 172 is not neccesary

Priority of tasks: 
- LOW - Not required, but a preference
- HIGH - Must be done and it takes a lot of effort to complete
- AFTER - Task to be done after finishing the project

### In progress:
- Check how to get the results of the variables that I need for the gender of calories (printing the list)
- Verify that the code to be implemented into Wordpress won't required for me to change anything within my Python code
    * I have an idea that it will be pulled from my GitHub repository
    * Search this up on ChatGPT for a quick checkup
- Construct the code that will implement the json url links to come to have it set up antes de implementing the data

Personal notes:
API User Guide [1] - Guidelines
    - Page 22 is to guide on use of UCGID
    - Page 16 includes instructions of the last step on how to handle the URL of the API
- Page 35-36 [2] contains information of all the common ACS API Variables
- Total population group name: P1_001N

### Requirements
- Have python 3.12.5
- Install geopandas, matplotlib, mapclassify, requests

### Requirements for Windows when activating .venv 
- Run $Set-ExecutionPolicy Unrestricted -Scope Process

Note: To run this code, it is recommended to install and activate .venv for a smoother run of the program

<!-- References -->
[1] https://www.census.gov/content/dam/Census/data/developers/api-user-guide/api-user-guide.pdf
[2] https://www2.census.gov/about/training-workshops/2020/2020-07-22-cedsci-presentation.pdf
[3] https://portal.nifa.usda.gov/web/crisprojectpages/1029124-food-security-and-agricultural-research-data-center.html 
[4] https://data.census.gov/table/ACSDP5Y2023.DP05?q=DP05:%20ACS%20Demographic%20and%20Housing%20Estimates&g=040XX00US72$0600000 
[5] https://chatgpt.com/c/67059f1b-90dc-8011-a7c0-cf5c2501c251 (Chat named: Sorting GeoDataFrame Column)

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
- DP05_0002PE	Percent!!SEX AND AGE!!Total population!!Male
- DP05_0003PE	Percent!!SEX AND AGE!!Total population!!Female

### Section 2.2
Hubieron cambios que se tuvieron que hacer para que la poblacion por edad cayera dentro de los generos porque esta data no se encuentra en
el CENSUS API [4]. Los cambios que se hicieron en los pasos que proveyo el profesor fue anadir un paso extra:
    Numero de hombres en X rango de edades = Poblacion en X rango de edades * (Porcentaje de hombres/100)
    Numero de feminas en X rango de edades = Poblacion en X rango de edades * (Porcentaje de feminas/100)