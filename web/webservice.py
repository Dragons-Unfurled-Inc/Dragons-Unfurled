import dotenv
from fastapi import FastAPI
import uvicorn

from app.web_service.controller import auth_router

dotenv.load_dotenv(override=True)


app = FastAPI()

app.include_router(auth_router.router)

if __name__ == "__main__":
    uvicorn.run("webservice:app", host="localhost", port="5000", log_level="info")