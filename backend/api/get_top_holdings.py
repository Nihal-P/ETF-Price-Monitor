from fastapi import HTTPException, APIRouter
from services.calculate_top_holdings import calculate_top_holdings

router = APIRouter()

@router.get("/top-holdings")
def get_top_holdings():
    """
    Get top 5 biggest holdings in the ETF by value
    
    Holding value = weight x latest price
    
    Returns:
        List[Dict]: Top 5 holdings with name and value
    """
    try:
        result =  calculate_top_holdings()
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
