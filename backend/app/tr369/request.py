class USPRequest:

    def __init__(
        self,
        operation=None,
        paths=None,
        object_path=None,
        value=None,
        command=None,
        arguments=None,
        event=None,
        data=None,
        subscription=None
    ):

        self.operation = operation
        self.paths = paths or []
        self.object_path = object_path
        self.value = value
        self.command = command
        self.arguments = arguments or {}
        self.event = event
        self.data = data or {}
        self.subscription = subscription

    @staticmethod
    def from_dict(data):

        if not isinstance(data, dict):

            raise ValueError("Invalid USP Request")

        return USPRequest(

            operation=data.get("Operation"),

            paths=data.get("Paths", []),

            object_path=data.get("Object"),

            value=data.get("Value"),

            command=data.get("Command"),

            arguments=data.get("Arguments", {}),

            event=data.get("Event"),

            data=data.get("Data", {}),

            subscription=data.get("Subscription")
        )