import pandas as pd
import os
from sqlalchemy import create_engine

CHUNKSIZE = 10000
FIELDS = ['network', 'latitude', 'longitude']

def init_db():

    # make this less hardcoded
    file = './static/test-ipv4.csv'

    print(pd.read_csv(file, nrows=5))
    csv_database = create_engine('sqlite:///ip_addresses.db')

    # not using the fields other than lat and long right now. saving the network just in case I want to use it
    for df in pd.read_csv(file, chunksize=CHUNKSIZE, iterator=True, usecols=FIELDS):
        df.to_sql('locations', csv_database, if_exists='append')