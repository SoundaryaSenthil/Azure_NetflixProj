# Databricks notebook source
# MAGIC %md
# MAGIC ## DLT Notebook-Gold layer

# COMMAND ----------

looktables_rules = {
    "rule1":"show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_directors"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df=spark.readStream.format("delta").load("abfss://silver@adlsnetflixproject.dfs.core.windows.net/netflix_directors")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_cast"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df=spark.readStream.format("delta").load("abfss://silver@adlsnetflixproject.dfs.core.windows.net/netflix_cast")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_countries"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df=spark.readStream.format("delta").load("abfss://silver@adlsnetflixproject.dfs.core.windows.net/netflix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflix_category"
)
@dlt.expect_or_drop("rule1","show_id is NOT NULL")
def myfunc():
    df=spark.readStream.format("delta").load("abfss://silver@adlsnetflixproject.dfs.core.windows.net/netflix_category")
    return df

# COMMAND ----------

@dlt.table

def gold_stg_netflix_titles():
    df=spark.readStream.format("delta").load("abfss://silver@adlsnetflixproject.dfs.core.windows.net/netflix_titles")
    return df

# COMMAND ----------

from pyspark.sql.functions import*

# COMMAND ----------

@dlt.view

def gold_transform_netflix_titles(): 
        df=spark.readStream.table("LIVE.gold_stg_netflix_titles")
        df= df.withColumn("newflag",lit(1))
        return df

# COMMAND ----------

masterdata_rules={
    "rule1":"newflag is NOT NULL",
    "rule2":"show_id is NOT NULL"
}


# COMMAND ----------

@dlt.table

@dlt.expect_all_or_drop(masterdata_rules)

def gold_netflix_titles():

    df=spark.readStream.table("LIVE.gold_transform_netflix_titles")
    return df
