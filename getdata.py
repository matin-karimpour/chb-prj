"""get data from randomuser
"""

import os
import json
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from utils import get_hashed_password
import numpy as np
engine = create_engine('postgresql://user1:12345678@localhost:5433/chbox')

# checks data downloaded
data_exists = os.path.isfile("part1.csv") and os.path.isfile("part2.csv") 
final_dataset_path = "final_dataset.csv"
final_dataset_exists = os.path.isfile(final_dataset_path) 
print(data_exists)
if data_exists:
    df = pd.read_csv(final_dataset_path)
else:
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

    # rename columns
    df = (df[df.columns]. rename( columns = lambda c: c. replace ( '.' ,'_')))
    print(df.columns)

    # filter users based on thier
    df = df[(df['gender']=='male') & (df['dob_age'] > 30)]
    print(df)

    # hash password
    df['login_password'] = df.login_password.astype(str).apply(get_hashed_password)
    print(df['login_password'])

    df = df [["email", "dob_age", "login_password", "name_first",
            "name_last", "login_username", "location_country", "location_city"]]
    df.to_csv(final_dataset_path, index=False)
# dataframe to postgres
df.index = np.arange(1, len(df) + 1)
df.to_sql('chb', engine, index=True, index_label='id', if_exists="replace")

with engine.connect() as conn:
#    conn.execute(text("ALTER TABLE chb ALTER COLUMN id TYPE INTEGER"))
#    conn.execute(text("ALTER TABLE chb ALTER COLUMN id SET NOT NULL;"))
#    conn.execute(text("ALTER TABLE chb ALTER COLUMN id  ADD GENERATED BY DEFAULT AS IDENTITY;"))
   conn.execute(text('ALTER TABLE chb ADD PRIMARY KEY (id);'))

print("done")
