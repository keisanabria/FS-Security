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

        * Create a function that calls the createMap function according to the new updated data

4. Make the map interactive so that it updates the map according to the data extracted from step 3
5. HIGH - Pass the maps to Wordpress. More information about this on reference link [6]
6. AFTER - Fix README.md to be readable in GitHub
7. LOW - Verify if .venv can be activated when the user runs the program so that it can run smoothly
8. LOW - Change this line (gdf.to_file("data/dimensions/geometry.geojson", driver="GeoJSON") # Export to GeoJSON) in mapCreation.py to check if that file exists. If it does, then don't recreate it.
9. HIGH - Put an order of which modules have to be executed so that the map can be created
    mapCreation.py > main.py
    imageListGenerator.py > dashInteraction.py
10. HIGH - Change the buttons of the Dash app to show the years of the map on the button-dropdown
11. HIGH - Change this to make the csv according to the year (e.g. '2023perPerSubCou')
12. Create collapse of data from total_calories [8]
13. Personalize the toml files from Ouslam's branch
14. DUMP - Remove the verifyFile() , cleaningData() from total_calories.py since a module for the same function was created

Recommended by Ouslam:
*   Read: 158 a 172 lines of https://github.com/ouslan/mov/blob/main/src/data/data_pull.py
    - Note: The key in line 172 is not neccesary

Priority of tasks: 
- LOW - Not required, but a preference
- HIGH - Must be done and it takes a lot of effort to complete
- AFTER - Task to be done after finishing the project
- DUMP - To reduce space

### In progress:
- Implement the data into the map to verify it is being extracted correctly
    * Change the names of the columns from insec_households results (one of them can be changed in line 90)
    * Add both columns so that they are all together with the ucgid
- Implement the functions needed to make the map update periodically

Personal notes:
API User Guide [1] - Guidelines
    - Page 22 is to guide on use of UCGID
    - Page 16 includes instructions of the last step on how to handle the URL of the API
- Page 35-36 [2] contains information of all the common ACS API Variables
- Total population group name: P1_001N
- Reference [7] gave a lot of details about how to work with Dash when the image does not show.
- Other ways to host an app, other than Render.com:
    * https://www.reddit.com/r/datascience/comments/rwrfmk/deploy_dash_app_for_free/
    * https://www.pythonanywhere.com/
    * Simply search up "how to host dash app for free"
- How to refresh the requirements.txt whenever a library is installed
    $pip freeze > requirements.txt

### Requirements
- Have python 3.12.5+
- Install geopandas, mapclassify, requests, pandas, pathlib, plotly, shapely, plotly-geo*, pyshp*, dash, json, openpyxl*, gunicorn
    * Libraries with asterik were only installed for the Plotly map, which currently won't be used

### How to install dependencies (libraries)
1. Use the following command in a new environment (e.g. .venv) to install all the dependencies listed in the file:
    $pip install -r requirements.txt

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
[8] https://outlook.office.com/mail/id/AAQkADg3ODZlNWM3LTM3ZTItNGUyOS05MDI1LTJmYTU4NGVlZTY4ZQAQAL81162xZvlEiasxtrIs%2F1w%3D 

## Section 2

### Section 2.1
Variable names that are being used for the population:
1. B01001_003E	Estimate!!Total:!!Male:!!Under 5 years
2. B01001_004E	Estimate!!Total:!!Male:!!5 to 9 years
3. B01001_005E	Estimate!!Total:!!Male:!!10 to 14 years
4. B01001_006E	Estimate!!Total:!!Male:!!15 to 17 years
5. B01001_007E	Estimate!!Total:!!Male:!!18 and 19 years
6. B01001_008E	Estimate!!Total:!!Male:!!20 years
7. B01001_009E	Estimate!!Total:!!Male:!!21 years
8. B01001_010E	Estimate!!Total:!!Male:!!22 to 24 years
9. B01001_011E	Estimate!!Total:!!Male:!!25 to 29 years
10. B01001_012E	Estimate!!Total:!!Male:!!30 to 34 years
11. B01001_013E	Estimate!!Total:!!Male:!!35 to 39 years
12. B01001_014E	Estimate!!Total:!!Male:!!40 to 44 years
13. B01001_015E	Estimate!!Total:!!Male:!!45 to 49 years
14. B01001_016E	Estimate!!Total:!!Male:!!50 to 54 years
15. B01001_017E	Estimate!!Total:!!Male:!!55 to 59 years
16. B01001_018E	Estimate!!Total:!!Male:!!60 and 61 years
17. B01001_019E	Estimate!!Total:!!Male:!!62 to 64 years
18. B01001_020E	Estimate!!Total:!!Male:!!65 and 66 years
19. B01001_021E	Estimate!!Total:!!Male:!!67 to 69 years
20. B01001_022E	Estimate!!Total:!!Male:!!70 to 74 years
21. B01001_023E	Estimate!!Total:!!Male:!!75 to 79 years
22. B01001_024E	Estimate!!Total:!!Male:!!80 to 84 years
23. B01001_025E	Estimate!!Total:!!Male:!!85 years and over
------------------------------------------------------------
24. B01001_027E	Estimate!!Total:!!Female:!!Under 5 years
25. B01001_028E	Estimate!!Total:!!Female:!!5 to 9 years
26. B01001_029E	Estimate!!Total:!!Female:!!10 to 14 years
27. B01001_030E	Estimate!!Total:!!Female:!!15 to 17 years
28. B01001_031E	Estimate!!Total:!!Female:!!18 and 19 years
29. B01001_032E	Estimate!!Total:!!Female:!!20 years
30. B01001_033E	Estimate!!Total:!!Female:!!21 years
31. B01001_034E	Estimate!!Total:!!Female:!!22 to 24 years
32. B01001_035E	Estimate!!Total:!!Female:!!25 to 29 years
33. B01001_036E	Estimate!!Total:!!Female:!!30 to 34 years
34. B01001_037E	Estimate!!Total:!!Female:!!35 to 39 years
35. B01001_038E	Estimate!!Total:!!Female:!!40 to 44 years
36. B01001_039E	Estimate!!Total:!!Female:!!45 to 49 years
37. B01001_040E	Estimate!!Total:!!Female:!!50 to 54 years
38. B01001_041E	Estimate!!Total:!!Female:!!55 to 59 years
39. B01001_042E	Estimate!!Total:!!Female:!!60 and 61 years
40. B01001_043E	Estimate!!Total:!!Female:!!62 to 64 years
41. B01001_044E	Estimate!!Total:!!Female:!!65 and 66 years
42. B01001_045E	Estimate!!Total:!!Female:!!67 to 69 years
43. B01001_046E	Estimate!!Total:!!Female:!!70 to 74 years
44. B01001_047E	Estimate!!Total:!!Female:!!75 to 79 years
45. B01001_048E	Estimate!!Total:!!Female:!!80 to 84 years
46. B01001_049E	Estimate!!Total:!!Female:!!85 years and over
-------------------------------------------------------------
47. DP05_0002PE	Percent!!SEX AND AGE!!Total population!!Male
48. DP05_0003PE	Percent!!SEX AND AGE!!Total population!!Female

### Section 2.2
1. DP03_0051E	Estimate!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households
2. DP03_0051PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households
3. DP03_0052PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000	
4. DP03_0053PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999	
5. DP03_0054PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999	
6. DP03_0055PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999	
7. DP03_0056PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999	
8. DP03_0057PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999	
9. DP03_0058PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999	
10. DP03_0059PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999	
11. DP03_0060PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999	
12. DP03_0061PE	Percent!!INCOME AND BENEFITS (IN 2023 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more

## Information on syntaxes:

### Geopandas
.columns = returns df's columns
.rows = returns df's rows

### Python
- if __name__ == "__main__":
    This is used to prevent a code block from being executed when importing that code block's module to another module.