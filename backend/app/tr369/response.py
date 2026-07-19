class USPResponse:

    def __init__(self, success=True, data=None, error=None):

        self.success = success
        self.data = data
        self.error = error

    def to_dict(self):

        return {

            "Success": self.success,

            "Data": self.data,

            "Error": self.error

        }