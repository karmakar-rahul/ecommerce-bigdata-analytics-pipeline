from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *


# Spark Session
spark = SparkSession.builder \
    .appName("KafkaOrderStream") \
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

# Read Kafka Stream-
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

# Convert Kafka Value
json_df = kafka_df.selectExpr(
    "CAST(value AS STRING)"
)

orders_df = json_df.select(
    from_json(
        col("value"),
        order_schema
    ).alias("data")
).select(
    "data.*"
)

# Console Output

console_query = orders_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()
# HDFS Output
hdfs_query = orders_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option(
        "path",
        "hdfs://localhost:9000/ecommerce/streaming/orders"
    ) \
    .option(
        "checkpointLocation",
        "hdfs://localhost:9000/ecommerce/checkpoints/orders"
    ) \
    .start()

spark.streams.awaitAnyTermination()
