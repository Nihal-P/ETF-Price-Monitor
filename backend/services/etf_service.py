import pandas as pd
from typing import Dict
from fastapi import File

ETF_DATA = None
# Assuming the prices data will be used for all etfs provided
PRICES_DATA = pd.read_csv("data/bankofmontreal-e134q-1arsjzss-prices.csv")


def upload_etf(file: File) -> Dict:
    """
    Parse and store the uploaded ETF CSV file

    Args:
        file (File): The ETF CSV file to upload

    Returns:
        Dict: A dictionary containing the result of the upload operation

    Raises:
        ValueError: If the file is not a CSV file
        ValueError: If the file does not contain the required columns
        ValueError: If the total weight is not 1

    Sources used:
        https://www.w3schools.com/python/pandas/pandas_csv.asp
    """

    global ETF_DATA
    
    try:
        ETF_DATA = pd.read_csv(file) # convert csv to pandas dataframe basically a table
        RequiredColumns = ['name', 'weight']
        
        # check if the file has the required columns
        if ETF_DATA.columns.tolist() != RequiredColumns:
            raise ValueError("File must contain 'name' and 'weight' columns")

        #  since etfs need to be weighted to 100% we can check if the total weight is 1
        total_weight = ETF_DATA['weight'].sum() 

        # for verifying the total wegith I had to use range because of floating point precision issues. An ETF can return 0.999 so this condition will catch that.
        if not (0.99 <= total_weight <= 1.01):
            raise ValueError("Total weight must be 1")

        return {
            "message": "File uploaded successfully",
            "constituents": len(ETF_DATA),
            "total_weight": round(total_weight, 2)
        }

    except Exception as e:
        raise e


def get_constituents() -> list:
    """
    Get the constituents of the ETF with their weight and latest price

    Returns:
        list: A list of constituents with their weight and latest price

    Raises:
        ValueError: If the ETF data is not found

    Sources used:
        https://stackoverflow.com/a/67922262
    """

    if ETF_DATA is None:
        raise ValueError("ETF data not found")
    
    # getting the last row of the prices data
    last_prices = PRICES_DATA.iloc[-1]
    constituents = []

    for i, row in ETF_DATA.iterrows():
        # get the name and weight of the constituent
        name = row['name']
        weight = row['weight']

        # get price from the constituents
        if name not in last_prices:
            raise ValueError(f"Price for {name} not found")
        
        price = last_prices[name]

        constituents.append({
            "name": name,
            "weight": weight,
            "price": round(price, 2)
        })
    
    return constituents
            
def get_etf_prices() -> list:
    """
    Get the ETF prices for the time series plot

    Calculates the etf price for each data by combining the weight and price of each constituent.
    
    Returns:
        list: A list of ETF prices for each date
    
    Raises:
        ValueError: If the ETF data is not found
    """
    
    if ETF_DATA is None:
        raise ValueError("ETF data not found")

    etf_time_series = []

    # extracting the constituents and weights from the etf data first otherwise we have to iterate over in the loop as a pandas dataframe
    constituents = ETF_DATA['name'].tolist()
    weights = ETF_DATA['weight'].tolist()

    # this is a big(n x m), n = number of dates, m = number of constituents
    for i, row in PRICES_DATA.iterrows():
        # we know the row will contain data in this format:
        # row = {"DATE": "2017-01-01", "A": 2.32, "B": 3.707, "C": 30.970, ...}
        date = row['DATE']

        # getting the prices of the constituents from each row
        # since we have extracted the constituents we can get the price from the row
        prices = [row[name] for name in constituents]
        
        etf_price = 0.0

        #found a zip function that we can use to iterate over the weights and prices at the same time
        for weight, price in zip(weights, prices):
            etf_price += weight * price
        
        etf_time_series.append({
            "date": date,
            "price": round(etf_price, 2)
        })
    
    return etf_time_series


