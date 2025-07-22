# UK Crimes Data Pipeline

## Overview

This project automates the ingestion, transformation, and analysis of UK crime data. The data is collected by the offical police department of the UK's API. The data is first set on a backfill DAG to collect all the data to present day (all the data available so far)
Backfilled data is stored into bronze(raw data) and silver(transformed data) layers on AWS S3, it's made queryable via AWS Glue and Athena. 

## Architecture

<img width="1846" height="724" alt="Screenshot 2025-07-17 at 9 05 01 PM" src="https://github.com/user-attachments/assets/a50baf0c-bf41-4381-bbc6-f0731d4bbdce" />

- **Data Sources:** UK Police API ([https://data.police.uk](https://data.police.uk/docs/))  
- **Storage Layers:**  
  - Bronze (raw JSON data in S3)  
  - Silver (transformed CSV/parquet data in S3)  
- **Compute:** AWS Glue jobs and crawlers for ETL and metadata management  
- **Querying:** AWS Athena for analytics  
- **Orchestration:** Apache Airflow for scheduling and dependency management  

## Features

- Automated data fetch for multiple cities and date ranges  
- Transformation includes geo-coordinates parsing, crime categorization, and outcome normalization  
- Raw and processed data storage for traceability  
- Schema management with AWS Glue Data Catalog  
- Modular Python code using pandas  

## Snapshots of Project

### S3 Silver Layer
<img width="1481" height="596" alt="Screenshot 2025-07-20 at 3 39 46 PM" src="https://github.com/user-attachments/assets/10d78009-947c-498c-98b7-a0173b4753ec" />


### Querying Results w/ Athena
<img width="1664" height="1071" alt="Screenshot 2025-07-20 at 3 16 11 PM" src="https://github.com/user-attachments/assets/7ed1ee06-6a86-46df-8797-39c65df0d3df" />

### Backfill DAG on airflow
<img width="896" height="1204" alt="Screenshot 2025-07-20 at 3 41 25 PM" src="https://github.com/user-attachments/assets/6c43b70b-3cad-4d85-bb95-58031e9bb970" />


### Prerequisites
- Python 3.8 or higher  
- AWS CLI configured with valid IAM credentials  
- Access to AWS S3, Glue, and Athena services  
- Apache Airflow (optional).

Note: Feel free to reach out if you want the requirements.txt for usage/testing :)

### Contact
- https://www.linkedin.com/in/artunselcuk/
