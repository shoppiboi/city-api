import os
from datetime import datetime

from settings import load_config

from fastapi import FastAPI, Request
from server.database import add_request

from server.routes.requests import router as RequestRouter
from server.routes.cities import router as CityRouter

if int(os.environ.get("DEBUG")) == 1:
  load_config()

BACKEND_HOST = os.environ.get("BACKEND_HOST") 
BACKEND_PORT = os.environ.get("BACKEND_PORT")

app = FastAPI()

app.include_router(RequestRouter, tags=["Request"], prefix="/requests")
app.include_router(CityRouter, tags=["City"], prefix="/cities")

@app.get("/")
def root():
    return {"message": "alive"}

@app.middleware("http")
async def save_request_information(request: Request, call_next):

  payload = {
    "time": datetime.now().isoformat(),
    "browser": request.headers["user-agent"],
    "endpoint": request.url.path,
  }

  # doesn't really make sense to add an entry for when accessing listRequests
  if request.url.path != "/requests/listRequests":
    await add_request(payload)

  response = await call_next(request)

  return response
