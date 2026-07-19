from app.tr181.cpu import CPU
from app.tr181.memory import Memory
from app.tr181.uptime import Uptime


class DeviceInfo:

    def __init__(self, router):
        self.router = router

    def get(self):

        hostname = self.router.hostname().strip()

        return {

            "Manufacturer": "OpenAI Demo",

            "ManufacturerOUI": "08:00:27",

            "ModelName": "Ubuntu Virtual Router",

            "Description": "Ubuntu VM acting as USP Agent",

            "SoftwareVersion": self.router.run(
                "uname -r"
            ).strip(),

            "HardwareVersion": self.router.run(
                "uname -m"
            ).strip(),

            "SerialNumber": self.router.run(
                "cat /etc/machine-id"
            ).strip(),

            "HostName": hostname,

            "UpTime": Uptime(self.router).get(),

            "Processor": CPU(self.router).get(),

            "MemoryStatus": Memory(self.router).get()

        }