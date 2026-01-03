"""
ASSUMPTION: 
the prices csv file will be the only one that will be used and assume will be compatible with the ETF file provided by a user.
"""

import pandas as pd
from database import SessionLocal, Price
def load_prices():
    db = SessionLocal()
    
    # Clear existing price data to reset
    db.query(Price).delete()
    
    # read our prices csv file
    df = pd.read_csv('data/bankofmontreal-e134q-1arsjzss-prices.csv')
    
    # Insert each price record into our db
    # Debugging to check if it parsed the data correctly
    print(f"Loading {len(df)} dates with {len(df.columns)-1} constituents...")
    count = 0
    for _, row in df.iterrows():
        date = row['DATE']
        for col in df.columns[1:]:  # Skip DATE column since its not a constituent
            price_record = Price(
                date=date,
                constituent=col,
                price=float(row[col])
            )
            db.add(price_record)
            count += 1
    
    db.commit()
    print(f"Loaded {count} price records into databas")
    db.close()
if __name__ == "__main__":
    load_prices()