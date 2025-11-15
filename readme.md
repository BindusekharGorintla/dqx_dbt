dbt-DQX Quality Integration
===

<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/d315b491-8a7e-47e3-81d5-fcde6b8611f0" />


Simplified Data Quality checking at Scale for PySpark Workloads on streaming and standard DataFrames.

[![build](https://github.com/databrickslabs/dqx/actions/workflows/push.yml/badge.svg)](https://github.com/databrickslabs/dqx/actions/workflows/push.yml) 
[![codecov](https://codecov.io/github/databrickslabs/dqx/graph/badge.svg)](https://codecov.io/github/databrickslabs/dqx) 
![linesofcode](https://aschey.tech/tokei/github/databrickslabs/dqx?category=code)
[![PyPI](https://img.shields.io/pypi/v/databricks-labs-dqx?label=pypi%20package&cacheSeconds=3600)](https://pypi.org/project/databricks-labs-dqx/) 
![PyPI Downloads](https://static.pepy.tech/personalized-badge/databricks-labs-dqx?period=month&units=international_system&left_color=grey&right_color=orange&left_text=PyPI%20downloads&cacheSeconds=3600)

Running DQX with DBT projects
This demo shows how to apply data quality checks from dbt projects. The DQX quality checking is executed using dbt python models.
Prerequisites
Install dbt and required adapters:
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/7112579d-ee67-4b08-83ff-302a3b4f173e" />


Project configuration
Open profiles.yml file and update the following parameters:

http_path to specify Databricks SQL Warehouse ID (<warehouse_id>) to use to execute the dbt sql models.
(optionally) default catalog and schema to use (default: main.default).

The project is using serverless cluster by default to execute dbt python models (dqx quality checks). To change the default cluster, open dbt_project.yml file and update submission_method
Execution
Provide authentication credentials to connect to the Databricks workspace by running the following in your console:

export DBT_ACCESS_TOKEN=<databricks_pat_token>
export DBT_HOST=<databricks_workspace_url>
export DBT_WAREHOUSE_ID=<databricks_sql_warehouse_id>

Navigate to /dqx_demo_dbt and execute the following commands:

# 📖 Documentation

The complete documentation is available at: [https://databrickslabs.github.io/dqx/](https://databrickslabs.github.io/dqx/)

# 🛠️ Contribution



# 💬 Project Support

Please note that this project is provided for your exploration only and is not 
formally supported by Databricks with Service Level Agreements (SLAs). They are 
provided AS-IS, and we do not make any guarantees. Please do not 
submit a support ticket relating to any issues arising from the use of this project.

Any issues discovered through the use of this project should be filed as GitHub 
[Issues on this repository](https://github.com/databrickslabs/dqx/issues). 
They will be reviewed as time permits, but no formal SLAs for support exist.
