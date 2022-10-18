import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
input_pin = (17, GPIO.IN) # GPIO 17 (physical pin 11)
GPIO.setup(*input_pin)

while True:
    state = GPIO.input(input_pin[0])
    print(f"State: {state}")
    sleep(1)

#  scp .\rpi_pin.py pi@192.168.187.239:/home/pi