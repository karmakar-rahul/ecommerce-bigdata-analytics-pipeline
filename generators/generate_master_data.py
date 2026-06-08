from faker import Faker
import pandas as pd
import random

fake = Faker()

# ==================================================
# CONFIGURATION
# ==================================================

NUM_CUSTOMERS = 100000
NUM_PRODUCTS = 10000

# ==================================================
# CUSTOMER GENERATION
# ==================================================

print("Generating customers...")

customers = []

for cid in range(1, NUM_CUSTOMERS + 1):

    r = random.random()

    if r < 0.60:
        segment = "Budget"
    elif r < 0.90:
        segment = "Regular"
    else:
        segment = "Premium"

    customers.append({
        "customer_id": cid,
        "customer_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "city": fake.city(),
        "state": fake.state(),
        "segment": segment,
        "registration_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "../data/customers.csv",
    index=False
)

print("Customers generated.")

# ==================================================
# PRODUCT GENERATION
# ==================================================

print("Generating products...")

categories = {

    "Electronics": {
        "products": [
            "Laptop",
            "Smartphone",
            "Tablet",
            "Monitor",
            "Headphones"
        ],
        "price_range": (
            15000,
            120000
        )
    },

    "Fashion": {
        "products": [
            "T-Shirt",
            "Jeans",
            "Jacket",
            "Shoes",
            "Watch"
        ],
        "price_range": (
            500,
            10000
        )
    },

    "Books": {
        "products": [
            "Novel",
            "Biography",
            "Textbook",
            "Magazine",
            "Comics"
        ],
        "price_range": (
            100,
            2000
        )
    },

    "Home": {
        "products": [
            "Chair",
            "Table",
            "Lamp",
            "Sofa",
            "Curtain"
        ],
        "price_range": (
            1000,
            50000
        )
    },

    "Sports": {
        "products": [
            "Football",
            "Cricket Bat",
            "Basketball",
            "Tennis Racket",
            "Yoga Mat"
        ],
        "price_range": (
            500,
            20000
        )
    },

    "Beauty": {
        "products": [
            "Face Wash",
            "Shampoo",
            "Perfume",
            "Cream",
            "Lipstick"
        ],
        "price_range": (
            100,
            5000
        )
    },

    "Grocery": {
        "products": [
            "Rice",
            "Oil",
            "Milk",
            "Tea",
            "Coffee"
        ],
        "price_range": (
            20,
            2000
        )
    }
}

products = []

for pid in range(1, NUM_PRODUCTS + 1):

    category = random.choice(
        list(categories.keys())
    )

    product_name = random.choice(
        categories[category]["products"]
    )

    min_price, max_price = \
        categories[category]["price_range"]

    products.append({

        "product_id": pid,

        "product_name": product_name,

        "category": category,

        "price": round(
            random.uniform(
                min_price,
                max_price
            ),
            2
        ),

        "stock_quantity":
        random.randint(
            100,
            10000
        )
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "../data/products.csv",
    index=False
)

print("Products generated.")

print("\nMaster Data Generation Complete")
print(f"Customers : {len(customers_df):,}")
print(f"Products  : {len(products_df):,}")
