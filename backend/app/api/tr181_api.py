from fastapi import APIRouter

from app.router.router_service import RouterService

from app.tr181.device_info import DeviceInfo
from app.tr181.ip import IP
from app.tr181.routing import Routing

router = APIRouter()

service = RouterService()


@router.get("/tr181")
def tr181():

    return {
        "Device": {
            "DeviceInfo": DeviceInfo(service).get(),
            "IP": IP(service).get(),
            "Routing": Routing(service).get()
        }
    }