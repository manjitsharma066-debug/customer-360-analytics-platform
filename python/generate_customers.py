"""
Generate Customer Master Data
Author : Manjit Kumar Sharma
Project: Customer 360 Analytics Platform
"""

import random
import pandas as pd
from faker import Faker

from config import RAW_DATA_DIR

# Faker Object
fake = Faker("en_IN")


def generate_customers(num_customers=5000):
    """
    Generate customer master dataset and save it as CSV.
    """

    customers = []

    for i in range(1, num_customers + 1):

        customers.append({
            "customer_id": f"C{i:05}",
            "customer_name": fake.name(),
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 70),
            "city": fake.city(),
            "state": fake.state(),
            "join_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })

    df = pd.DataFrame(customers)

    output_file = RAW_DATA_DIR / "customers.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("Customer Dataset Generated Successfully")
    print("=" * 60)
    print(df.head())
    print("-" * 60)
    print(f"Total Customers : {len(df)}")
    print(f"Output File     : {output_file}")
    print("=" * 60)

    return df


def main():
    generate_customers()


if __name__ == "__main__":
    main()