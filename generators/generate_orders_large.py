from faker import Faker
import pandas as pd
import random
from tqdm import tqdm

fake = Faker()

# ==================================================
# CONFIG
# ==================================================

NUM_ORDERS = 1_000_000

# ==================================================
# LOAD DATA
# ==================================================

customers = pd.read_csv("../data/customers.csv")
products = pd.read_csv("../data/products.csv")

print(f"Loaded {len(customers):,} customers")
print(f"Loaded {len(products):,} products")

# ==================================================
# CUSTOMER SEGMENTS
# ==================================================

segment_preferences = {

    "Budget": [
        "Grocery",
        "Books",
        "Beauty"
    ],

    "Regular": [
        "Fashion",
        "Home",
        "Sports"
    ],

    "Premium": [
        "Electronics",
        "Fashion"
    ]
}

# ==================================================
# BUYER TYPES
# ==================================================

customer_activity = {}

for customer_id in customers["customer_id"]:

    r = random.random()

    if r < 0.10:
        customer_activity[customer_id] = "Heavy"

    elif r < 0.40:
        customer_activity[customer_id] = "Regular"

    else:
        customer_activity[customer_id] = "Casual"

# ==================================================
# CUSTOMER WEIGHTS
# ==================================================

weighted_customer_ids = []

for customer_id in customers["customer_id"]:

    activity = customer_activity[customer_id]

    if activity == "Heavy":
        weight = 10

    elif activity == "Regular":
        weight = 4

    else:
        weight = 1

    weighted_customer_ids.extend(
        [customer_id] * weight
    )

# ==================================================
# PRODUCT LOOKUP
# ==================================================

products_by_category = {}

for category in products["category"].unique():

    products_by_category[
        category
    ] = products[
        products["category"] == category
    ]

# ==================================================
# PRODUCT POPULARITY
# ==================================================

product_popularity = {}

for product_id in products["product_id"]:

    product_popularity[product_id] = \
        random.randint(1, 100)

# ==================================================
# PAYMENT METHODS
# ==================================================

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash On Delivery"
]

payment_weights = [
    45,
    20,
    15,
    10,
    10
]

# ==================================================
# ORDERS
# ==================================================

orders = []

for order_id in tqdm(
        range(1, NUM_ORDERS + 1),
        desc="Generating Orders"
):

    # -----------------------------------------
    # Customer Selection
    # -----------------------------------------

    customer_id = random.choice(
        weighted_customer_ids
    )

    customer = customers[
        customers["customer_id"]
        == customer_id
    ].iloc[0]

    segment = customer["segment"]

    preferred_category = random.choice(
        segment_preferences[segment]
    )

    category_products = \
        products_by_category[
            preferred_category
        ]

    product = category_products.sample(
        1
    ).iloc[0]

    # -----------------------------------------
    # Product
    # -----------------------------------------

    product_id = product["product_id"]

    unit_price = float(
        product["price"]
    )

    quantity = random.randint(
        1,
        5
    )

    # -----------------------------------------
    # Seasonality
    # -----------------------------------------

    month_weights = {

        1: 0.7,
        2: 0.8,

        3: 1.0,
        4: 1.0,
        5: 1.0,

        6: 1.1,
        7: 1.1,
        8: 1.1,

        9: 1.2,
        10: 1.4,

        11: 2.0,
        12: 2.2
    }

    order_date = fake.date_time_between(
        start_date="-2y",
        end_date="now"
    )

    month = order_date.month

    seasonal_multiplier = \
        month_weights[month]

    order_value = round(
        quantity *
        unit_price *
        seasonal_multiplier,
        2
    )

    # -----------------------------------------
    # Status
    # -----------------------------------------

    order_status = random.choices(

        [
            "Delivered",
            "In Transit",
            "Returned",
            "Cancelled"
        ],

        weights=[
            90,
            5,
            3,
            2
        ]

    )[0]

    # -----------------------------------------
    # Payment
    # -----------------------------------------

    payment_method = random.choices(

        payment_methods,

        weights=payment_weights

    )[0]

    # -----------------------------------------
    # Save
    # -----------------------------------------

    orders.append({

        "order_id":
        order_id,

        "customer_id":
        customer_id,

        "product_id":
        product_id,

        "product_category":
        preferred_category,

        "quantity":
        quantity,

        "unit_price":
        unit_price,

        "order_value":
        order_value,

        "payment_method":
        payment_method,

        "order_status":
        order_status,

        "order_date":
        order_date

    })

# ==================================================
# SAVE
# ==================================================

orders_df = pd.DataFrame(
    orders
)

orders_df.to_csv(
    "../data/orders.csv",
    index=False
)

print("\nOrders Generated")
print(f"Total Orders: {len(orders_df):,}")
