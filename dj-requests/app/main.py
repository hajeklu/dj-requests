from fastapi import FastAPI
from app.routers import requests

app = FastAPI(title="DJ Requests API")

# Include the requests router
app.include_router(requests.router) 