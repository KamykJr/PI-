import RPi.GPIO as GPIO
import time
#Ustawienia numeracji PIN
GPIO.setmode(GPIO.BOARD) 

#Ustawienie jako wejscie
GPIO.setup(11, GPIO.IN)

while True: 
    print (GPIO.input(11))
    time.sleep(0.5)