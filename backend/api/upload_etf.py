from fastapi import UploadFile, HTTPException, APIRouter
from services import etf_service

router = APIRouter()

@router.post("/upload-etf")
def upload_etf(file: UploadFile):
    """
    Upload an ETF CSV file

    Args:
        file (UploadFile): The ETF CSV file to upload

    Returns:
        Dict: A dictionary containing the result of the upload operation
    """

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    
    try:
        result = etf_service.upload_etf(file.file)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
I am also calling my upload_etf service inside this endpoint which does the parsing of the 
csv so in case if there are any errors we could send the error response back right away.

Source:
Used this doc to creat the endpoint: https://fastapi.tiangolo.com/reference/uploadfile/#fastapi.UploadFile
"""