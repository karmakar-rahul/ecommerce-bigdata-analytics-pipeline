from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Create Spark Session
spark = SparkSession.builder \
    .appName("EcommerceETL") \
    .config(
        "spark.hadoop.fs.defaultFS",
        "hdfs://localhost:9000"
    ) \
    .getOrCreate()

# Load Data From HDFS
customers = spark.read.csv(
    "hdfs://localhost:9000/ecommerce/raw/customers.csv",
    header=True,
    inferSchema=True
)

products = spark.read.csv(
    "hdfs://localhost:9000/ecommerce/raw/products.csv",
    header=True,
    inferSchema=True
)

orders = spark.read.csv(
    "hdfs://localhost:9000/ecommerce/raw/orders.csv",
    header=True,
    inferSchema=True
)

payments = spark.read.csv(
    "hdfs://localhost:9000/ecommerce/raw/payments.csv",
    header=True,
    inferSchema=True
)

# Basic Validation
print("\nCustomers:")
customers.printSchema()

print("\nProducts:")
products.printSchema()

print("\nOrders:")
orders.printSchema()

print("\nPayments:")
payments.printSchema()

# Join Orders + Customers
order_customer = orders.join(
    customers,
    on="customer_id",
    how="left"
)


# Join Products
order_customer_product = order_customer.join(
    products,
    on="product_id",
    how="left"
)

final_df = order_customer_product.join(
    payments.select(
        "order_id",
        "payment_status"
    ),
    on="order_id",
    how="left"
)


# Select Final Columns
final_df = final_df.select(

    "order_id",

    "customer_id",
    "customer_name",
    "state",

    "product_id",
    "product_name",
    "category",

    "quantity",

    "order_value",

    "payment_method",
    "payment_status",

    "order_date"
)
final_df.show(10, False)
final_df.write \
    .mode("overwrite") \
    .parquet(
        "hdfs://localhost:9000/ecommerce/processed/business_dataset"
    )

print(
    "\nBusiness Dataset Saved Successfully"
)

spark.stop()
