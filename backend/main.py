from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_router

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

# just to add a prefix to the routes
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
