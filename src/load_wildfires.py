
from pathlib import Path
from pyspark.sql import SparkSession

# Locate the project and dataset
project_dir = Path(__file__).resolve().parent.parent
parquet_path = project_dir / "data" / "wildfires.parquet"

# Start Apache Spark
spark = (
    SparkSession.builder
    .appName("Wildfire Data Analysis")
    .master("local[2]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:
    # Load the Parquet dataset
    df = spark.read.parquet(str(parquet_path))

    # Display dataset information
    print("\nTotal records:", df.count())
    print("Total columns:", len(df.columns))

    print("\nDataset schema:")
    df.printSchema()

    print("\nFirst 5 records:")
    df.select(
        "FIRE_YEAR",
        "STATE",
        "NWCG_CAUSE_CLASSIFICATION",
        "FIRE_SIZE"
    ).show(5, truncate=False)

finally:
    spark.stop()
