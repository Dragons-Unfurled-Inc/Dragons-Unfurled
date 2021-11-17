from fastapi.applications import FastAPI
import uvicorn
#from web.controller_put.auth_routeur import routerput
#from web.controller.auth_router import router
from web.controller.monstre_router import routerm
from web.web_config import WebConfig

app = FastAPI()
#app.include_router(routerput)
#app.include_router(router)
app.include_router(routerm)

if __name__ == "__main__" :
    port = WebConfig().getApiPort()
    uvicorn.run("webservice:app", host="localhost", port=port, log_level="info")