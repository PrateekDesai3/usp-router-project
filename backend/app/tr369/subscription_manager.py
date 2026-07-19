class SubscriptionManager:

    def __init__(self):

        self.subscriptions = []

    def subscribe(self, event):

        if event not in self.subscriptions:

            self.subscriptions.append(event)

        return {

            "Event": event,

            "Status": "Subscribed"

        }

    def unsubscribe(self, event):

        if event in self.subscriptions:

            self.subscriptions.remove(event)

            return {

                "Event": event,

                "Status": "Unsubscribed"

            }

        return {

            "Event": event,

            "Status": "Subscription Not Found"

        }

    def is_subscribed(self, event):

        return event in self.subscriptions

    def get_subscriptions(self):

        return self.subscriptions