from datetime import datetime

from fastapi import FastAPI, Request 

from server.routes.requests import router as RequestRouter
from server.routes.cities import router as CityRouter

app = FastAPI()

app.include_router(RequestRouter, tags=["Request"], prefix="/requests")
app.include_router(CityRouter, tags=["City"], prefix="/cities")

@app.middleware("http")
def save_request_information(request: Request, call_next):

  request_time = datetime.now().isoformat()
  request_browser = request.headers["user-agent"]
  request_endpoint = request.url.path

  mongo_db_input = {
    "time": request_time,
    "browser": request_browser,
    "endpoint": request_endpoint
  }

  response = call_next(request)

  return response
