import RPi.GPIO as GPIO
from time import sleep
# import time

GPIO.setmode(GPIO.BCM)              # Nutze Bezeichnung BCM

InputPin = 17                       # GPIO 17, am Index 11
GPIO.setup(InputPin, GPIO.IN)      # Definieren, den als Input

while True:
    state = GPIO.input(InputPin)    # Abfrage des Zustandes an definierten Pin
    print("Der Zustand ist: " + str(state))

