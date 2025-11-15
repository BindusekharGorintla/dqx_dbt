Data Quality Framework (DQX):

DQX is a data quality framework for Apache Spark that enables you to define, monitor, and address data quality issues in your Python-based data pipelines.

Running DQX with DBT projects
This demo shows how to apply data quality checks from dbt projects. The DQX quality checking is executed using dbt python models.

Prerequisites
Install dbt and required adapters:
Press enter or click to view image in full size

Project configuration
Open profiles.yml file and update the following parameters:

http_path to specify Databricks SQL Warehouse ID (<warehouse_id>) to use to execute the dbt sql models.
(optionally) default catalog and schema to use (default: main.default).
Project_Name:
outputs:
dev:
type: databricks
method: http
catalog: catalog_name
schema: schema_name
host: host_name
http_path: url
cluster_id: id
token: id
threads: 8
submission_method: all_purpose_cluster
target: dev

The project is using serverless cluster by default to execute dbt python models (dqx quality checks). To change the default cluster, open dbt_project.yml file and update submission_method (see more here).

dqx:
+materialized: table
+schema: dqx
+submission_method: all_purpose_cluster
+cluster_id: XXXXXXXXXX
+create_notebook: false
+environment_key: Default
+environment_dependencies:
— databricks-labs-dqx

Execution
Provide authentication credentials to connect to the Databricks workspace by running the following in your console:

export DBT_ACCESS_TOKEN=<databricks_pat_token>
export DBT_HOST=<databricks_workspace_url>
export DBT_WAREHOUSE_ID=<databricks_sql_warehouse_id>

Navigate to /dqx_demo_dbt and execute the following commands:

dbt run
dummy python model:

import yaml

from databricks.labs.dqx.config import WorkspaceFileChecksStorageConfig
from databricks.labs.dqx.engine import DQEngine
from databricks.sdk import WorkspaceClient

def model(dbt, session):
input_df = dbt.ref(“dummy_model”) # reference to the model/table that checks will be applied to

dq_engine = DQEngine(WorkspaceClient())

checks = yaml.safe_load(“””
# completeness check
— criticality: error
check:
function: is_not_null
arguments:
column: id
# uniqueness check
— criticality: warn
check:
function: is_unique
arguments:
columns:
— id
“””)

# Checks can also be loaded from a file in the workspace or delta table
# checks_path = dbt.config.get(“checks_file_path”) # get from dbt var
# checks = dq_engine.load_checks(config=WorkspaceFileChecksStorageConfig(location=checks_path))

# apply quality checks with issues reported in _warnings and _errors columns
df = dq_engine.apply_checks_by_metadata(input_df, checks)

# dbt python models must return a single DataFrame
return df
