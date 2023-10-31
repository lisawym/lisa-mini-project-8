import argparse
import psutil
import os
import time

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
parser.add_argument("--all", action="store_true", help="Run all ETL tasks.")
parser.add_argument("--all_10", action="store_true", help="Run all ETL tasks 10 times.")

# Parse the command-line arguments
args = parser.parse_args()

# Perform the requested ETL task
if args.all:
    start_time = time.time()
    process = psutil.Process()
    memory_info = process.memory_info()
    extract()
    load_and_split()
    query("OfferDB.db")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Memory used: {memory_info.rss / 1024 / 1024:.2f} MB")
    avg_cpu_usage = psutil.cpu_percent(interval=0.3)
    print(f"Average CPU usage: {avg_cpu_usage}%")
elif args.all_10:
    total_time = 0
    total_memory = 0
    total_cpu_usage = 0
    for i in range(10):
        start_time = time.time()
        process = psutil.Process()
        memory_info = process.memory_info()
        extract()
        load_and_split()
        query("OfferDB.db")
        end_time = time.time()
        total_time += end_time - start_time
        total_memory += memory_info.rss / 1024 / 1024
        total_cpu_usage += psutil.cpu_percent(interval=0.3)
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time taken: {total_time / 10:.2f} seconds")
    print(f"Total memory used: {total_memory:.2f} MB")
    print(f"Average memory used: {total_memory / 10:.2f} MB")
    print(f"Total average CPU usage: {total_cpu_usage:.2f}%")
    print(f"Average CPU usage: {total_cpu_usage / 10:.2f}%")
elif args.extract:
    start_time = time.time()
    process = psutil.Process()
    memory_info = process.memory_info()
    extract()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Memory used: {memory_info.rss / 1024 / 1024:.2f} MB")
    avg_cpu_usage = psutil.cpu_percent(interval=0.3)
    print(f"Average CPU usage: {avg_cpu_usage}%")
elif args.transform_load:
    start_time = time.time()
    process = psutil.Process()
    memory_info = process.memory_info()
    load_and_split()
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Memory used: {memory_info.rss / 1024 / 1024:.2f} MB")
    avg_cpu_usage = psutil.cpu_percent(interval=0.3)
    print(f"Average CPU usage: {avg_cpu_usage}%")
elif args.query:
    start_time = time.time()
    process = psutil.Process()
    memory_info = process.memory_info()
    query("OfferDB.db")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Memory used: {memory_info.rss / 1024 / 1024:.2f} MB")
    avg_cpu_usage = psutil.cpu_percent(interval=0.3)
    print(f"Average CPU usage: {avg_cpu_usage}%")
