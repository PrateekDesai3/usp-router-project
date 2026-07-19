from app.router.router_service import RouterService

from app.tr181.device_info import DeviceInfo
from app.tr181.ip import IP
from app.tr181.routing import Routing


class TR181Mapper:

    def __init__(self):

        self.router = RouterService()

        self.device = DeviceInfo(self.router)
        self.ip = IP(self.router)
        self.routing = Routing(self.router)

    def get(self):

        return {

            "Device": {

                "DeviceInfo": self.device.get(),

                "IP": self.ip.get(),

                "Routing": self.routing.get()

            }

        }