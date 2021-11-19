import uvicorn
from fastapi.applications import FastAPI

from web.controller.administrateur_router import routera
#from web.controller.campagne_routeur import routerc
from web.controller.authentification_router import router
from web.controller.feed_back_router import routerf
from web.controller.joueur_router import routerj
from web.controller.monstre_router import routerm
from web.web_config import WebConfig

app = FastAPI()
#app.include_router(routerc)
app.include_router(router)
app.include_router(routerm)
app.include_router(routerf)
app.include_router(routera)
app.include_router(routerj)

if __name__ == "__main__" :
    port = WebConfig().getApiPort()
    uvicorn.run(app, host="localhost", port = "5000", log_level="info")
