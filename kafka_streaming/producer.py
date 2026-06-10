from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

order_id = 1

while True:

    order = {

        "order_id": order_id,

        "customer_id": random.randint(
            1,
            100000
        ),

        "product_id": random.randint(
            1,
            10000
        ),

        "category": random.choice([
            "Electronics",
            "Fashion",
            "Home",
            "Sports",
            "Beauty",
            "Books",
            "Grocery"
        ]),

        "quantity": random.randint(
            1,
            5
        ),

        "order_value": round(
            random.uniform(
                100,
                50000
            ),
            2
        ),

        "payment_method": random.choice([
            "UPI",
            "Credit Card",
            "Debit Card",
            "Net Banking"
        ]),

        "order_status": random.choice([
            "Delivered",
            "Delivered",
            "Delivered",
            "Returned",
            "Cancelled"
        ]),

        "event_time":
        datetime.now().isoformat()

    }

    producer.send(
        "ecommerce-orders",
        order
    )

    print(
        f"Sent Order {order_id}"
    )

    order_id += 1

    time.sleep(1)
