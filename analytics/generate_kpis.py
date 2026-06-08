from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, round

# -------------------------------------------------
# Spark Session
# -------------------------------------------------

spark = SparkSession.builder \
    .appName("GenerateKPIs") \
    .getOrCreate()

# -------------------------------------------------
# Load Business Dataset
# -------------------------------------------------

df = spark.read.parquet(
    "hdfs://localhost:9000/ecommerce/processed/business_dataset"
)

print(f"Total Records: {df.count():,}")

# -------------------------------------------------
# Revenue By Category
# -------------------------------------------------

revenue_by_category = df.groupBy(
    "category"
).agg(
    round(
        sum("order_value"),
        2
    ).alias("revenue")
)

revenue_by_category.write \
    .mode("overwrite") \
    .parquet(
        "hdfs://localhost:9000/ecommerce/analytics/revenue_by_category"
    )

# -------------------------------------------------
# Revenue By State
# -------------------------------------------------

revenue_by_state = df.groupBy(
    "state"
).agg(
    round(
        sum("order_value"),
        2
    ).alias("revenue")
)

revenue_by_state.write \
    .mode("overwrite") \
    .parquet(
        "hdfs://localhost:9000/ecommerce/analytics/revenue_by_state"
    )

# -------------------------------------------------
# Top Products
top_products = df.groupBy(
    "product_name"
).agg(
    count("*").alias("orders")
)

top_products.write \
    .mode("overwrite") \
    .parquet(
        "hdfs://localhost:9000/ecommerce/analytics/top_products"
    )


# Payment Summary
payment_summary = df.groupBy(
    "payment_status"
).agg(
    count("*").alias("total_transactions")
)

payment_summary.write \
    .mode("overwrite") \
    .parquet(
        "hdfs://localhost:9000/ecommerce/analytics/payment_summary"
    )

print("\nKPI Tables Generated Successfully")

spark.stop()
