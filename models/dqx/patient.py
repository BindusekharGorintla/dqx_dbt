import pyspark.sql.functions as F
import logging

logger = logging.getLogger("dbt")

def model(dbt, spark):

    dbt.config(
        materialized="table",
        submission_method="all_purpose_cluster",
        cluster_id="XXXXXXXXXXXXXXXXXXXXXX",  # must be literal
        create_notebook=False
    )

    # Reference another model
    stg_customers_df = dbt.ref("table_name")

    logger.info("✅ Model execution started")

    # (Optional) Do transformations
    result_df = stg_customers_df.withColumn("row_count", F.lit(1))

    return result_df
