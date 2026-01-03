from database.database import SessionLocal, Constituent, Price

def retrieve_constituents() -> list:
    """
    Get the constituents of the ETF with their weight and latest price

    Returns:
        list: A list of constituents with their weight and latest price

    Raises:
        ValueError: If the ETF data is not found
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
        price_dict = {p.constituent: p.price for p in prices}

        result = []
        for c in constituents:
            result.append({
                "name": c.name,
                "weight": c.weight,
                "price": price_dict[c.name]
            })
        
        return result
    except Exception as e:
        raise e
    finally:
        db.close()
        



