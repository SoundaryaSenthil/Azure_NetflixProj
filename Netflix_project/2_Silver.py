# Databricks notebook source
# MAGIC %md
# MAGIC ## silver notebook lookup tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## Parameters

# COMMAND ----------

dbutils.widgets.text("sourcefolder","netflix_directors")
dbutils.widgets.text("targetfolder","netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Variables

# COMMAND ----------

var_src_folder = dbutils.widgets.get("sourcefolder")
var_tgt_folder = dbutils.widgets.get("targetfolder")

# COMMAND ----------

print(var_src_folder)
print(var_tgt_folder)

# COMMAND ----------

df= spark.read.format("csv")\
    .option("header","true")\
    .option("inferSchema","true")\
    .load(f"abfss://bronze@adlsnetflixproject.dfs.core.windows.net/{var_src_folder}")
  

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("path",f"abfss://silver@adlsnetflixproject.dfs.core.windows.net/{var_tgt_folder}")\
    .save()

# COMMAND ----------


