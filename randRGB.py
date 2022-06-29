import RPi.GPIO as GPIO
import time
from random import randint

rPin = 19
gPin = 13
bPin = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)

red = GPIO.PWM(rPin, 100)
green = GPIO.PWM(gPin, 100)
blue = GPIO.PWM(bPin, 100)

red.start(0)
green.start(0)
blue.start(0)

try:
    while True:
        r = randint(0,100)
        g = randint(0,100)
        b = randint(0,100)
        red.ChangeDutyCycle(r)
        green.ChangeDutyCycle(g)
        blue.ChangeDutyCycle(b)
        print("Red: " + str(r) + "\tGreen: " + str(g) + "\tBlue: " + str(b))
        time.sleep(.1)
                    
        
except KeyboardInterrupt:
    GPIO.cleanup()

