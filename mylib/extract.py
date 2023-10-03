"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

"""

import requests


def extract(
    url="https://github.com/datablist/sample-csv-files/raw/main/files/offers/offers-1000.csv",
    file_path="data/offer.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


#     kaggle competitions download -c home-credit-default-risk

# import subprocess

# def extract(command):


#     command = "
#     "

#     try:
#         # Execute the shell command
#         subprocess.run(command, shell=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")


# extract("")
