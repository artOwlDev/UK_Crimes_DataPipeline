import boto3
import json
import pandas as pd
from datetime import datetime
import requests
from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def fetch_and_store_crime_data(city, lat, lng, date, aws_conn_id):

    url = f"https://data.police.uk/api/crimes-at-location?date={date}&lat={lat}&lng={lng}"
    response = requests.get(url)
    raw_data = response.json()

    s3_hook = S3Hook(aws_conn_id=aws_conn_id)
    raw_key = f"bronze/{city}/{date}/{city}_{date}.json"

    s3_hook.load_string(
        string_data=json.dumps(raw_data),
        key=raw_key,
        bucket_name='artun-crime-data',
        replace=True
    )
    return raw_data, raw_key

def transform_and_store_crime_data(raw_data, city, date, aws_conn_id):

    transformed_data = []

    for record in raw_data:

        crime_obj = {
            "city": city,
            "lat": record["location"]["latitude"],
            "lng": record["location"]["longitude"],
            "date": date,
            "crime_type": record["category"],
            "outcome": record["outcome_status"]["category"] if record["outcome_status"] else None,
            "processed_at": datetime.now().isoformat()
        }

        transformed_data.append(crime_obj)

    df = pd.DataFrame(transformed_data)

    csv_data = df.to_csv(index=False)  # convert to CSV string

    csv_key = f"silver/{city}/{date}/crimes_{city}_{date}.csv"

    s3_hook = S3Hook(aws_conn_id=aws_conn_id)
    s3_hook.load_string(
        string_data=csv_data,
        key=csv_key,
        bucket_name='artun-crime-data',
        replace=True
    )
    


def process_crime_data(cities, dates):
    for city_data in cities:
        for date_data in dates:
            city = city_data["city"]
            lat = city_data["lat"]
            lng = city_data["lng"]
            date = date_data["date"]
            
            raw_data, raw_key = fetch_and_store_crime_data(city, lat, lng, date, "crimes_IAM_connection")
            
            transformed_data = transform_and_store_crime_data(raw_data, city, date, "crimes_IAM_connection")