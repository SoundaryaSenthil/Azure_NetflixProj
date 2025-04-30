
# Azure Netflix Data Engineering Project

## Project Overview

This project implements a dynamic and scalable data engineering pipeline on Azure to process Netflix-related data from GitHub. It leverages Azure Data Factory for orchestration, Azure Data Lake Storage for storage, and Databricks with Unity Metastore for processing and transformation. The pipeline is designed to perform validation, conditional loading, parallel processing, and multi-stage data transformations using a bronze-silver-gold layer architecture.

![ChatGPT Image Apr 30, 2025, 10_27_03 PM](https://github.com/user-attachments/assets/97b4073d-7783-40e9-b3e4-bf55b874710f)

---

## Architecture

```
GitHub (Data Source)
       |
       v
Azure Data Factory (Dynamic Pipeline)
       |     |-- Data Validation & File Filtering
       |     |-- ForEach Activity (Parallel Load)
       v
Azure Data Lake Storage Gen2 (Raw Zone)
       |
       v
Databricks (Connected via DB Utils & Unity Metastore)
       |
       |-- Autoloader: Raw to Bronze (Streaming)
       |-- Silver: Data Cleansing & Transformation
       |-- Gold: Aggregation + Business Rules using DLT
       |
       v
Azure Data Lake (Bronze, Silver, Gold, Meta Layers)
       |
       v
Scheduled Workflows via Lookup Notebooks
```

---
![Screenshot 2025-04-30 213735](https://github.com/user-attachments/assets/0a674de0-a969-4d00-8df1-818a01f0348f)

## Technologies & Tools

- **Cloud Platform**: Microsoft Azure
- **Storage**: Azure Data Lake Storage Gen2
- **Orchestration**: Azure Data Factory (ADF)
- **Data Processing**: Azure Databricks (with Unity Catalog)
- **Languages**: Python, PySpark, SQL
- **Streaming**: Autoloader
- **Data Quality & ETL**: Delta Live Tables (DLT)
- **Workflow Scheduling**: Databricks Workflows + Lookup Notebooks
- **Version Control**: GitHub

---

## Features

- Dynamic and parameterized ADF pipeline for ingesting files from GitHub.
- Data validation to ensure presence of master files before processing.
- Parallel file loading using ForEach activity.
- Structured data lake zones: Raw, Bronze, Silver, Gold, and Meta.
- Real-time ingestion using Databricks Autoloader.
- Complex transformations using PySpark (casting, null handling, column operations, window functions, aggregations).
- Conditional workflow scheduling (only run on Sundays).
- Gold layer processing using Delta Live Tables (DLT) with quality checks (`show_id IS NOT NULL`).

---
![Screenshot 2025-04-29 231018](https://github.com/user-attachments/assets/725ce5c1-d231-4ea1-8e33-3b54cb5800cd)
![Screenshot 2025-04-29 232301](https://github.com/user-attachments/assets/a2b2c6c8-6031-47dd-a211-83762f7c3756)
![Screenshot 2025-04-30 213245](https://github.com/user-attachments/assets/397097f0-b58b-4e4e-b8a3-f3a75542f33e)
![Screenshot 2025-04-30 222831](https://github.com/user-attachments/assets/df74c64d-983e-4036-82d9-1ba5a717e3ca)



## My Contributions

- Designed and developed a parameterized dynamic ADF pipeline.
- Implemented validation checks for essential files.
- Set up Databricks external locations and Unity Metastore.
- Created notebooks for all transformation stages (bronze → silver → gold).
- Handled complex data logic (e.g., flag creation, ranking, counts by show/movie types).
- Developed a lookup notebook for dynamic workflow scheduling.
- Applied DLT rules for ensuring data quality in the gold layer.

---

## Challenges & Solutions

### 1. Streaming Limitation in Serverless Compute
- **Issue**: Serverless compute with Autoloader only allowed one-time loads.
- **Solution**: Switched to all-purpose compute clusters for continuous streaming.

### 2. Missing Master Files Breaking the Pipeline
- **Issue**: Pipeline failed if master files were not available.
- **Solution**: Built validation logic to skip execution if required files were missing.

### 3. Weekday-Based Scheduling
- **Issue**: Pipeline needed to run only on Sundays.
- **Solution**: Created a lookup notebook to detect the current day and conditionally execute the workflow.

---
![Screenshot 2025-04-30 200707](https://github.com/user-attachments/assets/ed446c2e-af2c-411a-8d1a-555a72b48395)
![Screenshot 2025-04-30 200930](https://github.com/user-attachments/assets/21270b7b-7e40-45c5-8504-58d9dffe6891)


---

## Contact

If you have any questions or want to collaborate, feel free to connect with me on [LinkedIn](linkedin.com/in/soundarya-s-dataengineer).

---
Happy learning!!
