import time
from opcua import Client
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()                # Eine Instanz aus der Bibliothek erstellen

client = Client("opc.tcp://192.168.187.24:4840/htwdresden/server/")
# bekommt man auch über if-Config raus
#client = Client("opc.tcp://127.0.0.1:4840/htwdresden/server/")
try:
    client.connect()
    myNode = client.get_node("ns=2;i=5")
finally:
    client.disconnect()

while True:
    temperature = sensor.get_temperature()  # Sensorwert abfragen
    #print("The temperature is %s celsius" % temperature)
    myNode.set_value(temperature) 
    print("The temperature is " + str(temperature) + " celsius")    # Sensowert anzeigen
    time.sleep(1)                                                   # Warten, da die Änderungen 