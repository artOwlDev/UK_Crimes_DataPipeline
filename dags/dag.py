from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests

UK_CITIES = [
    {"city": "London", "lat": 51.507351, "lng":  -0.127758},
    {"city": "Birmingham", "lat": 52.4823, "lng":  -1.8900},
    {"city": "Manchester", "lat": 53.4808, "lng":  -2.2426},
    {"city": "Glasgow", "lat": 55.8617, "lng":  -4.2583},
    {"city": "Leeds", "lat": 53.8008, "lng":  -1.5491},
    {"city": "Liverpool", "lat": 53.4084, "lng":  -2.9916},
    {"city": "Sheffield", "lat": 53.3811, "lng":  -1.4701},
    {"city": "Bristol", "lat": 51.4545, "lng":  -2.5879},
    {"city": "Leicester", "lat": 52.6369, "lng":  -1.1398},
    {"city": "Edinburgh", "lat": 55.9533, "lng":  -3.1883},
]

DATES = [
    {"date" : "2023-01"},
    {"date" : "2023-02"},
    {"date" : "2023-03"},
    {"date" : "2023-04"},
    {"date" : "2023-05"},
    {"date" : "2023-06"},
    {"date" : "2023-07"},
    {"date" : "2023-08"},
    {"date" : "2023-09"},
    {"date" : "2023-10"},
    {"date" : "2023-11"},
    {"date" : "2023-12"},
    {"date" : "2024-01"},
    {"date" : "2024-02"},
    {"date" : "2024-03"},
    {"date" : "2024-04"},
    {"date" : "2024-05"},
    {"date" : "2024-06"},
    {"date" : "2024-07"},
    {"date" : "2024-08"},
    {"date" : "2024-09"},
    {"date" : "2024-10"},
    {"date" : "2024-11"},
    {"date" : "2024-12"},
    {"date" : "2025-01"},
    {"date" : "2025-02"},
    {"date" : "2025-03"},
    {"date" : "2025-04"},
    {"date" : "2025-05"},
]

default_args = {
    'owner': 'artun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)  
}

url = "https://data.police.uk/api/crimes-at-location?date=2024-01&lat=51.507351&lng=-0.127758"

my_dag = DAG(
    dag_id="crimes_etl",
    default_args=default_args,
    description="ETL pipeline for UK crime data.",
    start_date=datetime(2025, 7, 15),
    schedule="@monthly", 

)


def fetch_crime_data(city, lat, lng, date):

    url = f"https://data.police.uk/api/crimes-at-location?date={date}&lat={lat}&lng={lng}"
    response = requests.get(url)
    raw_data = response.json()

    file_name_format = f"crimes_{city}_{date}"

    

    return crime


def transform_crime_data():

    crime = {
        "city": city,
        "lat": data["location"]["latitude"],
        "lng": data["location"]["longitude"],
        "date": date,
        "crime_type": data["category"],
        "outcome": data["outcome_status"]["category"]        
    }

