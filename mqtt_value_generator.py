from time import sleep
from datetime import datetime
import paho.mqtt.client as mqtt
from random import seed
from random import random
from random import randint
import json

seed(1)

BASE_TOPIC = "HTW/Z/9/%s/%s"
DATA = [
    {
        "type": "Temp",
        "unit": "°C",
        "var": "float",
        "range": {
            "min": 18,
            "max": 28
        },
        "sensors": ["0001bab111fx", "200aaa2111fx", "773aa2111fx"]
    },
    {
        "type": "Light",
        "unit": "lx",
        "var": "int",
        "range": {
            "min": 500,
            "max": 1000
        },
        "sensors": ["0001bab111fx", "200aaa2111fx", "773aa2111fx"]
    },
    {
        "type": "Pressure",
        "unit": "hPa",
        "var": "float",
        "range": {
            "min": 900,
            "max": 1100
        },
        "sensors": ["0001bab111fx", "200aaa2111fx", "773aa2111fx"]
    },
    {
        "type": "Humidity",
        "unit": "%",
        "var": "int",
        "range": {
            "min": 30,
            "max": 70
        },
        "sensors": ["0001bab111fx", "200aaa2111fx", "773aa2111fx"]
    }
]

mqtt_con = mqtt.Client("Tetspublisher")
mqtt_con.connect("127.0.0.1", 1883)


def generate_val(t, min, max):
    if t == "int":
        return randint(min, max)
    elif t == "float":
        return min + (random() * (max - min))


while True:
    room = randint(901, 912)
    room_sensors = randint(1, 4)

    for i in range(room_sensors):
        sensor_type = randint(0, 3)
        sensor = DATA[sensor_type]["sensors"][randint(0, 2)]
        value = generate_val(DATA[sensor_type]["var"], DATA[sensor_type]["range"]["min"], DATA[sensor_type]["range"]["max"])

        mqtt_con.publish(BASE_TOPIC % (str(room) + "_TEST", DATA[sensor_type]["type"]), json.dumps({
            "n": str(sensor),
            "u": str(DATA[sensor_type]["unit"]),
            "v": float(value),
            "t": int(datetime.timestamp(datetime.now()))
        }))

    sleep(1)