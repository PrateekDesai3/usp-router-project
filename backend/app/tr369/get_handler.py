from app.tr181.mapper import TR181Mapper


class GetHandler:

    def __init__(self):
        self.mapper = TR181Mapper()

    def get_parameter(self, path):

        data = self.mapper.get()

        parts = path.split(".")

        value = data

        try:
            for part in parts:
                value = value[part]

            return {
                "Path": path,
                "Value": value
            }

        except Exception:

            return {
                "Path": path,
                "Error": "Parameter Not Found"
            }