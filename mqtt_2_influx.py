from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqttClient

# Funktion wird aufgerufen, sobald es eine Änderung auf dem abbonieretn Topic gab

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected MQTT disconnection. Will auto-reconnect")

def push2Influx():

    # Influx-Config
    token = "3QvFY24dcHwU59VoE6ku7iiztRgAU2c3xTTtI8lgDuw9wOxyrE5Wz5SG9gqHAyIeD2rjK0gDstmuc4RhdFFSTg=="
    org = "Workshop22"
    bucket = "Workshop22"

    with InfluxDBClient(url="http://192.168.187.24:8086", token=token, org=org) as client:
        point = Point("mem") \
            .tag("host", "rpi-4") \
            .field("used_percent", 23.43234543) \
            .time(datetime.utcnow(), WritePrecision.NS)
        write_api.write(bucket, org, point)





#MQTT-Config
broker_address= "192.168.187.232"     #Broker address
port = 1883                          #Broker port

client = mqttClient.Client("rpi-4")         


client.on_message= on_message 
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(broker_address, port=port)   

#client.loop_start()                        #start the loop
client.subscribe("Z903a/#", 1)
#client.subscribe("HTW/Z/9/906_TEST/Temp",1)


client.loop_forever()