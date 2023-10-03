import argparse

from mylib.extract import extract
from mylib.transform_load import load_and_split
from mylib.query import query

# Define the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--extract", action="store_true", help="Extract the data.")
parser.add_argument(
    "--transform_load", action="store_true", help="Transform and load the data."
)
parser.add_argument("--query", action="store_true", help="Query the data.")

# Parse the command-line arguments
args = parser.parse_args()

# Perform the requested ETL task
if args.extract:
    extract()
elif args.transform_load:
    load_and_split()
elif args.query:
    query()
