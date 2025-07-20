from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

from airflow.providers.amazon.aws.hooks.s3 import S3Hook


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etls.etl import process_crime_data
from config.constants import UK_CITIES, DATES

default_args = {
    'owner': 'artun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)  
}

my_dag = DAG(
    dag_id="crimes_backfill_dag",
    default_args=default_args,
    description="ETL pipeline for past UK crime data.",
    start_date=datetime(2025, 7, 15),
    schedule=None, 
    tags=['backfill', 'crime-data', 'historical']
)

def upload_to_s3():
    s3 = S3Hook(aws_conn_id='crimes_IAM_connection')
    s3.load_string(
        string_data="hello from airflow",
        key="test-folder/test.txt",
        bucket_name="artun-crime-data"
    )


test_task = PythonOperator(
    task_id="test_task",
    python_callable=upload_to_s3,
    dag=my_dag
)

backfill_task = PythonOperator(
    task_id="backfill_task",
    python_callable=process_crime_data,
    op_kwargs={"cities": UK_CITIES, "dates": DATES},
    dag=my_dag
)

backfill_task