#!/usr/bin/env python3
# Imports
from time import sleep
import paho.mqtt.client as mqtt             # MQTT
from datetime import datetime               # Uhrzeit
from influxdb_client import InfluxDBClient, Point, WritePrecision   # InfluxDB
from influxdb_client.client.write_api import SYNCHRONOUS            # InfluxDB API

import json                                 # JSON Parser


###############################################################################
# MQTT - Funktionen 

def on_connect(client, userdata, flags, rc):
    # This will be called once the client connects
    print(f"Connected with result code {rc}")
    # Subscribe here!
    client.subscribe("Z903a/Temp")

def on_message(client, userdata, msg):
    topic = msg.topic
    msgJson = msg.payload
    print(f"Message received [{topic}]: {msgJson}")
    if topic == "Z903a/Temp":
        # Diesen Raum wollen wir überwachen und auzeichnen -> 
        push2Influx(msgJson)

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

###############################################################################
# InfluxDB - Funktionen 
def push2Influx(jsonStr):

    # Influx-Config
    token = "3QvFY24dcHwU59VoE6ku7iiztRgAU2c3xTTtI8lgDuw9wOxyrE5Wz5SG9gqHAyIeD2rjK0gDstmuc4RhdFFSTg=="
    org = "Workshop22"
    bucket = "Workshop22"

    myDict = json.loads(jsonStr)    # Eingabe ist ein String im Json-Format -> dieses schicken wir jetzt in den Parser
                                    # der uns den String in ein Dict wandelt, auf dass wir nun einfach zugreifen können

    t = myDict["t"]     # Timestamp
    n = myDict["n"]     # Name (Sensorbezeichnung)                
    v = myDict["v"]     # Value (Messwert)
    u = myDict["u"]     # Unit (Messeinheit)     

    t = int(t)

    print("push2Influx" , "t=" , t)

    with InfluxDBClient(url="http://192.168.187.24:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point("mem2") \
            .tag("host", "rpi-4") \
            .tag("sensorname", n) \
            .tag("unit", u) \
            .field("v", v) \
            .time(t, WritePrecision.NS)
        write_api.write(bucket, org, point)

###############################################################################
client = mqtt.Client("Laptop-test") # client ID "mqtt-test"
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect('192.168.187.24', 1883)

#sleep(5)
#client.subscribe("Z903a/Temp")

client.loop_forever()  # Start networking daemon