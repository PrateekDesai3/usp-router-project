from app.tr181.mapper import TR181Mapper

from app.tr369.supported_dm import SupportedDataModel
from app.tr369.get_handler import GetHandler
from app.tr369.set_handler import SetHandler
from app.tr369.get_instances_handler import GetInstancesHandler
from app.tr369.add_handler import AddHandler
from app.tr369.delete_handler import DeleteHandler
from app.tr369.operate_handler import OperateHandler
from app.tr369.notify_handler import NotifyHandler
from app.tr369.subscription_manager import SubscriptionManager
from app.tr369.session_manager import SessionManager
from app.tr369.logger import USPLogger


class USPAgent:

    def __init__(self):

        self.mapper = TR181Mapper()

        self.get_handler = GetHandler()

        self.set_handler = SetHandler()

        self.instances_handler = GetInstancesHandler()

        self.add_handler = AddHandler()

        self.delete_handler = DeleteHandler()

        self.operate_handler = OperateHandler()

        self.notify_handler = NotifyHandler()

        self.subscription_manager = SubscriptionManager()

        self.session = SessionManager()

        self.logger = USPLogger()

    # -------------------------
    # Device
    # -------------------------

    def get_device(self):

        self.logger.log("GetDevice")

        return self.mapper.get()

    def get_supported_dm(self):

        self.logger.log("GetSupportedDM")

        return SupportedDataModel.get()

    # -------------------------
    # Parameters
    # -------------------------

    def get_parameter(self, path):

        self.logger.log(f"Get {path}")

        return self.get_handler.get_parameter(path)

    def set_parameter(self, path, value):

        self.logger.log(f"Set {path}")

        return self.set_handler.set_parameter(path, value)

    def get_instances(self, object_path):

        self.logger.log(f"GetInstances {object_path}")

        return self.instances_handler.get_instances(object_path)

    # -------------------------
    # Objects
    # -------------------------

    def add_object(self, object_path):

        self.logger.log(f"Add {object_path}")

        return self.add_handler.add_object(object_path)

    def delete_object(self, object_path):

        self.logger.log(f"Delete {object_path}")

        return self.delete_handler.delete_object(object_path)

    # -------------------------
    # Operate
    # -------------------------

    def operate(self, command, arguments=None):

        self.logger.log(f"Operate {command}")

        return self.operate_handler.operate(command, arguments)

    # -------------------------
    # Subscription
    # -------------------------

    def subscribe(self, event):

        self.logger.log(f"Subscribe {event}")

        return self.subscription_manager.subscribe(event)

    def unsubscribe(self, event):

        self.logger.log(f"Unsubscribe {event}")

        return self.subscription_manager.unsubscribe(event)

    def get_subscriptions(self):

        self.logger.log("Subscriptions")

        return self.subscription_manager.get_subscriptions()

    def notify(self, event, data):

        self.logger.log(f"Notify {event}")

        if self.subscription_manager.is_subscribed(event):

            return self.notify_handler.notify(event, data)

        return {

            "Event": event,

            "Status": "No Subscribers"

        }

    # -------------------------
    # Session
    # -------------------------

    def session_info(self):

        self.logger.log("Session")

        return self.session.get_session()

    def heartbeat(self):

        self.logger.log("Heartbeat")

        return self.session.heartbeat()

    def disconnect(self):

        self.logger.log("Disconnect")

        return self.session.disconnect()