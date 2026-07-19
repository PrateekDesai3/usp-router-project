import uuid
from datetime import datetime


class SessionManager:

    def __init__(self):

        self.session_id = str(uuid.uuid4())

        self.agent_id = "USP-Agent"

        self.controller_id = "USP-Controller"

        self.connected = True

        self.created = datetime.now().isoformat()

    def get_session(self):

        return {

            "SessionId": self.session_id,

            "AgentId": self.agent_id,

            "ControllerId": self.controller_id,

            "Connected": self.connected,

            "Created": self.created

        }

    def heartbeat(self):

        return {

            "SessionId": self.session_id,

            "Status": "Alive"

        }

    def disconnect(self):

        self.connected = False

        return {

            "Status": "Disconnected"

        }