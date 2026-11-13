# US Wildfire Analysis using Apache Spark

## Project Overview

This project is developed for the **Handling Large Data Sets** course at VIZJA University.

The objective is to analyze historical wildfire patterns in the United States using Apache Spark, focusing on wildfire causes, temporal trends, geographical distribution, and burned area.

The project will also explore potential relationships between wildfire activity and climate conditions.

## Dataset

**Source:** USDA Forest Service  
**Dataset:** Spatial Wildfire Occurrence Data for the United States (1992–2024), 7th Edition.

- 2,661,383 wildfire records
- 38 attributes
- Geographic, temporal, and fire-related information

Dataset reference: https://doi.org/10.2737/RDS-2013-0009.7

## Technologies

- Python 3.13
- Apache Spark / PySpark
- Spark SQL
- PyArrow and Parquet
- Pyogrio and GeoPandas
- Git and GitHub

## Project Stages

### Report 1 — Data Preparation (November 18, 2026)
- Configure Apache Spark.
- Import and validate the dataset.
- Clean and prepare the data.
- Generate descriptive statistics.
- Document the preparation process.

### Report 2 — Data Analysis (December 23, 2026)
- Implement analytical queries.
- Apply Spark optimization techniques.
- Compare query execution times.
- Interpret the results.

### Report 3 — Visualization (January 14, 2027)
- Create meaningful visualizations.
- Interpret wildfire patterns.
- Present findings, limitations and conclusions.

## Project Status

**Current stage:** Report 1 — Data Preparation.

The original geodatabase has been converted to Parquet. Loading and validation with Apache Spark are the next steps.

## Notes

Large datasets and local Python environments are excluded from the Git repository. The source dataset can be obtained from the USDA Forest Service.
