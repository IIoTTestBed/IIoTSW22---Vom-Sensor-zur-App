from MyMax7219 import MyMatrix
from random import randint
import time

data = [26.0,25.0,27.0,28.0,29.0,30.0,32.0,35.0,28.0,27.0,26.0,25.0,24.0,23.0,22.0,23.0]

def aqrData():
    newDirection = float(randint(-15,15)/10)
    newPoint = data[len(data)-1]+newDirection

    #forward array
    for i in range(0,15):
        data[i]=data[i+1]
    data[len(data)-1]=newPoint

matrix = MyMatrix()

#matrix.showMessage('Starting OPC-UA...')
time.sleep(1)
#matrix.showMessage('Display Temperature Device: 1')

matrix.clear()
matrix.brightness(150)

time.sleep(0.2)

while True:

    #data aquisition
    aqrData()

    #data mapping
    fmax = max(data)
    fmin = min(data)
    scale = (fmax-fmin)/8

    for i in range(0,16):
        for j in range(0,8):
            if j >= (8-round((data[i]-fmin)/scale)):
                matrix.pixel(i,j,1)
            else:
                matrix.pixel(i,j,0)
        time.sleep(0.02)
    
    time.sleep(1)
    #matrix.clear()