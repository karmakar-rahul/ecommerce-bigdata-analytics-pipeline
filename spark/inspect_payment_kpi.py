from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("InspectPaymentKPI") \
    .getOrCreate()

df = spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/live_kpis/revenue_by_payment/batch_5"
)

df.show(truncate=False)
