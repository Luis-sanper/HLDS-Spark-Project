
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Project directories
project_dir = Path(__file__).resolve().parent.parent

input_path = project_dir / "data" / "wildfires.parquet"
output_path = project_dir / "data" / "wildfires_prepared.parquet"

# Start Spark
spark = (
    SparkSession.builder
    .appName("Prepare Wildfire Dataset")
    .master("local[2]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    # Load the original dataset
    df = spark.read.parquet(str(input_path))

    print("Original records:", df.count())
    print("Original columns:", len(df.columns))

    # Rename the cause classification column
    prepared = df.withColumnRenamed(
        "NWCG_CAUSE_CLASSIFICATION",
        "CAUSE_CATEGORY"
    )

    # Simplify the cause classification values
    prepared = prepared.withColumn(
        "CAUSE_CATEGORY",
        F.when(
            F.col("CAUSE_CATEGORY") == "Human",
            "Human"
        ).when(
            F.col("CAUSE_CATEGORY") == "Natural",
            "Natural"
        ).when(
            F.col("CAUSE_CATEGORY") ==
            "Missing data/not specified/undetermined",
            "Unknown"
        ).otherwise(F.col("CAUSE_CATEGORY"))
    )

    # Extract month from discovery date
    prepared = prepared.withColumn(
        "DISCOVERY_MONTH",
        F.month("DISCOVERY_DATE")
    )

    # Save the prepared dataset separately
    prepared.write.mode("overwrite").parquet(str(output_path))

    # Verify the saved dataset
    result = spark.read.parquet(str(output_path))

    print("\nPrepared records:", result.count())
    print("Prepared columns:", len(result.columns))

    print("\nCause categories:")
    result.groupBy("CAUSE_CATEGORY") \
        .count() \
        .orderBy("CAUSE_CATEGORY") \
        .show(truncate=False)

    print("\nDiscovery months:")
    result.groupBy("DISCOVERY_MONTH") \
        .count() \
        .orderBy("DISCOVERY_MONTH") \
        .show(12)

    print("\nPrepared dataset saved to:")
    print(output_path)

finally:
    spark.stop()
