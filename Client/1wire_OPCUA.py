import time
from opcua import Client
from opcua import ua
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()                # Eine Instanz aus der Bibliothek erstellen

client = Client("opc.tcp://192.168.187.24:4840/htwdresden/server/")
# bekommt man auch über if-Config raus
#client = Client("opc.tcp://127.0.0.1:4840/htwdresden/server/")
try:
    client.connect()
except:
    print("FEHLER")


fehler = False
while True:
    if fehler:
        try:
            client.connect()
            fehler = False
        except:
            print("Verbindungsaufbau nicht möglich")

    try:    
        temperature = sensor.get_temperature()  # Sensorwert abfragen

        var = client.get_node("ns=2;i=5")
        var.set_value(temperature) 

        print("The temperature is " + str(temperature) + " celsius")    # Sensowert anzeigen
    except:
        fehler = True

    time.sleep(1)  

client.disconnect()