# Azure Netflix Data Engineering Project

# Project Description

This project focuses on building a fully automated, scalable, and efficient data ingestion and processing pipeline using Azure services for processing Netflix-related datasets. The pipeline fetches data from GitHub, validates it, performs multi-stage transformations using Databricks, and stores the curated data in a structured Data Lake with layered architecture (Raw, Bronze, Silver, Gold). The project is designed to support incremental loads, parameterized workflows, scheduling, and robust data quality checks using Delta Live Tables (DLT).

# Project Architecture:

# GitHub (Data Source)
       |
       v
# Azure Data Factory (Dynamic Pipeline)
       |     |-- Data Validation & File Filtering
       |     |-- ForEach Activity (Parallel Load)
       v
# Azure Data Lake Storage Gen2 (Raw Zone)
       |
       v
# Databricks (Connected via DB Utils & Unity Metastore)
       |
       |-- Autoloader: Raw to Bronze (Streaming)
       |-- Silver: Data Cleansing & Transformation
       |-- Gold: Aggregation + Business Rules using DLT
       |
       v
# Azure Data Lake (Bronze, Silver, Gold, Meta Layers)
       |
       v
# Scheduled Workflows via Lookup Notebooks

**Technologies & Skills Used:**
	•**Cloud Platform**: Microsoft Azure
	•**Data Lake:** Azure Data Lake Storage Gen2
	•**Data Orchestration**: Azure Data Factory (ADF)
	•**Data Processing & Transformation:** Databricks (PySpark, SQL, Autoloader)
	•**Metadata Management:** Unity Catalog & External Locations
        •**WorkflowManagement:** Databricks Workflows & Lookup Notebooks
	•**Scheduling:** Cron-based notebook scheduling with weekday conditions
	•**Data Quality:** Delta Live Tables (DLT) with Expectation Rules
	•**Languages:** Python, PySpark, SQL
	•**Version Control:**  GitHub

⸻

**My Contributions**
	•Designed and implemented a dynamic ADF pipeline that imports files from GitHub to ADLS, with parameterized arrays and parallel execution using ForEach activity.
	•Built data validation logic to check for the presence of required master files before processing.
	•Set up Databricks external locations using Unity Metastore for all layers: Raw, Bronze, Silver, Gold, and Meta.
	•Developed Autoloader jobs to stream files from Raw to Bronze layer efficiently.
	•Created transformation notebooks for Silver layer that handled:
	•Null filling
	•Data type casting
	•Column splitting and flag creation
	•Window functions (ranking)
	•Aggregations (counts by show/movie type)
	•Scheduled workflows using lookup notebooks to run on specific days (only Sundays).
	•Built DLT pipelines for Gold layer with expectation rules (e.g., show_id IS NOT NULL) for quality enforcement.
	•Maintained modular, reusable, and production-friendly code with clear separation of layers and parameters.

⸻

**Challenges Faced and Solutions**
	1.Streaming Limitation in Serverless Autoloader
	•Issue: Serverless compute only loaded data once; it didn’t support continuous streaming.
	•Solution: Switched to all-purpose compute clusters in Databricks which allowed the Autoloader to work in streaming mode.
	2.Handling Missing Master Files
	•Issue: Pipeline would break if required master file wasn’t present in the Raw zone.
	•Solution: Implemented data validation logic in ADF to skip processing when critical files were missing.
	3.Workflow Scheduling Constraints
	•Issue: Needed pipeline to run only on Sundays with conditional logic.
	•Solution: Used a lookup notebook to dynamically check the weekday and proceed only if the day was Sunday.
