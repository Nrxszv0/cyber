import RPi.GPIO as GPIO
import time
from random import randint

rPin = 19
gPin = 13
bPin = 6
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0x00FFFF, 0xFF00FF, 0xFFFFFF, 0x9400D3]

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

def map(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
        R_val = (col & 0x110000) >> 16
        G_val = (col & 0x001100) >> 8
        B_val = (col & 0x000011) >> 0

        R_val = map(R_val, 0, 255, 0, 100)
        G_val = map(G_val, 0, 255, 0, 100)
        B_val = map(B_val, 0, 255, 0, 100)
        
        R_val = map(R_val, 0, 6.667, 0, 100)
        G_val = map(G_val, 0, 6.667, 0, 100)
        B_val = map(B_val, 0, 6.667, 0, 100)

        

        red.ChangeDutyCycle(R_val)     # Change duty cycle
        green.ChangeDutyCycle(G_val)
        blue.ChangeDutyCycle(B_val)
        
        print("Red: " + str(R_val) + "\tGreen: " + str(G_val) + "\tBlue: " + str(B_val))
        
        



try:
    while True:
        for col in colors:
            setColor(col)
            time.sleep(.1)
       
                    
        
except KeyboardInterrupt:
    GPIO.cleanup()


