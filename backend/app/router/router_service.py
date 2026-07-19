from app.ssh.ssh_client import SSHClient


class RouterService:

    def __init__(self):

        self.ssh = SSHClient()

    def run(self, command):

        self.ssh.connect()

        result = self.ssh.execute(command)

        self.ssh.disconnect()

        return result

    # -------------------------
    # Existing Methods
    # -------------------------

    def hostname(self):

        return self.run("hostname")

    def uptime(self):

        return self.run("cat /proc/uptime")

    def interfaces(self):

        return self.run("ip addr")

    def routes(self):

        return self.run("ip route")

    def cpu(self):

        return self.run("cat /proc/cpuinfo")

    def memory(self):

        return self.run("cat /proc/meminfo")

    def network(self):

        return self.run("cat /proc/net/dev")

    # -------------------------
    # USP Operate Methods
    # -------------------------

    def reboot(self):

        output = self.run("sudo reboot")

        return {

            "Operation": "Reboot",

            "Output": output,

            "Status": "Success"

        }

    def ping(self, host):

        output = self.run(f"ping -c 4 {host}")

        return {

            "Operation": "Ping",

            "Host": host,

            "Output": output,

            "Status": "Success"

        }

    def traceroute(self, host):

        output = self.run(f"traceroute {host}")

        return {

            "Operation": "Traceroute",

            "Host": host,

            "Output": output,

            "Status": "Success"

        }

    def hostname_operation(self):

        output = self.hostname()

        return {

            "Operation": "Hostname",

            "Output": output,

            "Status": "Success"

        }

    def uptime_operation(self):

        output = self.uptime()

        return {

            "Operation": "Uptime",

            "Output": output,

            "Status": "Success"

        }
