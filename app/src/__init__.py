import os
import uvicorn
from settings import load_config

load_config()

BACKEND_HOST = os.environ.get("BACKEND_HOST") 

if __name__ == "__main__":
    uvicorn.run("main:app", host=BACKEND_HOST, port=8000, reload=True)
