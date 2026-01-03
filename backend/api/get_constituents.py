from fastapi import UploadFile, HTTPException, APIRouter
from services import etf_service

router = APIRouter()

@router.get("/constituents")
def get_constituents():
    """
    Get the constituents of the ETF with their weight and latest price
    
    Requires an ETF to be uploaded first via /upload-etf

    Returns:
        List[Dict]: A list of dicts containing the name, weight and latest price of each constituent
    """
    try:
        result =  etf_service.get_constituents()
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
We will need to return a list of dicts with name, weight and last price because i have decided
to use AG grid community version for frontend table view. 

Source used:
https://www.ag-grid.com/react-data-grid/getting-started/#define-rows-and-columns
"""