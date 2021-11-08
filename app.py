from fastapi.applications import FastAPI
import uvicorn
from web.controller_put.auth_routeur import routerput
from web.controller.auth_router import router

app = FastAPI()
app.include_router(routerput)
app.include_router(router)

if __name__ == "__main__" : 
    uvicorn.run(app, host = "0.0.0.0", port = 5000)