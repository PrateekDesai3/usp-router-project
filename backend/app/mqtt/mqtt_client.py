import json
import paho.mqtt.client as mqtt


class MQTTClient:

    def __init__(self):

        self.client = mqtt.Client()

        # Ubuntu VM MQTT Broker
        self.client.connect("192.168.0.14", 1883, 60)

        self.client.loop_start()

    def publish(self, topic, message):

        if isinstance(message, dict):

            message = json.dumps(message)

        self.client.publish(topic, message)

    def disconnect(self):

        self.client.loop_stop()

        self.client.disconnect()