
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Project directories
project_dir = Path(__file__).resolve().parent.parent
data_path = project_dir / "data" / "wildfires_prepared.parquet"

# Start Spark
spark = (
    SparkSession.builder
    .appName("Wildfire Descriptive Statistics")
    .master("local[2]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    # Load prepared dataset
    df = spark.read.parquet(str(data_path))

    print("\nTOTAL RECORDS:")
    print(df.count())

    # 1. Fire frequency by cause
    print("\nFIRES BY CAUSE:")
    df.groupBy("CAUSE_CATEGORY") \
        .count() \
        .orderBy(F.desc("count")) \
        .show(truncate=False)

    # 2. Fire size statistics by cause
    print("\nFIRE SIZE BY CAUSE (ACRES):")
    df.groupBy("CAUSE_CATEGORY").agg(
        F.count("*").alias("fire_count"),
        F.round(F.sum("FIRE_SIZE"), 2).alias("total_acres"),
        F.round(F.avg("FIRE_SIZE"), 2).alias("average_acres"),
        F.round(F.percentile_approx("FIRE_SIZE", 0.5), 2)
            .alias("median_acres"),
        F.round(F.max("FIRE_SIZE"), 2).alias("largest_fire_acres")
    ).orderBy("CAUSE_CATEGORY").show(truncate=False)

    # 3. Number of fires by year
    print("\nFIRES BY YEAR:")
    df.groupBy("FIRE_YEAR") \
        .count() \
        .orderBy("FIRE_YEAR") \
        .show(40, truncate=False)

    # 4. Burned area by year
    print("\nBURNED AREA BY YEAR (ACRES):")
    df.groupBy("FIRE_YEAR").agg(
        F.count("*").alias("fire_count"),
        F.round(F.sum("FIRE_SIZE"), 2).alias("total_acres"),
        F.round(F.avg("FIRE_SIZE"), 2).alias("average_acres")
    ).orderBy("FIRE_YEAR").show(40, truncate=False)

    # 5. Top 10 states by fire frequency
    print("\nTOP 10 STATES BY FIRE COUNT:")
    df.groupBy("STATE") \
        .count() \
        .orderBy(F.desc("count")) \
        .show(10, truncate=False)

finally:
    spark.stop()
