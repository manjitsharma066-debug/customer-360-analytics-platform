"""
Generate Store Master Data
Author : Manjit Kumar Sharma
Project: Customer 360 Analytics Platform
"""

import random
import pandas as pd
from faker import Faker

from config import RAW_DATA_DIR

# Faker Object
fake = Faker("en_IN")

# Available Store Regions
REGIONS = ["North", "South", "East", "West"]


def generate_stores(num_stores=100):
    """
    Generate store master dataset and save it as CSV.
    """

    stores = []

    for i in range(1, num_stores + 1):

        stores.append({
            "store_id": f"S{i:03}",
            "store_name": f"RetailMart Store {i}",
            "city": fake.city(),
            "state": fake.state(),
            "region": random.choice(REGIONS)
        })

    df = pd.DataFrame(stores)

    output_file = RAW_DATA_DIR / "stores.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("Store Dataset Generated Successfully")
    print("=" * 60)
    print(df.head())
    print("-" * 60)
    print(f"Total Stores : {len(df)}")
    print(f"Output File  : {output_file}")
    print("=" * 60)

    return df


def main():
    generate_stores()


if __name__ == "__main__":
    main()