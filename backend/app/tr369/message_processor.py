from app.tr369.controller import USPController
from app.tr369.messages import USPMessage
from app.tr369.request import USPRequest


class USPMessageProcessor:

    def __init__(self):

        self.controller = USPController()

    def process(self, request):

        try:

            request = USPRequest.from_dict(request)

        except Exception as e:

            return USPMessage.error(str(e))

        operation = request.operation

        if operation is None:

            return USPMessage.error(
                "Operation Missing"
            )

        try:

            if operation == "Get":

                results = []

                for path in request.paths:

                    result = self.controller.get_parameter(path)

                    results.append(result)

                return USPMessage.get_response(results)

            elif operation == "Set":

                data = self.controller.set_parameter(

                    request.object_path,

                    request.value

                )

                return USPMessage.get_response(data)

            elif operation == "GetDevice":

                data = self.controller.get_device()

                return USPMessage.get_response(data)

            elif operation == "GetSupportedDM":

                data = self.controller.get_supported_dm()

                return USPMessage.get_response(data)

            elif operation == "GetInstances":

                data = self.controller.get_instances(

                    request.object_path

                )

                return USPMessage.get_response(data)

            elif operation == "Add":

                data = self.controller.add_object(

                    request.object_path

                )

                return USPMessage.get_response(data)

            elif operation == "Delete":

                data = self.controller.delete_object(

                    request.object_path

                )

                return USPMessage.get_response(data)

            elif operation == "Operate":

                data = self.controller.operate(

                    request.command,

                    request.arguments

                )

                return USPMessage.get_response(data)

            elif operation == "Subscribe":

                data = self.controller.subscribe(

                    request.subscription

                )

                return USPMessage.get_response(data)

            elif operation == "Unsubscribe":

                data = self.controller.unsubscribe(

                    request.subscription

                )

                return USPMessage.get_response(data)

            elif operation == "Subscriptions":

                data = self.controller.get_subscriptions()

                return USPMessage.get_response(data)

            elif operation == "Notify":

                data = self.controller.notify(

                    request.event,

                    request.data

                )

                return USPMessage.get_response(data)

            elif operation == "Session":

                data = self.controller.session_info()

                return USPMessage.get_response(data)

            elif operation == "Heartbeat":

                data = self.controller.heartbeat()

                return USPMessage.get_response(data)

            elif operation == "Disconnect":

                data = self.controller.disconnect()

                return USPMessage.get_response(data)

            else:

                return USPMessage.error(
                    "Unsupported USP Operation"
                )

        except Exception as e:

            return USPMessage.error(str(e))