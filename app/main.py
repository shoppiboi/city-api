from fastapi import FastAPI

import os
from settings import load_config

load_config()

CITY_API_HOST = os.environ.get("BACKEND_CITY_API_HOST")
CITY_API_URL = os.environ.get("BACKEND_CITY_API_URL")
CITY_API_KEY = os.environ.get("BACKEND_CITY_API_KEY")


app = FastAPI()

@app.get("/availableCities")
def get_cities():

  query_parameters = {"minPopulation": "1000000"}

  return {"Hello": "World!"}