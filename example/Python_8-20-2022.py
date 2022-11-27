import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (23, 17, 14)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
    
while(True):
    GPIO.output(23,True)
    time.sleep(5)
    GPIO.output(23,False)
    GPIO.output(17,True)
    time.sleep(2)
    GPIO.output(17,False)
    GPIO.output(14, True)
    time.sleep(3)
    GPIO.output(14,False)
