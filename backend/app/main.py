import threading

from fastapi import FastAPI

from app.config import Config
from app.api.router_api import router as router_api
from app.api.tr181_api import router as tr181_api
from app.tr369.api import router as tr369_router
from app.mqtt.mqtt_listener import start as mqtt_start


threading.Thread(
    target=mqtt_start,
    daemon=True
).start()


app = FastAPI(
    title=Config.PROJECT_NAME,
    version=Config.VERSION
)


app.include_router(router_api)
app.include_router(tr181_api)
app.include_router(tr369_router)


@app.get("/")
def home():

    return {
        "status": "Running",
        "project": Config.PROJECT_NAME,
        "services": {
            "REST API": "Running",
            "TR-369 USP": "Running",
            "MQTT Listener": "Running"
        }
    }