from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

from airflow.providers.amazon.aws.hooks.s3 import S3Hook

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etls.etl import process_crime_data
from config.constants import UK_CITIES

default_args = {
    'owner': 'artun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_previous_month_dates(execution_date=None):
    if execution_date is None:
        execution_date = datetime.today()
    first_day_this_month = execution_date.replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)
    return first_day_prev_month, last_day_prev_month

def upload_to_s3():
    s3 = S3Hook(aws_conn_id='crimes_IAM_connection')
    s3.load_string(
        string_data="hello from airflow",
        key="test-folder/test.txt",
        bucket_name="artun-crime-data"
    )

def run_monthly_etl(**context):
    start_date, end_date = get_previous_month_dates(context['execution_date'])
    process_crime_data(cities=UK_CITIES, dates=(start_date, end_date))

with DAG(
    dag_id="crimes_monthly_dag",
    default_args=default_args,
    description="Monthly ETL pipeline for UK crime data.",
    start_date=datetime(2025, 7, 15),
    schedule='@monthly',
    catchup=False,
    tags=['monthly', 'crime-data']
) as dag:

    test_task = PythonOperator(
        task_id="test_task",
        python_callable=upload_to_s3
    )

    monthly_task = PythonOperator(
        task_id="monthly_task",
        python_callable=run_monthly_etl,
        provide_context=True
    )

test_task >> monthly_task
