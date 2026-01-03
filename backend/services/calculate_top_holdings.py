from database.database import SessionLocal, Constituent, Price

def calculate_top_holdings() -> list:
    """
    Get top 5 biggest holdings of the ETF
    
    Returns:
        list: A list of top 5 biggest holdings of the ETF

    Sources used:
        https://www.geeksforgeeks.org/python/sorting-list-of-dictionaries-in-descending-order-in-python/
    """
    db = SessionLocal()

    try:
        constituents = db.query(Constituent).all()
        if not constituents:
            raise ValueError("ETF data not found")
        
        # this query should be fast since we are using an index for the date column so just needs the max date
        latest_date = db.query(Price.date).order_by(Price.date.desc()).first()
        if not latest_date:
            raise ValueError("Prices data not found")
        
        # since the above query is returinig a tuble of the date, somthing like this: ('2017-04-28',)
        # we will need to extract the date
        latest_date = latest_date[0]

        # from the etf data we will need the names of the constituents
        constituent_names = [c.name for c in constituents]

        prices = db.query(Price).filter(
            Price.date == latest_date, # get only from the latest date
            Price.constituent.in_(constituent_names) # get only the constituents that are in the etf
        ).all()
        # we will need to create a dictionary to store the prices
        # since the above query will return a list of Price objects example: [Price(date='2017-04-28', constituent='A', price=2.32), ...]
        # create a smaller key value pair of constituent and price for eaiser lookup
        price_dict = {p.constituent: p.price for p in prices}
        
        top_holdings = []
        for c in constituents:

            value = c.weight * price_dict[c.name] 
            top_holdings.append({
                "name": c.name,
                "value": round(value, 2)
            })

        # return a sorted list from high to low so easier to pass in the chart
        top_holdings.sort(key=lambda x: x['value'], reverse=True)
        return top_holdings[:5]
    except Exception as e:
        raise e
    finally:
        db.close()

        


        
        

    