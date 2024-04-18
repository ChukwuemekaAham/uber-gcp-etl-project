# Uber Data Analytics | Modern Data Engineering GCP Project

## Introduction

The goal of this project is to perform data analytics on Uber data using various tools and technologies, including GCP Storage, Python, Compute Instance, Mage Data Pipeline Tool, BigQuery, and Looker Studio.

https://lucid.app/users/login#/login 

https://draw.io 

## Architecture 
<img src="architecture.jpg">

## Technology Used
- Programming Language - Python

Google Cloud Platform
1. Terraform Infrastructure
2. Google Storage
3. Compute Instance 
4. Mage
5. PySpark
6. BigQuery
7. Looker Studio

Modern Data Pipeine Tool - https://www.mage.ai/

Contibute to this open source project - https://github.com/mage-ai/mage-ai


## Dataset Used
TLC Trip Record Data
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. 

More info about dataset can be found here:
1. Website - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary - https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


## GOALS

- Find the top ten pick up locations, based on the number of trips
- Find the total number of trips by passenger count
- Find the average fair amount by hour of the day


The PySpark transformation script includes the necessary PySpark functions and logic to perform the required transformations. However, it assumes that the input DataFrame `df` contains the required columns (`index`, `tpep_pickup_datetime`, `tpep_dropoff_datetime`, `passenger_count`, `trip_distance`, `RatecodeID`, `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`).


Navigate to the repo:

```bash
cd uber-gcp-etl-project
```

Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with the course. 

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
4. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
