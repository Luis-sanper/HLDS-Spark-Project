# Descriptive Statistics — US Wildfire Analysis

## 1. Overview

This document summarizes the initial descriptive statistics calculated using Apache Spark for the US Wildfire Analysis project.

**Dataset:** Spatial Wildfire Occurrence Data for the United States, 1992–2024 (7th Edition)  
**Source:** USDA Forest Service  
**Processing tool:** PySpark 4.3.0  
**Input:** `data/wildfires_prepared.parquet`  
**Script:** `src/descriptive_statistics.py`

The prepared dataset contains **2,661,383 wildfire records and 39 attributes**, covering the period from 1992 to 2024.

The objectives of this preliminary analysis are to describe the distribution of ignition causes, compare fire sizes, examine annual variation, and identify states with the largest numbers of recorded fires.

## 2. Wildfire Causes

| Cause category | Number of fires | Percentage |
|---|---:|---:|
| Human | 2,034,178 | 76.43% |
| Natural | 356,409 | 13.39% |
| Unknown | 270,796 | 10.18% |
| **Total** | **2,661,383** | **100%** |

Human-caused fires represent the majority of recorded wildfire incidents.

However, the number of incidents alone does not indicate which category accounts for the greatest burned area.

The Unknown category represents records whose ignition causes were not specified or could not be determined. These records are retained in the dataset.

## 3. Wildfire Size by Cause

Fire sizes are measured in acres.

| Cause | Total burned area (million acres) | Mean size (acres) | Approximate median (acres) | Largest recorded fire (acres) |
|---|---:|---:|---:|---:|
| Human | 72.27 | 35.53 | 1.0 | 1,054,153 |
| Natural | 120.14 | 337.09 | 0.2 | 606,945 |
| Unknown | 17.01 | 62.81 | 0.5 | 963,309 |

### Preliminary Interpretation

Human-caused fires are substantially more frequent than naturally caused fires.

However, naturally caused fires have a considerably greater mean burned area (337.09 acres compared with 35.53 acres for human-caused fires).

Interestingly, the approximate median size of natural fires is smaller than that of human-caused fires.

This suggests that wildfire size distributions are strongly skewed and that exceptionally large fires may have a major influence on average values.

Further analysis of percentiles, size distributions, and geographical differences will be necessary before drawing stronger conclusions.

## 4. Historical Wildfire Patterns

The dataset covers 33 years, from 1992 through 2024.

Selected annual results:

| Year | Number of fires | Total burned area (acres) | Mean fire size (acres) |
|---|---:|---:|---:|
| 1992 | 67,964 | 2,232,492.53 | 32.85 |
| 2000 | 96,507 | 7,858,843.06 | 81.43 |
| 2010 | 85,624 | 3,539,784.25 | 41.34 |
| 2015 | 78,272 | 10,247,705.74 | 130.92 |
| 2020 | 74,530 | 10,611,088.50 | 142.37 |
| 2023 | 87,084 | 2,878,385.98 | 33.05 |
| 2024 | 87,708 | 9,190,956.36 | 104.79 |

### Preliminary Interpretation

Annual wildfire counts and total burned area fluctuate considerably.

The results suggest that the number of recorded fires and the total area burned do not always follow the same pattern.

For example, 2020 had fewer recorded fires than 2000 but a greater total burned area.

These observations do not yet establish a statistically significant long-term trend.

Historical reporting differences and additional climate data will need to be considered during subsequent stages.

## 5. Geographic Distribution

The ten states with the highest number of recorded wildfire incidents are:

| Rank | State | Number of fires |
|---|---|---:|
| 1 | California (CA) | 283,285 |
| 2 | Texas (TX) | 198,785 |
| 3 | Georgia (GA) | 195,819 |
| 4 | North Carolina (NC) | 152,009 |
| 5 | Florida (FL) | 113,052 |
| 6 | Arizona (AZ) | 112,224 |
| 7 | New York (NY) | 103,819 |
| 8 | Colorado (CO) | 95,270 |
| 9 | South Carolina (SC) | 94,028 |
| 10 | Mississippi (MS) | 91,893 |

California has the highest number of recorded fires in this dataset.

However, fire frequency alone is insufficient to determine which state experiences the greatest total burned area or the most severe wildfire activity.

These comparisons will be investigated in later analytical stages.

## 6. Methods Used

Descriptive statistics were calculated with the PySpark DataFrame API.

The principal operations included:

- `groupBy()` to group records by cause, year, or state.
- `count()` to calculate wildfire frequency.
- `sum()` to calculate total burned area.
- `avg()` to calculate mean fire size.
- `percentile_approx()` to estimate median fire size.
- `max()` to identify the largest recorded fire size.
- `orderBy()` to sort aggregated results.

The calculations were performed on the prepared Parquet dataset using Apache Spark in local mode.

## 7. Limitations

- Unknown causes cannot be reliably classified as human or natural.
- The fire-size distribution is highly skewed, so means should be interpreted alongside medians and other distributional statistics.
- Changes in reporting systems and data collection practices may influence historical comparisons.
- The dataset does not independently establish whether climate change has caused changes in wildfire frequency or burned area.
- No external climate dataset has yet been integrated.
- The results are descriptive; formal trend analysis and more detailed comparisons are planned for the next project stage.

## 8. Next Steps

The subsequent analysis will focus on:

1. Comparing wildfire frequency and burned area by cause over time.
2. Examining the distribution of large fires and extreme burned-area values.
3. Investigating geographical and seasonal differences.
4. Integrating historical climate data where appropriate.
5. Applying Spark optimization techniques and measuring execution times under comparable conditions.

These analyses will provide the basis for Report 2 and the visualizations required in Report 3.
