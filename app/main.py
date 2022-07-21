import os
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

from settings import load_config

load_config()

CITY_API_HOST = os.environ.get("BACKEND_CITY_API_HOST")
CITY_API_URL = os.environ.get("BACKEND_CITY_API_URL")
CITY_API_KEY = os.environ.get("BACKEND_CITY_API_KEY")


app = FastAPI()

@app.get("/availableCities")
def get_cities():

  query_parameters = {"minPopulation": "1000000"}

  headers = {
    "X-RapidAPI-Key": CITY_API_KEY,
    "X-RapidAPI-Host": CITY_API_HOST
  }

  response = requests.request(
    "GET",
    CITY_API_URL,
    headers=headers,
    params=query_parameters
  )
  
  cities = json.loads(response.text)["data"]

  return JSONResponse(content=cities)