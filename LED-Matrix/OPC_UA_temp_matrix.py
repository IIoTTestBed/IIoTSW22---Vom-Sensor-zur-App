from telnetlib import OLD_ENVIRON
from w1thermsensor import W1ThermSensor
from os import system
from MyMax7219 import MyMatrix
from random import randint
from gpiozero import Button
import time
import asyncio
from asyncua import Client
from asyncua import ua

data = [26.0,25.0,27.0,28.0,29.0,30.0,32.0,35.0,28.0,27.0,26.0,25.0,24.0,23.0,22.0,23.0]
ownNode = 3
minNode = 3
maxNode = 5
currentNode = minNode
oldNode = currentNode

async def main():
    global ownNode
    global currentNode
    global oldNode
    global data

    async with Client("opc.tcp://192.168.187.24:4840/htwdresden/server/") as client:
        while True:
            #get current Node value
            var = client.get_node(f"ns=2;i={currentNode}")
            serverValue = await var.get_value()

            #sensor data aquisition
            var = client.get_node(f"ns=2;i={ownNode}")
            temp = readTempSensor()
            await var.write_value(temp)

            #Debug
            print(f"Read Node:  {currentNode} -> Value: {serverValue}")
            print(f"Write Node: {temp} -> Value: {temp}")

            if currentNode != oldNode:
                setListValues(serverValue)
                matrix.clear()
                oldNode=currentNode
            else:
                forwardArray(serverValue)

            #data mapping
            fmax = max(data)+0.5
            fmin = min(data)-0.5
            scale = (fmax-fmin)/8

            for i in range(0,16):
                for j in range(0,8):
                    if j >= 8-(round((data[15-i]-fmin)/scale)):
                        matrix.pixel(15-i,j,1)
                    else:
                        matrix.pixel(15-i,j,0)
                time.sleep(0.01)
            
            time.sleep(0.01)
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
matrix.showMessage('...Starting OPC-UA...', 0.1)
#matrix.showMessage('Display Temperature Device: 1')
matrix.clear()
matrix.brightness(150)
#start opcua client
asyncio.run(main())

    