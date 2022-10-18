import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)                                  # Nutze Bezeichnung BCM zum Ansprechen der Pins

InputPin = 17                                           # GPIO 17, am Index 11
GPIO.setup(InputPin, GPIO.IN)                           # Pin als Input definieren (Pins am Raspb. sind je ins/outs!)

while 1:
    state = GPIO.input(InputPin)                        #Abfrage des Zustandes an definiertem Pin
    print("Der Zustand ist:", str(state))
