# UK Crimes Data Pipeline

## Project Architecture
<img width="3692" height="1448" alt="image" src="https://github.com/user-attachments/assets/415f5a7d-92f9-4bb6-89d0-822c4547102d" />

## Project Overview
This project automates the processing and visualization of UK crime data. It handles historical backfill and monthly updates, providing insights into crime types and frequency.

## Project Lifecycle
- **Data Ingestion:** Collects UK crime data from the official [UK Crimes Dataset](https://data.police.uk/) using batch processing  
- **ETL Pipeline:** Airflow orchestrates the pipeline, handling both historical backfill and monthly updates  
- **Data Transformation:** Processes and cleans data using Python before storage  
- **Data Storage:** Stores raw and transformed data in **AWS S3**  
- **Metadata & Cataloging:** Uses **AWS Glue Crawler** and **Glue Data Catalog** to manage schema and metadata  
- **Querying & Analytics:** Processes data with **AWS Athena** for efficient querying  
- **Data Visualization:** Visualizes insights using **Tableau** dashboards  

## Technologies
- **Python** for data processing  
- **Airflow** for scheduling and pipeline orchestration  
- **AWS S3** for data storage  
- **Tableau** for visualizing trends and patterns

## Snapshots
**DAGs on Airflow**
<img width="896" height="1000" alt="Screenshot 2025-07-20 at 3 41 25 PM" src="https://github.com/user-attachments/assets/25a76e1f-2fe4-4ef1-a42c-a8f1db3259b9" />

**Querying with SQL in Athena**
<img width="2006" height="1203" alt="Screenshot 2025-07-20 at 3 16 03 PM" src="https://github.com/user-attachments/assets/30f5265c-5435-487d-b8e4-321aef567a4f" />

**Visualization with Tableau**
<img width="3224" height="2093" alt="image" src="https://github.com/user-attachments/assets/5cc610f1-0d05-4634-8c3b-342a4d899365" />

## Usage
- Run the DAG in Airflow to process new monthly data  
- Visualizations are automatically updated in Tableau dashboards
- Feel free to ask for the requirments.txt if you want to run it locally :)
