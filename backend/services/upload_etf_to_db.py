import pandas as pd
from typing import Dict
from fastapi import File

import pandas as pd
from database.database import SessionLocal, Constituent, Price # to create a session and access our models

# ETF_DATA = None
# # Assuming the prices data will be used for all etfs provided
# PRICES_DATA = pd.read_csv("data/bankofmontreal-e134q-1arsjzss-prices.csv")


def upload_etf_to_db(file: File) -> Dict:
    """
    Parse and store the uploaded ETF CSV file

    Args:
        file (File): The ETF CSV file to upload

    Returns:
        Dict: A dictionary containing the result of the upload operation

    Sources used:
        https://www.w3schools.com/python/pandas/pandas_csv.asp
    """

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

    db = SessionLocal()
    try:
        # delete any existing data in the constituents table to avoid any conflicts
        db.query(Constituent).delete()
        
        # basically iterrate over the rows of the ETF_DATA dataframe and push them in the db
        for i, row in ETF_DATA.iterrows():
            constituent = Constituent(
                name=row['name'],
                weight=row['weight']
            )
            db.add(constituent)
        db.commit()

        return {
            "message": "File uploaded successfully",
            "constituents": len(ETF_DATA),
            "total_weight": round(total_weight, 2)
        }
    except Exception as e:
        raise e
    finally:
        db.close()
