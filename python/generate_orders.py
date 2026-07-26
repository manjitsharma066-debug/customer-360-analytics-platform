"""
Generate Sales Orders Data
Author : Manjit Kumar Sharma
Project: Customer 360 Analytics Platform
"""

import random
import pandas as pd
from faker import Faker

from config import RAW_DATA_DIR

# Faker Object
fake = Faker("en_IN")

# Master Data Files
CUSTOMERS_FILE = RAW_DATA_DIR / "customers.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "products.csv"
STORES_FILE = RAW_DATA_DIR / "stores.csv"

# Static Lookup Values
PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

ORDER_STATUS = [
    "Delivered",
    "Cancelled",
    "Returned"
]


def generate_orders(num_orders=100000):
    """
    Generate order transaction dataset and save it as CSV.
    """

    # Load Master Data
    customers = pd.read_csv(CUSTOMERS_FILE)
    products = pd.read_csv(PRODUCTS_FILE)
    stores = pd.read_csv(STORES_FILE)

    orders = []

    for i in range(1, num_orders + 1):

        customer = customers.sample(1).iloc[0]
        product = products.sample(1).iloc[0]
        store = stores.sample(1).iloc[0]

        quantity = random.randint(1, 5)
        unit_price = product["price"]
        total_amount = quantity * unit_price

        orders.append({
            "order_id": f"O{i:06}",
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "store_id": store["store_id"],
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount,
            "payment_method": random.choice(PAYMENT_METHODS),
            "order_status": random.choices(
                ORDER_STATUS,
                weights=[90, 5, 5]
            )[0]
        })

    df = pd.DataFrame(orders)

    output_file = RAW_DATA_DIR / "orders.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("Orders Dataset Generated Successfully")
    print("=" * 60)
    print(df.head())
    print("-" * 60)
    print(f"Total Orders : {len(df)}")
    print(f"Output File  : {output_file}")
    print("=" * 60)

    return df


def main():
    generate_orders()


if __name__ == "__main__":
    main()