class USPBody:

    def __init__(self, data):

        self.data = data

    def to_dict(self):

        return {

            "Data": self.data

        }
        