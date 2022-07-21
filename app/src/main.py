import os
import json
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests

from settings import load_config

load_config()

CITY_API_HOST = os.environ.get("BACKEND_CITY_API_HOST")
CITY_API_URL = os.environ.get("BACKEND_CITY_API_URL")
CITY_API_KEY = os.environ.get("BACKEND_CITY_API_KEY")

app = FastAPI()


@app.middleware("http")
def save_request_information(request: Request, call_next):

  request_time = datetime.datetime.now().isoformat()
  request_browser = request.headers["user-agent"]
  request_endpoint = request.url.path

  mongo_db_input = {
    "time": request_time,
    "browser": request_browser,
    "endpoint": request_endpoint
  }

  response = call_next(request)

  return response


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


@app.get("/nearbyCities")
def get_nearby_cities(city: int):

  query_parameters = {"radius": "100"}  # radius wasn't specified in assignment brief, so just keeping it the default 100

  headers = {
    "X-RapidAPI-Key": CITY_API_KEY,
    "X-RapidAPI-Host": CITY_API_HOST
  }

  response = requests.request(
    "GET",
    f"{CITY_API_URL}/{city}/nearbyCities", 
    headers=headers,
    params=query_parameters
  )
  
  nearby_cities = json.loads(response.text)["data"]

  return JSONResponse(content=nearby_cities)
