from app.router.router_service import RouterService


class OperateHandler:

    def __init__(self):

        self.router = RouterService()

    def operate(self, command, arguments=None):

        if arguments is None:

            arguments = {}

        if command == "Reboot":

            return self.router.reboot()

        elif command == "Ping":

            return self.router.ping(

                arguments.get("Host")

            )

        elif command == "Traceroute":

            return self.router.traceroute(

                arguments.get("Host")

            )

        elif command == "Uptime":

            return self.router.uptime()

        elif command == "Hostname":

            return self.router.hostname()

        return {

            "Status": "Unsupported Operation",

            "Operation": command

        }