from app.tr369.header import USPHeader
from app.tr369.response import USPResponse


class USPMessage:

    @staticmethod
    def get_response(data):

        header = USPHeader("Response")

        body = USPResponse(

            success=True,

            data=data

        )

        return {

            "Header": header.to_dict(),

            "Body": body.to_dict()

        }

    @staticmethod
    def error(message):

        header = USPHeader("Error")

        body = USPResponse(

            success=False,

            error=message

        )

        return {

            "Header": header.to_dict(),

            "Body": body.to_dict()

        }