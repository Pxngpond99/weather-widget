import paho.mqtt.client as mqtt
from datetime import datetime
import time
import random
import json

# broker = "test.mosquitto.org"
broker = "localhost"
port = 1883
topic = "mymqtt/sensors"
client_id = "itscoe-mqtt-011"
data = dict()


def on_publish(client, userdata, mid):
    print("[" + str(datetime.now()) + "]", "sent a message => Data:", data)


mqttClient = mqtt.Client(client_id)
mqttClient.on_publish = on_publish
mqttClient.connect(broker, port)
# start a new thread
mqttClient.loop_start()

# Why use msg.encode('utf-8') here
# MQTT is a binary based protocol where the control elements are binary bytes and not text strings.
# Topic names, Client ID, Usernames and Passwords are encoded as stream of bytes using UTF-8.
while True:
    msg = "hello"
    temperature = round(random.uniform(25.0, 29.0), 2)
    humidity = round(random.uniform(58.0, 70.0), 2)
    light = round(random.uniform(0.0, 100.0), 2)
    raindrop = round(random.uniform(0.0, 100.0), 2)
    # data = {"temperature": temperature, "humidity": humidity, "light": light, "raindrop": raindrop}
    data["temperature"] = temperature
    data["humidity"] = humidity
    data["light"] = light
    data["raindrop"] = raindrop
    data_json = json.dumps(data)
    #print("[" + str(datetime.now()) + "]", "Data:", data_json)
    info = mqttClient.publish(
        topic=topic,
        payload=data_json.encode(),
        qos=0,
    )
    # Because published() is not synchronous,
    # it returns false while he is not aware of delivery that's why calling wait_for_publish() is mandatory.
    info.wait_for_publish()
    print("Sent:", info.is_published())
    time.sleep(1)
