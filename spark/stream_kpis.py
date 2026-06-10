from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


# Spark Session
spark = SparkSession.builder \
    .appName("LiveKPIEngine") \
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


# Read Kafka Stream
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

#json
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

revenue_by_category = orders_df.groupBy(
    "category"
).agg(
    round(
        sum("order_value"),
        2
    ).alias("revenue")
)
revenue_by_category = revenue_by_category.coalesce(1)
# Write KPI
# Debug Stream
def write_revenue(batch_df, batch_id):

    output_path = (
        f"hdfs://localhost:9000/"
        f"ecommerce/live_kpis/revenue_by_category/"
        f"batch_{batch_id}"
    )

    batch_df.write \
        .mode("overwrite") \
        .parquet(output_path)

    print(
        f"Batch {batch_id} written successfully"
    )
query = revenue_by_category.writeStream \
    .outputMode("complete") \
    .foreachBatch(write_revenue) \
    .start()

query.awaitTermination()

