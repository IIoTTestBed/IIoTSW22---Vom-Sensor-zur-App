#therm sensor
from w1thermsensor import W1ThermSensor
#Matrix setup
from MyMax7219 import MyMatrix
#button
from gpiozero import Button
#opcua
from asyncua import Client
from asyncua import ua
#common
import time
from random import randint
import asyncio

#global vars+++
data = [26.0,25.0,27.0,28.0,29.0,30.0,32.0,35.0,28.0,27.0,26.0,25.0,24.0,23.0,22.0,23.0]

stateNode = 7
ownNode = 3
minNode = 3
maxNode = 5
currentNode = minNode

async def main():
    global ownNode
    global currentNode
    global data
    oldNode = 0

    async with Client("opc.tcp://192.168.187.24:4840/htwdresden/server/") as client:
        while True:
            #get current node
            currentNodeTemp = currentNode

            #get current Node value
            var = client.get_node(f"ns=2;i={currentNodeTemp}")
            serverValue = await var.get_value()

            #sensor data aquisition
            var = client.get_node(f"ns=2;i={ownNode}")
            temp = readTempSensor()
            #set node value
            await var.write_value(temp)

            #Debug
            print(f"Read Node:  {currentNodeTemp} -> Value: {serverValue}")
            print(f"Write Node: {temp} -> Value: {temp}")

            #if node changes
            if currentNodeTemp != oldNode:
                setListValues(serverValue)
                matrix.clear()
                oldNode=currentNodeTemp
                #set current sensor to node
                var = client.get_node(f"ns=2;i={stateNode}")
                await var.write_value(currentNodeTemp-(minNode-1))
                #show node on matrix
                matrix.letter(str(currentNodeTemp-(minNode-1)),1)
                time.sleep(0.6)
            else:
                forwardArray(serverValue)

            #data mapping and display
            fmax = max(data)+0.5
            fmin = min(data)-0.5
            scale = (fmax-fmin)/8

            for i in range(0,16):
                for j in range(0,8):
                    if j >= 8-(round((data[15-i]-fmin)/scale)):
                        matrix.pixel(15-i,j,1)
                    else:
                        matrix.pixel(15-i,j,0)
                time.sleep(0.008)
            #matrix.clear()


def readTempSensor():
    #get all available sensors
    sensors = W1ThermSensor.get_available_sensors();
    if(len(sensors)<=0):
        print("Error: No temperature sensor found!")
        return 0
    else:
        #only use first sensor
        return sensors[0].get_temperature()
        #print(f"Sensor \'{sensor.id}\' -> Temperature[°C] = {sensor.get_temperature()}")

def setListValues(value):
    for i in range(len(data)):
        data[i]=value

def forwardArray(newValue):
    #forward array
    for i in range(0,15):
        data[i]=data[i+1]
    data[len(data)-1]=newValue

def simulateData():
    newDirection = float(randint(-15,15)/10)
    return data[len(data)-1]+newDirection

def buttonPressed():
    global currentNode
    currentNode += 1
    if currentNode > maxNode:
        currentNode=minNode

    print(f"Button pressed -> Node {currentNode}")


#init++++++++++++++++++++++++++++++++++++++
matrix = MyMatrix()
button=Button(17)
button.when_activated=buttonPressed
#on boot
matrix.brightness(140)
matrix.showMessage('...Starting OPC-UA...', 0.1)
#matrix.showMessage('Display Temperature Device: 1')
matrix.clear()
#start opcua client
asyncio.run(main())

    