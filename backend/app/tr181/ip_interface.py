import re

from app.router.router_service import RouterService


class IPInterface:

    def __init__(self):

        self.router = RouterService()

    def get(self):

        data = self.router.interfaces()

        interfaces = []

        current = None

        for line in data.splitlines():

            if re.match(r'^\d+:', line):

                if current:

                    interfaces.append(current)

                name = line.split(":")[1].strip()

                current = {

                    "Name": name,

                    "IPv4": "",

                    "MAC": "",

                    "Status": "Unknown"

                }

                if "UP" in line:

                    current["Status"] = "Up"

            elif "inet " in line:

                if current:

                    current["IPv4"] = line.strip().split()[1]

            elif "link/ether" in line:

                if current:

                    current["MAC"] = line.strip().split()[1]

        if current:

            interfaces.append(current)

        return {

            "IP": {

                "Interface": interfaces

            }

        }