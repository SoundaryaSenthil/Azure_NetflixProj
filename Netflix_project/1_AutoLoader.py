# Databricks notebook source
# MAGIC %md
# MAGIC ## Incremental loading using Autoloader

# COMMAND ----------

checkpoint_path ='abfss://silver@adlsnetflixproject.dfs.core.windows.net/checkpointloc'

# COMMAND ----------

df= spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_path)\
  .load("abfss://raw@adlsnetflixproject.dfs.core.windows.net/")

# COMMAND ----------

display(df)

# COMMAND ----------

df.writeStream.option("checkpointLocation", checkpoint_path)\
  .trigger(processingTime='10 seconds')\
  .start("abfss://bronze@adlsnetflixproject.dfs.core.windows.net/netflix_titles")
