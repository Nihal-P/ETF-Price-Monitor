from database.database import SessionLocal, Constituent, Price

def calculate_etf_price() -> list:
    """
    Get the ETF prices for the time series plot

    Calculates the etf price for each data by combining the weight and price of each constituent.
    
    Returns:
        list: A list of ETF prices for each date
    
    Raises:
        ValueError: If the ETF data is not found
    """

    db = SessionLocal()
    try:
        constituents = db.query(Constituent).all()
        if not constituents:
            raise ValueError("ETF data not found")

        # need to get the weight and name of the constituents
        weights = {c.name: c.weight for c in constituents}
        constituent_names = [c.name for c in constituents]

        # get the prices of the constituents that are in the etf
        # prices will return be a list of Price objects example: [Price(date='2017-04-28', constituent='A', price=2.32), ...]
        # need to use order_by so we get the prices in order
        prices = db.query(Price).filter(Price.constituent.in_(constituent_names)).order_by(Price.date).all()
        
        # need to group the prices by date
        date_prices = {}
        for i in prices:
            # create a entry for the date if it doesn't exist
            if i.date not in date_prices:
                date_prices[i.date] = {}
            # by this point we have the date and so just need to add the constituents and prices to the date entry
            date_prices[i.date][i.constituent] = i.price
        
        result = []
        # this way date will be the first key and prices will be a dictionary of constituent and price
        # main job is now to calculate the etf price for each date by combining the weight and price of each constituent
        for date, prices in date_prices.items():
            etf_price = 0.0

            # now that prices can be split to iterate over the inner dictionary
            for constituent, price in prices.items():
                etf_price += weights[constituent] * price
            result.append({
                "date": date,
                "price": round(etf_price, 2)
            })
        return result
    except Exception as e:
        raise e
    finally:
        db.close()