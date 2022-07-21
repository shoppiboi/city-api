from pydantic import BaseModel
from datetime import datetime 


class RequestSchema(BaseModel):
    time: datetime = None
    browser: str = None
    endpoint: str = None


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }