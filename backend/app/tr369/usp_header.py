import uuid


class USPHeader:

    def __init__(
        self,
        message_type,
        agent_id="usp-agent",
        controller_id="usp-controller"
    ):

        self.message_id = str(uuid.uuid4())
        self.message_type = message_type
        self.agent_id = agent_id
        self.controller_id = controller_id

    def to_dict(self):

        return {

            "MessageId": self.message_id,

            "MessageType": self.message_type,

            "AgentId": self.agent_id,

            "ControllerId": self.controller_id

        }