from app.tr369.usp_header import USPHeader
from app.tr369.usp_body import USPBody


class USPRecord:

    def __init__(self, message_type, data):

        self.header = USPHeader(message_type)

        self.body = USPBody(data)

    def to_dict(self):

        return {

            "Header": self.header.to_dict(),

            "Body": self.body.to_dict()

        }