import acs_year

acsYear = acs_year.getACS_year()

# Construct the URL for the ACS dataset
popPerSubCou_url = f"https://api.census.gov/data/{acsYear}/acs/acs5?get=group(B01001)&ucgid=pseudo(0400000US72$0600000)"
households_url = f"https://api.census.gov/data/{acsYear}/acs/acs5/profile?get=DP03_0051E,DP03_0051PE,DP03_0052PE,DP03_0053PE,DP03_0054PE,DP03_0055PE,DP03_0056PE,DP03_0057PE,DP03_0058PE,DP03_0059PE,DP03_0060PE,DP03_0061PE&ucgid=pseudo(0400000US72$0600000)"
