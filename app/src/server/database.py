import os
import motor.motor_asyncio

MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_HOST = os.environ.get("MONGODB_HOST")

MONGO_DETAILS = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.requests
request_collection = database.get_collection("requests_collection")


def request_helper(request) -> dict:
    return {
        "id": str(request["_id"]),
        "time": str(request["time"]),
        "browser": str(request["browser"]),
        "endpoint": str(request["endpoint"]),
    }


async def list_requests():
    requests = []
    async for request in request_collection.find():
        requests.append(request_helper(request))
    return requests


async def add_request(request_data: dict) -> dict:
    request = await request_collection.insert_one(request_data)
    new_request = await request_collection.find_one({"_id": request.inserted_id})
    return request_helper(new_request)
