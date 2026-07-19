import re


class IP:

    def __init__(self, router):
        self.router = router

    def get(self):

        data = self.router.interfaces()

        interfaces = []

        current = None

        for line in data.splitlines():

            line = line.strip()

            if re.match(r'^\d+:', line):

                if current:
                    interfaces.append(current)

                name = line.split(":")[1].strip()

                current = {
                    "Name": name,
                    "Enable": True,
                    "Status": "Down",
                    "Type": "Loopback" if name == "lo" else "Ethernet",
                    "MACAddress": "",
                    "IPv4Address": "",
                    "IPv6Address": ""
                }

                if "UP" in line:
                    current["Status"] = "Up"

            elif current is not None:

                if line.startswith("inet "):
                    current["IPv4Address"] = line.split()[1]

                elif line.startswith("inet6 "):
                    if current["IPv6Address"] == "":
                        current["IPv6Address"] = line.split()[1]

                elif line.startswith("link/ether"):
                    current["MACAddress"] = line.split()[1]

        if current:
            interfaces.append(current)

        return {
            "Interface": interfaces
        }