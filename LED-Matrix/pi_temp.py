import time
from w1thermsensor import W1ThermSensor
from os import system

while True:
    #get all available sensors
    for sensor in W1ThermSensor.get_available_sensors():
        print(f"Sensor \'{sensor.id}\' -> Temperature[°C] = {sensor.get_temperature()}")
        time.sleep(0.01)
    print("+++++++++++++++++")
    time.sleep(1)
    
