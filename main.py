import RPi.GPIO as GPIO
import time
import os
#Ustawienia numeracji PIN
GPIO.setmode(GPIO.BOARD) 
#Ala ma kota i psa
#Ustawienie jako wejscie
GPIO.setup(11, GPIO.IN)



while True: 
    var=GPIO.input(11)
    if var:
    print 1 > /sys/class/leds/led0/brightness
    print (GPIO.input(11))

    else: 
    print 0 > /sys/class/leds/led0/brightness
    