import requests
from mapCreation import gpd

# More information of this module in Section 2.1 of README.md

# Transpose the variables to a csv file
r = requests.get("https://api.census.gov/data/2022/acs/acs5/profile?get=group(DP03)&ucgid=0400000US72").json()
df = gpd.GeoDataFrame(r)
df.transpose().to_csv("data/live_data/tmp.csv")

# API link that contains variable with population according to age and gender ALONG with other variables
    # https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP05)&ucgid=pseudo(0400000US72$0600000)
variableNames = ["DP05_0001E","DP05_0001EA","DP05_0001M","DP05_0001MA","DP05_0001PE","DP05_0001PEA","DP05_0001PM","DP05_0001PMA","DP05_0002E","DP05_0002EA","DP05_0002M","DP05_0002MA","DP05_0002PE","DP05_0002PEA","DP05_0002PM","DP05_0002PMA","DP05_0003E","DP05_0003EA","DP05_0003M","DP05_0003MA","DP05_0003PE","DP05_0003PEA","DP05_0003PM","DP05_0003PMA","DP05_0004E","DP05_0004EA","DP05_0004M","DP05_0004MA","DP05_0004PE","DP05_0004PEA","DP05_0004PM","DP05_0004PMA","DP05_0005E","DP05_0005EA","DP05_0005M","DP05_0005MA","DP05_0005PE","DP05_0005PEA","DP05_0005PM","DP05_0005PMA","DP05_0006E","DP05_0006EA","DP05_0006M","DP05_0006MA","DP05_0006PE","DP05_0006PEA","DP05_0006PM","DP05_0006PMA","DP05_0007E","DP05_0007EA","DP05_0007M","DP05_0007MA","DP05_0007PE","DP05_0007PEA","DP05_0007PM","DP05_0007PMA","DP05_0008E","DP05_0008EA","DP05_0008M","DP05_0008MA","DP05_0008PE","DP05_0008PEA","DP05_0008PM","DP05_0008PMA","DP05_0009E","DP05_0009EA","DP05_0009M","DP05_0009MA","DP05_0009PE","DP05_0009PEA","DP05_0009PM","DP05_0009PMA","DP05_0010E","DP05_0010EA","DP05_0010M","DP05_0010MA","DP05_0010PE","DP05_0010PEA","DP05_0010PM","DP05_0010PMA","DP05_0011E","DP05_0011EA","DP05_0011M","DP05_0011MA","DP05_0011PE","DP05_0011PEA","DP05_0011PM","DP05_0011PMA","DP05_0012E","DP05_0012EA","DP05_0012M","DP05_0012MA","DP05_0012PE","DP05_0012PEA","DP05_0012PM","DP05_0012PMA","DP05_0013E","DP05_0013EA","DP05_0013M","DP05_0013MA","DP05_0013PE","DP05_0013PEA","DP05_0013PM","DP05_0013PMA","DP05_0014E","DP05_0014EA","DP05_0014M","DP05_0014MA","DP05_0014PE","DP05_0014PEA","DP05_0014PM","DP05_0014PMA","DP05_0015E","DP05_0015EA","DP05_0015M","DP05_0015MA","DP05_0015PE","DP05_0015PEA","DP05_0015PM","DP05_0015PMA","DP05_0016E","DP05_0016EA","DP05_0016M","DP05_0016MA","DP05_0016PE","DP05_0016PEA","DP05_0016PM","DP05_0016PMA","DP05_0017E","DP05_0017EA","DP05_0017M","DP05_0017MA","DP05_0017PE","DP05_0017PEA","DP05_0017PM","DP05_0017PMA","DP05_0018E","DP05_0018EA","DP05_0018M","DP05_0018MA","DP05_0018PE","DP05_0018PEA","DP05_0018PM","DP05_0018PMA","DP05_0019E","DP05_0019EA","DP05_0019M","DP05_0019MA","DP05_0019PE","DP05_0019PEA","DP05_0019PM","DP05_0019PMA","DP05_0020E","DP05_0020EA","DP05_0020M"]
varResults = ["4660","null","673","null","4660","null","-888888888","(X)","2173","null","398","null","46.6","null","4.2","null","2487","null","377","null","53.4","null","4.2","null","87.4","null","14.6","null","-888888888","(X)","-888888888","(X)","173","null","114","null","3.7","null","2.4","null","312","null","135","null","6.7","null","2.6","null","382","null","154","null","8.2","null","3.2","null","327","null","131","null","7.0","null","2.6","null","138","null","87","null","3.0","null","1.7","null","651","null","243","null","14.0","null","4.3","null","502","null","154","null","10.8","null","3.1","null","515","null","167","null","11.1","null","3.0","null","151","null","62","null","3.2","null","1.2","null","300","null","114","null","6.4","null","2.4","null","681","null","137","null","14.6","null","2.9","null","424","null","111","null","9.1","null","2.4","null","104","null","57","null","2.2"]

print(variableNames[varResults.index("173")])

# Variable names that are being used for the population 
# DP05_0005E	Estimate!!SEX AND AGE!!Total population!!Under 5 years
# DP05_0006E	Estimate!!SEX AND AGE!!Total population!!5 to 9 years
# DP05_0007E	Estimate!!SEX AND AGE!!Total population!!10 to 14 years
# DP05_0008E	Estimate!!SEX AND AGE!!Total population!!15 to 19 years
# DP05_0009E	Estimate!!SEX AND AGE!!Total population!!20 to 24 years
# DP05_0010E	Estimate!!SEX AND AGE!!Total population!!25 to 34 years
# DP05_0011E	Estimate!!SEX AND AGE!!Total population!!35 to 44 years
# DP05_0012E	Estimate!!SEX AND AGE!!Total population!!45 to 54 years
# DP05_0013E	Estimate!!SEX AND AGE!!Total population!!55 to 59 years
# DP05_0014E	Estimate!!SEX AND AGE!!Total population!!60 to 64 years
# DP05_0015E	Estimate!!SEX AND AGE!!Total population!!65 to 74 years
# DP05_0016E	Estimate!!SEX AND AGE!!Total population!!75 to 84 years
# DP05_0017E	Estimate!!SEX AND AGE!!Total population!!85 years and over