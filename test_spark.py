from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HLDS First Test") \
    .master("local[*]") \
    .getOrCreate()

data = [("Luis", 20), ("Ana", 22), ("Carlos", 25)]

df = spark.createDataFrame(data, ["name", "age"])

df.show()
print("Total records:", df.count())

spark.stop()