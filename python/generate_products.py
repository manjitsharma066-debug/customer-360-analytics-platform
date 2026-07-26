"""
Generate Product Master Data
Author : Manjit Kumar Sharma
Project: Customer 360 Analytics Platform
"""

import random
import pandas as pd

from config import RAW_DATA_DIR


# Product Categories and Brands
CATEGORIES = {
    "Electronics": ["Samsung", "Apple", "Sony", "LG", "HP"],
    "Clothing": ["Nike", "Adidas", "Puma", "Levis", "Zara"],
    "Home": ["Prestige", "Philips", "Bajaj", "Milton"],
    "Furniture": ["IKEA", "Godrej", "Durian"],
    "Books": ["Penguin", "Harper", "Oxford"]
}


def generate_products(num_products=500):
    """
    Generate product master dataset and save it as CSV.
    """

    products = []

    for i in range(1, num_products + 1):

        category = random.choice(list(CATEGORIES.keys()))
        brand = random.choice(CATEGORIES[category])

        products.append({
            "product_id": f"P{i:04}",
            "product_name": f"{brand} Product {i}",
            "category": category,
            "brand": brand,
            "price": random.randint(200, 100000)
        })

    df = pd.DataFrame(products)

    output_file = RAW_DATA_DIR / "products.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("Product Dataset Generated Successfully")
    print("=" * 60)
    print(df.head())
    print("-" * 60)
    print(f"Total Products : {len(df)}")
    print(f"Output File    : {output_file}")
    print("=" * 60)

    return df


def main():
    generate_products()


if __name__ == "__main__":
    main()