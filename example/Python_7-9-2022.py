import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (3,5,9,11,8,7,10,1)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment,0)

num = {
    '0':(0,0,0,0,0,0,1,1),
    '1':(1,0,0,1,1,1,1,1),
    '2':(0,0,1,0,0,1,0,1),
    '3':(0,0,0,0,1,1,0,1),
    '4':(1,0,0,1,1,0,0,1),
    '5':(0,1,0,0,1,0,0,1),
    '6':(0,1,0,0,0,0,0,1),
    '7':(0,0,0,1,1,0,1,1),
    '8':(0,0,0,0,0,0,0,1),
    '9':(0,0,0,0,1,0,0,1)
    }

for index in range(0,10):
    s=str(index)
    for loop in range(0,8):
        print (loop)
        GPIO.output(segments[loop],num[s][loop] )
    time.sleep(1)
GPIO.cleanup()