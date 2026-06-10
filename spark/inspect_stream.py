from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("InspectStream") \
    .getOrCreate()

df = spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/streaming/orders"
)

print("\nSCHEMA")
df.printSchema()

print("\nSAMPLE RECORDS")
df.show(10, truncate=False)

print("\nTOTAL RECORDS")
print(df.count())
