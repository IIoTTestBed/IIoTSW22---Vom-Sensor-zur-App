import time
import asyncio
from asyncua import Client
from asyncua import ua
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()                # Eine Instanz aus der Bibliothek erstellen

async def main():
   async with Client("opc.tcp://192.168.187.24:4840/htwdresden/server/") as client:
# bekommt man auch über if-Config raus
#client = Client("opc.tcp://127.0.0.1:4840/htwdresden/server/")
        while True:
# try:
#     client.connect()
# except:
#     print("FEHLER")
            temperature = sensor.get_temperature()
            var = client.get_node("ns=2;i=4")
            data = await var.get_value()
            
            print(data) 
            print("The temperature is " + str(temperature) + " celsius")    # Sensowert anzeigen
            time.sleep(1)      

# while True:
    
#     temperature = sensor.get_temperature()  # Sensorwert abfragen
#     #print("The temperature is %s celsius" % temperature)
#     #myNode = client.get_node("ns=2;i=5")
#     #myNode get_value()
#     #myNode.set_value(10)
#     var = client.get_node("ns=2;i=4")
    
#     print(var.get_value()) # get value of node as a python builtin
#     #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
#     #var.set_value(3.9) # set node value using implicit data type

#     #myNode.set_value(ua.Variant([50], ua.VariantType.Double))
#     #var.set_value(temperature) 
#     print("The temperature is " + str(temperature) + " celsius")    # Sensowert anzeigen
#     time.sleep(1)                                                   # Warten, da die Änderungen 


# client.disconnect()
asyncio.run(main())
