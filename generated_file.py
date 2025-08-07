import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
from loguru import logger as log

# Initialize Faker
fake = Faker("id_ID")

# Set the range for datetime
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)


# Function to generate a random datetime between a given range
def random_date(start, end):
    return start + timedelta(
        seconds=np.random.randint(0, int((end - start).total_seconds()))
    )


# Function to generate each row
def generateSalesRow(names: list, prices: list):
    return {
        "date": random_date(start_date, end_date),
        "name": random.choice(names),
        "market_area": fake.administrative_unit(),
        "number_of_sales": fake.random_int(min=1, max=75),
        "pricing_unit": random.choice(prices),
    }


# Function to generate whole dataset
def generateSales(num: int):
    """
    param :
    - num = nummber of dataset
    """
    try:
        sales_list = [
            "Diah",
            "Wahyu",
            "Lisa",
            "Anton",
            "Malik",
            "Riana",
            "Rafi",
            "Bela",
            "Budi",
        ]
        pricing_units = [50000, 100000, 150000]

        log.info("Flow - Generating Data Rows")
        generated_data = [
            generateSalesRow(names=sales_list, prices=pricing_units) for _ in range(num)
        ]

        log.info("Flow - Saving dataframe into csv")
        generated_dataframe = pd.DataFrame(generated_data)
        generated_dataframe.to_csv("sales_generated.csv", index=False)
    except Exception as e:
        log.error(f"Flow error - error occured as {e}")


if __name__ == "__main__":
    """
    All entry point
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers", help="Numbers of data to generate", type=int)
    args = parser.parse_args()

    if args.numbers:
        generateSales(num=args.numbers)
    else:
        log.error("Specify numbers")
