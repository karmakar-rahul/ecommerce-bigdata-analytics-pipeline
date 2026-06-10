from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Spark Session
spark = SparkSession.builder \
    .appName("PaymentKPIEngine") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
# Schema
order_schema = StructType([
    StructField("order_id", IntegerType()),
    StructField("customer_id", IntegerType()),
    StructField("product_id", IntegerType()),
    StructField("category", StringType()),
    StructField("quantity", IntegerType()),
    StructField("order_value", DoubleType()),
    StructField("payment_method", StringType()),
    StructField("order_status", StringType()),
    StructField("event_time", StringType())
])
kafka_df = spark.readStream \
    .format("kafka") \
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    ) \
    .option(
        "subscribe",
        "ecommerce-orders"
    ) \
    .option(
        "startingOffsets",
        "earliest"
    ) \
    .load()

# Parse JSON
orders_df = kafka_df.selectExpr(
    "CAST(value AS STRING)"
)

orders_df = orders_df.select(
    from_json(
        col("value"),
        order_schema
    ).alias("data")
).select(
    "data.*"
)

# KPI
# Revenue By Payment Method
payment_kpis = orders_df.groupBy(
    "payment_method"
).agg(
    round(
        sum("order_value"),
        2
    ).alias("revenue")
)

payment_kpis = payment_kpis.coalesce(1)

# Write Function
def write_payment_kpis(batch_df, batch_id):

    output_path = (
        f"hdfs://localhost:9000/"
        f"ecommerce/live_kpis/revenue_by_payment/"
        f"batch_{batch_id}"
    )

    batch_df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print(
        f"Payment KPI Batch {batch_id} written"
    )
# Stream Query
query = payment_kpis.writeStream \
    .outputMode("complete") \
    .foreachBatch(write_payment_kpis) \
    .start()

query.awaitTermination()
