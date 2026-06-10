from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("InspectKPI") \
    .getOrCreate()

df = spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/live_kpis/revenue_by_category/batch_5"
)

df.show(truncate=False)
