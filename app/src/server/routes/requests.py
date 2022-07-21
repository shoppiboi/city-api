from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.database import add_request, list_requests
from server.models import ResponseModel, RequestSchema

router = APIRouter()


@router.post("/", response_description="Request instance added into the database")
async def add_request_data(request: RequestSchema = Body(...)):
    request = jsonable_encoder(request)
    new_request = await add_request(request)
    return ResponseModel(new_request)


@router.get("/listRequests")
async def get_requests():
    requests = await list_requests()
    if requests:
        return JSONResponse(requests)
    return ResponseModel(requests)