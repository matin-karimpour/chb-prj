"""get data from randomuser
"""

import os
import json
import requests
import pandas as pd
from sqlalchemy import create_engine
from utils import get_hashed_password

# checks data downloaded
data_exists = os.path.isfile("part1.csv") and os.path.isfile("part2.csv") 
print(data_exists)

if not data_exists:
    # download data and save it
    for i in [1,2]:
        r = requests.get(f"https://randomuser.me/api/?page={i}&results=5000")
        x = r.json()
        df = pd.json_normalize(x['results'])
        df.to_csv(f"part{i}.csv",index=False)
        print(df)

df = pd.read_csv("part1.csv")
df1 = pd.read_csv("part2.csv")
df = pd.concat([df,df1], ignore_index=True)
del df1
print(df)
print(df.columns)

# rename columns
df = (df[df.columns]. rename( columns = lambda c: c. replace ( '.' ,'_')))

# filter users based on thier
df = df[(df['gender']=='male') & (df['dob_age'] > 30)]
print(df)

# hash password
df['login_password'] = df.login_password.astype(str).apply(get_hashed_password)
print(df['login_password'])