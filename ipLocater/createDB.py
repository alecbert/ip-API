import pandas as pd
from sqlalchemy import create_engine

# make this less hardcoded
file='../resources/test-ipv4.csv'

print(pd.read_csv(file, nrows=5))
csv_database = create_engine('sqlite:///ip_addresses.db')

CHUNKSIZE = 1000
fields=['network', 'latitude', 'longitude']

# not using the fields other than lat and long right now. saving the network just in case I want to use it
for df in pd.read_csv(file, chunksize=CHUNKSIZE, iterator=True, usecols=fields):
    df.to_sql('locations', csv_database, if_exists='append')
