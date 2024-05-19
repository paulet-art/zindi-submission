from scripts.extract import extract_supabase_data, extract_yahoo_finance_data

btc_data, eth_data = extract_yahoo_finance_data()
print("\nSample data from Yahoo Finance (Bitcoin):")
print(btc_data.head())
print("\nSample data from Yahoo Finance (Ethereum):")
print(eth_data.head())