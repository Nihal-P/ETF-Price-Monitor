"""
The purpose of this init file is to package all the routers and export them to be used in main.py
"""

from fastapi import APIRouter
from .upload_etf import router as upload_etf_router
from .get_constituents import router as get_constituents_router
from .get_etf_prices import router as get_etf_prices_router

api_router = APIRouter()
api_router.include_router(upload_etf_router)
api_router.include_router(get_constituents_router)
api_router.include_router(get_etf_prices_router)