import paramiko

from app.config import Config


class SSHClient:

    def __init__(self):

        self.client = None

    def connect(self):

        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        self.client.connect(

            hostname=Config.VM_HOST,

            port=Config.VM_PORT,

            username=Config.VM_USERNAME,

            password=Config.VM_PASSWORD

        )

    def execute(self, command):

        stdin, stdout, stderr = self.client.exec_command(command)

        return stdout.read().decode()

    def disconnect(self):

        if self.client:

            self.client.close()