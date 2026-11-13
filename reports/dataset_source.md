# Dataset Source — US Wildfire Analysis

## 1. Data Source

**Dataset:** Spatial Wildfire Occurrence Data for the United States, 1992–2024 (7th Edition)

**Provider:** United States Department of Agriculture (USDA), Forest Service.

**Official reference:** https://doi.org/10.2737/RDS-2013-0009.7

**Geodatabase download:**

https://data.fs.usda.gov/geodata/edw/edw_resources/fc/S_USA.Fire_FPA_FOD_7th_Fires.gdb.zip

## 2. Dataset Description

The dataset contains historical wildfire occurrence records across the United States.

- **Total records:** 2,661,383
- **Attributes:** 38
- **Time period:** 1992–2024
- **Original format:** ESRI File Geodatabase
- **Processing format:** Apache Parquet

The dataset provides information about ignition causes, discovery dates, wildfire sizes, geographic locations, reporting agencies, and other incident-related attributes.

Wildfire size is recorded in acres.

## 3. Dataset Selection

This dataset was selected because it:

- Contains more than 100,000 records, meeting the course requirements.
- Covers 33 years of historical wildfire records.
- Includes human, natural, and undetermined ignition classifications.
- Provides fire-size information for comparing burned areas.
- Includes temporal and geographical attributes for studying historical patterns.
- Can potentially be combined with external climate datasets.

## 4. Data Acquisition and Preparation

The initial Shapefile version provided only 405,032 accessible records, covering 1992–2009.

To obtain the complete dataset, the ESRI File Geodatabase version was downloaded and inspected using Pyogrio.

The complete Geodatabase contained 2,661,383 records and 38 attributes.

It was converted to Apache Parquet in batches of 50,000 records using Python, Pyogrio, and PyArrow.

Apache Spark subsequently loaded the Parquet dataset successfully, verifying the full record count and schema.

## 5. Preliminary Data Quality

Initial checks using PySpark found:

- No duplicated `FOD_ID` values.
- No missing values in the seven core attributes examined.
- No non-positive `FIRE_SIZE` values.
- No latitude or longitude values outside standard coordinate bounds.
- Several secondary attributes containing substantial missing data.
- 270,796 records with undetermined ignition cause classification.

The original dataset will be preserved, and any later transformations or exclusions will be documented.

## 6. Limitations

The dataset combines wildfire records from different reporting systems and agencies. Reporting completeness and consistency may vary over time or between locations.

Some wildfire causes are undetermined, and several secondary attributes contain missing information.

The dataset does not directly include the historical temperature, precipitation, or drought measurements needed for the climate component of the research. Additional sources will be required.

## 7. Data Storage

The original Geodatabase and converted Parquet files are stored locally in the `data/` directory.

This directory is excluded from GitHub using `.gitignore` because the dataset files are large. The repository contains the scripts needed to reproduce the preparation process.
