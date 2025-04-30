# Databricks notebook source
var = dbutils.jobs.taskValues.get(taskKey = 'weekdaylookup', key = 'weekoutput')

# COMMAND ----------

print(var)
