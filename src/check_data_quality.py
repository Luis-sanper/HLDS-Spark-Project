
# Data quality assessment of the original wildfire dataset.
# Checks missing values, duplicate IDs, geographic coordinates,
# fire sizes, year range and ignition cause classifications.
# This script does not modify or remove any records.

from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

project_dir = Path(__file__).resolve().parent.parent
parquet_path = project_dir / "data" / "wildfires.parquet"

spark = (
    SparkSession.builder
    .appName("Wildfire Data Quality")
    .master("local[2]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    df = spark.read.parquet(str(parquet_path))


    print("\nMISSING VALUES IN ALL COLUMNS:")

    missing_counts = df.select([
        F.count(
            F.when(
                F.col(c).isNull() |
                (F.trim(F.col(c).cast("string")) == ""),
                1
            )
        ).alias(c)
        for c in df.columns
    ])

    missing_counts.show(vertical=True, truncate=False)

    print("\nINVALID COORDINATES:")

    df.select(
        F.count(
            F.when(
                ~F.col("LATITUDE").between(-90, 90) |
                ~F.col("LONGITUDE").between(-180, 180),
                1
            )
        ).alias("invalid_coordinates")
    ).show()


    # Columns relevant to our research
    important_columns = [
        "FOD_ID",
        "FIRE_YEAR",
        "STATE",
        "NWCG_CAUSE_CLASSIFICATION",
        "FIRE_SIZE",
        "LATITUDE",
        "LONGITUDE"
    ]

    print("\nMISSING VALUES:")
    df.select([
        F.count(F.when(F.col(c).isNull(), 1)).alias(c)
        for c in important_columns
    ]).show(truncate=False)

    print("\nDUPLICATE FIRE IDs:")
    duplicates = df.groupBy("FOD_ID").count().filter(F.col("count") > 1)
    print("Duplicated IDs:", duplicates.count())

    print("\nYEAR RANGE:")
    df.select(
        F.min("FIRE_YEAR").alias("min_year"),
        F.max("FIRE_YEAR").alias("max_year")
    ).show()

    print("\nINVALID FIRE SIZES:")
    df.select(
        F.count(
            F.when(F.col("FIRE_SIZE") <= 0, 1)
        ).alias("non_positive_fire_sizes")
    ).show()

    print("\nFIRE CAUSE CLASSIFICATIONS:")
    df.groupBy("NWCG_CAUSE_CLASSIFICATION") \
      .count() \
      .orderBy(F.desc("count")) \
      .show(truncate=False)

finally:
    spark.stop()
