from databricks.labs.dqx.engine import DQEngine
from databricks.sdk import WorkspaceClient
from pyspark.sql.types import StructType, StructField, StringType, LongType
from pyspark.sql.functions import size, col
import yaml
import logging

logger = logging.getLogger("dbt")

def model(dbt, spark):
    # --------------------------
    # DBT model configuration
    dbt.config(
        materialized="table",
        alias="dq_checks_validation"
    )

    ws = WorkspaceClient()
    dq_engine = DQEngine(ws)

    # --------------------------
    # Read YAML checks from dq_checks Delta table (dbt handles catalog/schema)
    dq_checks_df = dbt.ref("dqx_checks")

    checks = {}
    for row in dq_checks_df.toLocalIterator():
        table_name = row["table_name"]
        checks_yaml_str = row["checks_yaml"]

        try:
            checks[table_name] = yaml.safe_load(checks_yaml_str) or []
        except Exception as e:
            logger.error(f"Failed to parse YAML for {table_name}: {e}")
            checks[table_name] = []

    # --------------------------
    counts_list = []
    for table, table_checks in checks.items():
        # Source data tables (still need full path if external to dbt project)
        input_df = spark.table(f"database_name.catalog_name.{table}")

        dq_result = dq_engine.apply_checks_by_metadata(input_df, table_checks)

        total_count = dq_result.count()
        invalid_count = dq_result.filter(size(col("_errors")) > 0).count()
        valid_count = total_count - invalid_count

        counts_list.append((table, valid_count, invalid_count))

    # --------------------------
    schema = StructType([
        StructField("table", StringType(), True),
        StructField("valid_count", LongType(), True),
        StructField("invalid_count", LongType(), True)
    ])

    summary_df = spark.createDataFrame(counts_list, schema)
    return summary_df
