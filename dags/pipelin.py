from airflow import DAG
from airflow.operators.python_operators import PythonOperator
from datetime import datetime 
from scripts.extract import extract_supabase_data, extract_yahoo_finance_data
from scripts.transform import transform_data
from scripts.load import load_data_to_supabase

default_args = {
    'owner' : 'airflow',
    'start_date': datetime(2024, 5, 19),
    'retries': 1
}

dag = DAG(
    'pipeline',
    default_args=default_args,
    schedule_interval='@daily'
)

def extract_task(ti):
    df = extract_supabase_data()
    btc, eth = extract_yahoo_finance_data()
    