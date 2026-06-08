import pandas as pd
from tqdm import tqdm

orders = pd.read_csv(
    "../data/orders.csv"
)

payments = []

for idx, row in tqdm(
        orders.iterrows(),
        total=len(orders),
        desc="Generating Payments"
):

    order_status = row[
        "order_status"
    ]

    if order_status == "Cancelled":

        payment_status = \
            "Refunded"

    elif order_status == "Returned":

        payment_status = \
            "Refunded"

    else:

        payment_status = \
            "Success"

    payments.append({

        "payment_id":
        idx + 1,

        "order_id":
        row["order_id"],

        "payment_amount":
        row["order_value"],

        "payment_method":
        row["payment_method"],

        "payment_status":
        payment_status,

        "payment_date":
        row["order_date"]

    })

payments_df = pd.DataFrame(
    payments
)

payments_df.to_csv(
    "../data/payments.csv",
    index=False
)

print(
    f"{len(payments_df):,} payments generated."
)
