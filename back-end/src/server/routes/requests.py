from fastapi import APIRouter
from fastapi.responses import JSONResponse

from server.database import list_requests

router = APIRouter()

@router.get("/listRequests")
async def get_requests():
    requests = await list_requests()
    if requests:
        return JSONResponse(requests)
    
    return JSONResponse(content="No requests found")