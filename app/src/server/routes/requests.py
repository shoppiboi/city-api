from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from server.database import list_requests
from server.models import ResponseModel, RequestSchema

router = APIRouter()

@router.get("/listRequests")
async def get_requests():
    requests = await list_requests()
    if requests:
        return JSONResponse(requests)
    return ResponseModel(requests)