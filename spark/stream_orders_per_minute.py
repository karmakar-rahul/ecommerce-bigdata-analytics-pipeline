from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("OrdersPerMinute") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

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
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "ecommerce-orders") \
    .option("startingOffsets", "latest") \
    .load()

orders_df = kafka_df.selectExpr(
    "CAST(value AS STRING)"
)

orders_df = orders_df.select(
    from_json(col("value"), order_schema).alias("data")
).select("data.*")

orders_df = orders_df.withColumn(
    "event_timestamp",
    to_timestamp("event_time")
)

orders_per_minute = orders_df.groupBy(
    window(col("event_timestamp"), "1 minute")
).count()

orders_per_minute = orders_per_minute.coalesce(1)

def write_orders(batch_df, batch_id):

    output_path = (
        f"hdfs://localhost:9000/"
        f"ecommerce/live_kpis/orders_per_minute/"
        f"batch_{batch_id}"
    )

    batch_df.write \
        .mode("overwrite") \
        .parquet(output_path)

query = orders_per_minute.writeStream \
    .outputMode("complete") \
    .foreachBatch(write_orders) \
    .start()

query.awaitTermination()
