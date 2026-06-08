from faker import Faker
import pandas as pd
import random
from tqdm import tqdm

fake = Faker()

NUM_ORDERS = 100000

customers = pd.read_csv(
    "../data/customers.csv"
)

products = pd.read_csv(
    "../data/products.csv"
)

orders = []

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash On Delivery"
]

for oid in tqdm(
    range(1, NUM_ORDERS + 1)
):

    customer = customers.sample(1).iloc[0]

    product = products.sample(1).iloc[0]

    quantity = random.randint(1, 5)

    orders.append({

        "order_id": oid,

        "customer_id":
        customer["customer_id"],

        "product_id":
        product["product_id"],

        "quantity":
        quantity,

        "unit_price":
        product["price"],

        "order_value":
        round(
            quantity *
            product["price"],
            2
        ),

        "payment_method":
        random.choice(
            payment_methods
        ),

        "order_date":
        fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )
    })

orders_df = pd.DataFrame(
    orders
)

orders_df.to_csv(
    "../data/orders.csv",
    index=False
)

print(
    f"{NUM_ORDERS} orders generated."
)
