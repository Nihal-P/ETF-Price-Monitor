from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_router
from database.database import SessionLocal, Price
from database.load_prices import load_prices

# from my understanding this is a similar thing as how we setup in express.js for the entrypoing of the app
app = FastAPI(
    title="ETF Price Monitor API",
    description="API for ETF Price Monitor",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # will be using port 3000 for frontend
    allow_credentials=True, # technically not required since we have no auth, tokens or cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

# created this logic so the user does not have to manually run "python database/load_prices.py" 
# now basically creates a startup event that will run when the server starts.
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        price_count = db.query(Price).count()
        if price_count == 0:
            load_prices()
    finally:
        db.close()

# just to add a prefix to the routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}
