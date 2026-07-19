import json

import paho.mqtt.client as mqtt

from app.tr369.message_processor import USPMessageProcessor


processor = USPMessageProcessor()


def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("MQTT Connected Successfully")

        client.subscribe("usp/request")

    else:

        print(f"MQTT Connection Failed : {rc}")


def on_message(client, userdata, msg):

    try:

        request = json.loads(msg.payload.decode())

        print("MQTT Request Received")

        print(request)

        response = processor.process(request)

        client.publish(

            "usp/response",

            json.dumps(response)

        )

        print("MQTT Response Published")

    except Exception as e:

        client.publish(

            "usp/response",

            json.dumps(

                {

                    "Error": str(e)

                }

            )

        )


def start():

    client = mqtt.Client()

    client.on_connect = on_connect

    client.on_message = on_message

    # Ubuntu VM MQTT Broker
    client.connect("192.168.0.14", 1883, 60)

    client.loop_forever() 