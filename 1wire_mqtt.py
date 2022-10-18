
import time
from w1thermsensor import W1ThermSensor, Unit
import paho.mqtt.client as mqtt 

def getMyJson(v, u, n):
    unixts = time.time()
    returnString = '{ "t":' + str(unixts)+ ', "n":"' + str(n) + '",  "v":"' + str(v)+ '",   "u":"'  + str(u) + '"}'
    return returnString


# Init

mqttBroker ="192.168.187.24" 

client = mqtt.Client("rpi-4")
client.connect(mqttBroker) 


sensor = W1ThermSensor()                # Eine Instanz aus der Bibliothek erstellen

while True:
    temperature = sensor.get_temperature(Unit.DEGREES_C)  # Sensorwert abfragen -> liefert immer °C
    sensorID = sensor.id
    myJSON = getMyJson(temperature, "°C", sensorID)
    test = client.publish("Z903a/Temp", myJSON, 1)
    print("MQTT Publish result: " + str(test))
    print("The temperature is " + str(temperature) + " celsius")    # Sensowert anzeigen
    time.sleep(1)                                                        # Warten, da die Änderungen 