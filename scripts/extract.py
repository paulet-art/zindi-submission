import pandas as pd
from sqlalchemy import create_engine
import pandas_datareader as pdr
import json
import re
#from pandas_datareader.yahoo.headers import DEFAULT_HEADERS
#from pandas_datareader import requests_cache
import datetime as dt

def extract_supabase_data():
    engine = create_engine("postgresql://postgres.fsbquqgnsutpepvjcrfr:juM70PkREv4HDxVm@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres")
    connection = engine.connect()
    result = connection.execute("SELECT * FROM historical_financial_data_obt")
    result = result.fetchall()
    print("Fetched Data:")
    for row in result:
        print(row)
    return result

extracted_data = extract_supabase_data()

def extract_yahoo_finance_data():
    #expire_after = dt.timedelta(days=1)
    #session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
    #session.headers = DEFAULT_HEADERS
    start_date = dt.datetime(2018, 1, 1)
    end_date = dt.datetime(2024, 1, 1)
    btc = pdr.get_data_yahoo('BTC-USD', start_date, end_date)
    eth = pdr.get_data_yahoo('ETH-USD', start_date, end_date)
    btc.reset_index(inplace=True)
    eth.reset_index(inplace=True)
    return btc, eth

