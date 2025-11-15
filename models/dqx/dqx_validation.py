import json
from databricks.labs.dqx.engine import DQEngine
from databricks.sdk import WorkspaceClient
from pyspark.sql.types import StructType, StructField, StringType, LongType
from pyspark.sql.functions import size, col
from pyspark.sql import functions as F

def model(dbt, spark):
  # dbt model configuration
  dbt.config(
      materialized="table",
      database="databse_name",
      schema="dqx",
      alias="dq_validation"
  )

  # Initialize DQEngine
  ws = WorkspaceClient()
  dq_engine = DQEngine(ws)

  # Read dq_checks seed table created by dbt
  dq_checks_df = spark.table("database_name.catalog_name.dqx_checks")

  dq_checks = {}
  for row in dq_checks_df.collect():
      entity = row["entity"]
      column = row["column"]
      function = row["function"]
      criticality = row["criticality"]

      if entity not in dq_checks:
          dq_checks[entity] = []

      dq_checks[entity].append({
          "column": column,
          "check": {
              "function": function,
              "arguments": {
                  "column": column,
                  "offset": 0,              # int
                  "curr_timestamp": None    # let DQX handle it
              }
          },
          "level": criticality
      })


  tables_to_validate = list(dq_checks.keys())
  counts_list = []

  for table in tables_to_validate:
      # Read input table
      input_df = spark.table(f"databsae_name.catalog_name.{table}")

      # Apply DQ checks from seed metadata
      dq_result = dq_engine.apply_checks_by_metadata(input_df, dq_checks[table])

      # invalid rows = rows where _errors array is not empty
      invalid_df = dq_result.filter(size(col("_errors")) > 0)
      invalid_count = invalid_df.count()

      # valid rows = total - invalid
      valid_count = input_df.count() - invalid_count

      counts_list.append((table, valid_count, invalid_count))

  # Create summary DataFrame
  schema = StructType([
      StructField("table", StringType(), True),
      StructField("valid_count", LongType(), True),
      StructField("invalid_count", LongType(), True)
  ])

  summary_df = spark.createDataFrame(counts_list, schema)
  return summary_df
