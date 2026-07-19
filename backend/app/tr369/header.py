import uuid


class USPHeader:

    def __init__(self, message_type):

        self.message_id = str(uuid.uuid4())
        self.message_type = message_type
        self.protocol = "TR-369 USP"
        self.version = "1.0"

    def to_dict(self):

        return {
            "MessageId": self.message_id,
            "MessageType": self.message_type,
            "Protocol": self.protocol,
            "Version": self.version
        }