from fastapi import APIRouter, HTTPException
from services import etf_service

router = APIRouter()

@router.get("/etf-prices")
def get_etf_prices():
    """
    Get the ETF prices for the time series plot

    Calculates the etf price for each data by combining the weight and price of each constituent.
    
    Returns:
        List[Dict]: A list of dicts containing the date and price of the ETF
    """
    try:
        result = etf_service.get_etf_prices()
        return result
    
    # error if etf data is not found or so other invalid input
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        
    # error if the error is on the server side
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))