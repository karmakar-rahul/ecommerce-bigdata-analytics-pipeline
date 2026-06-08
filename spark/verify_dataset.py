from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("VerifyDataset") \
    .getOrCreate()

df = spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/processed/business_dataset"
)

df.printSchema()

df.show(5, truncate=False)

spark.stop()
