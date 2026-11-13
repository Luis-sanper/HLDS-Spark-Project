# Research Plan — US Wildfire Analysis

**Course:** Handling Large Data Sets  
**Project:** Data Processing, Analysis and Visualization using Apache Spark  
**Study period:** 1992–2024

## 1. Research Objective

The objective of this project is to investigate wildfire occurrence and burned area in the United States, focusing on differences between human-caused and naturally caused fires.

The study will examine how wildfire frequency and burned area have changed over time, and explore whether these patterns are associated with changes in climatic conditions.

## 2. Main Research Question

**How have wildfire causes and burned areas evolved in the United States between 1992 and 2024, and how are these trends related to changing climate conditions?**

## 3. Specific Research Questions

### RQ1 — Wildfire Causes

What proportion of recorded wildfires is classified as human-caused, naturally caused, or undetermined?

How do specific ignition causes differ within these categories?

### RQ2 — Wildfire Size

How does wildfire size differ between human-caused and naturally caused fires?

Are certain causes associated with a greater proportion of large fires or a larger total burned area?

### RQ3 — Historical Trends

How have wildfire frequency, average size, median size, and total burned area changed between 1992 and 2024?

Do the trends differ between human-caused and naturally caused fires?

### RQ4 — Geography and Seasonality

How do wildfire causes, frequency, and burned area vary across states and throughout the year?

### RQ5 — Climate Relationships

Are higher temperatures, lower precipitation levels, or drought conditions associated with changes in wildfire frequency or burned area?

Do these associations vary geographically or over time?

## 4. Dataset

**Source:** USDA Forest Service  
**Dataset:** Spatial Wildfire Occurrence Data for the United States, 1992–2024 (7th Edition).

The dataset contains 2,661,383 wildfire records and 38 attributes.

The original ESRI File Geodatabase has been converted into Parquet for processing with Apache Spark.

The original dataset will be preserved. Variables will only be selected, transformed, or excluded when justified by a specific analytical requirement.

## 5. Key Variables

| Variable | Purpose |
|---|---|
| FOD_ID | Identify records and check uniqueness |
| FIRE_YEAR | Historical trends |
| DISCOVERY_DATE, DISCOVERY_DOY | Monthly and seasonal patterns |
| NWCG_CAUSE_CLASSIFICATION | Human, natural, or undetermined ignition |
| NWCG_GENERAL_CAUSE | More specific ignition causes |
| FIRE_SIZE, FIRE_SIZE_CLASS | Burned area and fire-size distribution |
| STATE, COUNTY | Geographic comparisons |
| LATITUDE, LONGITUDE | Spatial analysis |
| SOURCE_SYSTEM, NWCG_REPORTING_AGENCY | Assess reporting differences and data provenance |

Additional columns may be retained if they support the research questions or help assess data quality.

## 6. Data Preparation Strategy

1. Preserve the complete source dataset.
2. Assess missing values, data types, unique identifiers, and categorical values.
3. Retain records with undetermined causes, representing them as an explicit "Unknown" category in analytical outputs.
4. Apply question-specific filters only when required and document the number of excluded records.
5. Avoid inventing missing values or discarding useful observations unnecessarily.
6. Create reproducible datasets or Spark views for subsequent analyses.

## 7. Planned Analytical Methods

The project will use PySpark DataFrames and Spark SQL to perform filtering, grouping, aggregation, and potentially joining wildfire records with external climate datasets.

For wildfire size, both mean and median values will be examined because a small number of exceptionally large fires may strongly influence averages.

The climate analysis will require additional historical temperature, precipitation, or drought data with compatible geographical and temporal coverage.

## 8. Preliminary Data Quality Findings

Initial analysis of the 2,661,383 records found:

- No missing values in seven core variables: FOD_ID, FIRE_YEAR, STATE, NWCG_CAUSE_CLASSIFICATION, FIRE_SIZE, LATITUDE, and LONGITUDE.
- No duplicated FOD_ID values.
- Recorded fire years ranging from 1992 to 2024.
- No non-positive FIRE_SIZE values.
- No coordinates outside standard latitude and longitude bounds.
- 2,034,178 human-caused fires.
- 356,409 naturally caused fires.
- 270,796 records with undetermined cause classification.

Other attributes contain substantial missing data. The relevance of these missing values will be evaluated according to the intended analysis.

## 9. Limitations and Research Considerations

- Undetermined ignition causes cannot be reliably assigned to human or natural categories.
- Reporting practices and source systems may vary across years and locations.
- The wildfire occurrence dataset does not itself provide the meteorological variables needed for climate analysis.
- Differences in wildfire frequency and burned area must be examined separately.
- Statistical associations with weather or climate variables do not, by themselves, demonstrate that climate change caused particular wildfire trends.
- Data completeness and comparability must be considered before interpreting historical patterns.

## 10. Project Deliverables

**Report 1 — Data Preparation:** Dataset description, research objectives, Spark setup, loading, quality assessment, preparation and documentation.

**Report 2 — Data Analysis:** Analytical queries, Spark optimizations, execution-time comparisons and interpretation.

**Report 3 — Visualization:** Visual representations of findings, conclusions and discussion of limitations.
