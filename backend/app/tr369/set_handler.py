from app.router.router_service import RouterService


class SetHandler:

    def __init__(self):
        self.router = RouterService()

    def set_parameter(self, path, value):

        if path == "Device.DeviceInfo.HostName":

            command = f"sudo hostnamectl set-hostname {value}"

            self.router.run(command)

            return {
                "Path": path,
                "Value": value,
                "Status": "Success"
            }

        return {
            "Path": path,
            "Status": "Parameter Not Writable"
        }