# dbt-DQX Quality Integration

<img width="150" height="150" alt="image" src="https://github.com/user-attachments/assets/d315b491-8a7e-47e3-81d5-fcde6b8611f0" />

Simplified Data Quality checking at scale for PySpark workloads on streaming and standard DataFrames.

[![build](https://github.com/databrickslabs/dqx/actions/workflows/push.yml/badge.svg)](https://github.com/databrickslabs/dqx/actions/workflows/push.yml) 
[![codecov](https://codecov.io/github/databrickslabs/dqx/graph/badge.svg)](https://codecov.io/github/databrickslabs/dqx) 
![linesofcode](https://aschey.tech/tokei/github/databrickslabs/dqx?category=code)
[![PyPI](https://img.shields.io/pypi/v/databricks-labs-dqx?label=pypi%20package&cacheSeconds=3600)](https://pypi.org/project/databricks-labs-dqx/) 
![PyPI Downloads](https://static.pepy.tech/personalized-badge/databricks-labs-dqx?period=month&units=international_system&left_color=grey&right_color=orange&left_text=PyPI%20downloads&cacheSeconds=3600)

## Running DQX with DBT Projects

This demo shows how to apply data quality checks from dbt projects. The DQX quality checking is executed using dbt Python models.

### Prerequisites

To get started, install dbt and the required adapters:

![Install dbt](https://github.com/user-attachments/assets/7112579d-ee67-4b08-83ff-302a3b4f173e)

### Project Configuration

1. Open the `profiles.yml` file and update the following parameters:
   - **http_path**: Specify the Databricks SQL Warehouse ID (`<warehouse_id>`) to use for executing dbt SQL models.
   - **default catalog and schema** (optional, default: `main.default`).

2. The project uses a **serverless cluster** by default to execute dbt Python models (DQX quality checks). To change the default cluster, open the `dbt_project.yml` file and update the **submission_method**.

### Execution

Provide authentication credentials to connect to the Databricks workspace by running the following commands in your console:

```bash
export DBT_ACCESS_TOKEN=<databricks_pat_token>
export DBT_HOST=<databricks_workspace_url>
export DBT_WAREHOUSE_ID=<databricks_sql_warehouse_id>

Navigate to /dqx_demo_dbt and execute the following commands:

# 📖 Documentation

The complete documentation is available at: [https://databrickslabs.github.io/dqx/](https://databrickslabs.github.io/dqx/)


