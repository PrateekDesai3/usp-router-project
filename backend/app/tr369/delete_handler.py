class DeleteHandler:

    def delete_object(self, object_path):

        return {

            "Object": object_path,

            "Status": "Deleted"

        }