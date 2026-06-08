from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ExportKPIs") \
    .getOrCreate()
# Revenue By Category
spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/analytics/revenue_by_category"
).coalesce(1).write.mode(
    "overwrite"
).option(
    "header",
    True
).csv(
    "../dashboard/data/revenue_by_category"
)

# Revenue By State
spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/analytics/revenue_by_state"
).coalesce(1).write.mode(
    "overwrite"
).option(
    "header",
    True
).csv(
    "../dashboard/data/revenue_by_state"
)

# Top Products
spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/analytics/top_products"
).coalesce(1).write.mode(
    "overwrite"
).option(
    "header",
    True
).csv(
    "../dashboard/data/top_products"
)


# Payment Summary
spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/analytics/payment_summary"
).coalesce(1).write.mode(
    "overwrite"
).option(
    "header",
    True
).csv(
    "../dashboard/data/payment_summary"
)

print("Export Complete")

spark.stop()
