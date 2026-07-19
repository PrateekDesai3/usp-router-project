from fastapi import APIRouter

from app.router.router_service import RouterService

router = APIRouter()

service = RouterService()


@router.get("/hostname")
def hostname():
    return {
        "hostname": service.hostname().strip()
    }


@router.get("/interfaces")
def interfaces():
    return {
        "interfaces": service.interfaces()
    }


@router.get("/routes")
def routes():
    return {
        "routes": service.routes()
    }


@router.get("/cpu")
def cpu():
    return {
        "cpu": service.cpu()
    }


@router.get("/memory")
def memory():
    return {
        "memory": service.memory()
    }


@router.get("/uptime")
def uptime():
    return {
        "uptime": service.uptime()
    }