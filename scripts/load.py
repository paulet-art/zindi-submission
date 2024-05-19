from sqlalchemy import create_engine

def load_data_to_supabase(financial_data, meta_data, btc, eth):
    engine = create_engine("postgres://postgres.gexcnsxysqvujxbfsgpx:e8xtmSjWSW8NfPP3@aws-0-eu-central-1.pooler.supabase.com:5432/postgres")
    btc.to_sql('bitcoin_historical_data', engine, if_exists='replace', index=False)
    eth.to_sql('ethereum_historical_data', engine, if_exists='replace', index=False)
