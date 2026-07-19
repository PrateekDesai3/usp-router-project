from app.tr181.mapper import TR181Mapper


class GetInstancesHandler:

    def __init__(self):

        self.mapper = TR181Mapper()

    def get_instances(self, object_path):

        data = self.mapper.get()

        if object_path == "Device.IP.Interface":

            interfaces = data["Device"]["IP"]["Interface"]

            instances = []

            for i in range(len(interfaces)):

                instances.append(
                    f"Device.IP.Interface.{i+1}"
                )

            return {

                "Object": object_path,

                "Instances": instances

            }

        return {

            "Object": object_path,

            "Error": "Object Not Found"

        }