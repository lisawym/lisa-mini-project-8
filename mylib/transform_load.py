import sqlite3
import csv
import random


def load_and_split(dataset="data/offer.csv", train_ratio=0.8, seed=42):
    """Loads the data from the CSV file,
    inserts it into a SQLite3 database, and splits it into a training and test dataset,
    using the specified random seed.
    """

    random.seed(seed)

    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("OfferDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS OfferDB")
    c.execute("CREATE TABLE OfferDB (iindex,ean,stock,price)")

    # Insert the data into the database
    c.executemany("INSERT INTO OfferDB VALUES (?,?, ?, ?)", payload)
"""

    # Shuffle the data
    data = c.fetchall()
    random.shuffle(data)

    # Split the data into training and test sets
    split = int(len(data) * train_ratio)
    train_data = data[:split]
    test_data = data[split:]

    # Save the training and test datasets to separate CSV files
    with open("train_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for row in train_data:
            writer.writerow(row)

    with open("test_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for row in test_data:
            writer.writerow(row)

    conn.commit()
    conn.close()

    return "train_data.csv", "test_data.csv"

"""


# Load and split the data, using the random seed 42
#train_data_file, test_data_file = load_and_split(seed=42)
