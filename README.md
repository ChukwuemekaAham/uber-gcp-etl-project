# Uber Data Analytics | Data Engineering Zoomcamp Final Project 2023

![certificate.pdf](https://github.com/ChukwuemekaAham/uber-gcp-etl-project/blob/main/certificate.pdf)

## Overview
This data engineering project is part of the [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) and focuses on analyzing Uber taxi data. The objective is to apply the knowledge gained during the course to build a comprehensive data pipeline.

## Problem Statement
The goal of this project is to perform data analytics on Uber data using various tools and technologies, including GCP Storage, Python, Compute Instance, Mage Data Pipeline Tool, BigQuery, and Looker Studio.

**Questions to answer:**

1. Find the top ten pick up locations, based on the number of trips
2. Find the total number of trips by passenger count
3. Find the average fair amount by hour of the day

## Dataset Used
TLC Trip Record Data
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. 

More info about dataset can be found here:
1. Website - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary - https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

The PySpark transformation script includes the necessary PySpark functions and logic to perform the required transformations. However, it assumes that the input DataFrame `df` contains the required columns (`index`, `tpep_pickup_datetime`, `tpep_dropoff_datetime`, `passenger_count`, `trip_distance`, `RatecodeID`, `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`).

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


## Project Architecture

![Cloud Architecture](https://github.com/ChukwuemekaAham/uber-gcp-etl-project/blob/main/architecture.png)

The project architecture consists of a set of interconnected components designed to handle various aspects of data ingestion, processing, storage, and analysis. The key components are as follows:

- Data Ingestion: Mage is used to get the data, ensuring that the data is collected.
- Data Storage: The data is stored in Google Cloud Storage (GCS) as csv file. GCS provides a scalable and reliable storage solution for the project.
- Data Processing: Mage is utilized to process the data using python and Apache Spark. Enabling data processing tasks, transforming and aggregating the raw data into the uber_dataset tables.
- Data Warehouse: Google BigQuery serves as the data warehouse for the project, storing the processed and aggregated data in the uber_dataset tables. BigQuery allows for efficient querying and analysis of the data, making it an ideal choice for this project.
- Data Visualization: Looker is used for data visualization, enabling users to explore the data and uncover insights about uber trips and patterns. By leveraging Looker's powerful visualization capabilities, stakeholders can easily understand the results of the data analysis and make informed decisions.
- Infrastructure as Code (IaC): Terraform is used to manage the infrastructure components of the project. This IaC approach ensures that the infrastructure is easily reproducible and can be managed in a version-controlled manner.

The project architecture is designed to provide a scalable, reliable, and efficient solution for ingesting, processing, storing, and analyzing Uber Trip data, ultimately enabling stakeholders to make data-driven decisions and improve the system's performance.

1. Clone this repository
2. Refresh service-account's auth-token for this session

    ```gcloud auth application-default login```

3. Terraform
   Change to terraform directory

     ```cd terraform_infra```
    
    Initialize terrform

    ```terraform init```

    Preview the changes to be applied:
    ```terraform plan```
    It will ask for your GCP Project ID and a name for your DataProc Cluster

    Apply the changes:
    ```terraform apply```

4. Install the required Python packages:

    ```open linux.md file and follow the instructions```

    ```open pyspark.md file and follow the instructions```
   
    ```open the setup.txt file and run the commands```

5. Add Google Cloud Service Account Key to Mage io_config.yaml file

   `GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/path/to/your/service/account/key.json"`

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
4. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
