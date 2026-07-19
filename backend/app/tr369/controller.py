from app.tr369.agent import USPAgent


class USPController:

    def __init__(self):

        self.agent = USPAgent()

    def get_device(self):

        return self.agent.get_device()

    def get_supported_dm(self):

        return self.agent.get_supported_dm()

    def get_parameter(self, path):

        return self.agent.get_parameter(path)

    def set_parameter(self, path, value):

        return self.agent.set_parameter(path, value)

    def get_instances(self, object_path):

        return self.agent.get_instances(object_path)

    def add_object(self, object_path):

        return self.agent.add_object(object_path)

    def delete_object(self, object_path):

        return self.agent.delete_object(object_path)

    def operate(self, command, arguments=None):

        return self.agent.operate(command, arguments)

    def subscribe(self, event):

        return self.agent.subscribe(event)

    def unsubscribe(self, event):

        return self.agent.unsubscribe(event)

    def get_subscriptions(self):

        return self.agent.get_subscriptions()

    def notify(self, event, data):

        return self.agent.notify(event, data)
    def session_info(self):

      return self.agent.session_info()


    def heartbeat(self):

      return self.agent.heartbeat()


    def disconnect(self):

      return self.agent.disconnect()