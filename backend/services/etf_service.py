import pandas as pd
from typing import Dict
from fastapi import File

ETF_DATA = None
# Assuming the prices data will be used for all etfs provided
PRICES_DATA = pd.read_csv("data/bankofmontreal-e134q-1arsjzss-prices.csv")


"""
we can just return basic success or error message and some stats so we can also check if the data was
parsed correctly.

for verifying the total wegith I had to use range because of floating point precision issues. An ETF
can return 0.999 so this condition will catch that.

Sources used:
https://www.w3schools.com/python/pandas/pandas_csv.asp
"""

def upload_etf(file: File) -> Dict:
    global ETF_DATA
    
    try:
        ETF_DATA = pd.read_csv(file) # convert csv to pandas dataframe basically a table
        RequiredColumns = ['name', 'weight']
        
        # check if the file has the required columns
        if ETF_DATA.columns.tolist() != RequiredColumns:
            raise ValueError("File must contain 'name' and 'weight' columns")

        #  since etfs need to be weighted to 100% we can check if the total weight is 1
        total_weight = ETF_DATA['weight'].sum() 

        if not (0.99 <= total_weight <= 1.01):
            raise ValueError("Total weight must be 1")

        return {
            "message": "File uploaded successfully",
            "constituents": len(ETF_DATA),
            "total_weight": round(total_weight, 2)
        }

    except Exception as e:
        raise e

