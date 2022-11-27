import RPi.GPIO as GPIO # GPIO import
GPIO.setmode(GPIO.BOARD) # Board Mode
GPIO.setwarnings(False) # Warning Check

gpio_pin = 12 # Buzzer Pin number
scale = [261, 294, 329, 349, 392, 440, 493, 523] # scale
SW=[3,5,7,11,13,15,19] # Switch pin number (7 types)
GPIO.setup(gpio_pin,GPIO.OUT) # Buzzer ready
for i in range(7):
    GPIO.setup(SW[i],GPIO.IN) # Switch ready
    
p=GPIO.PWM(gpio_pin,100)
p.start(10)
print("If you want to quit, press Ctrl C.")
try:
    while True:
        if GPIO.input(SW[0]) == GPIO.HIGH :
            p.ChangeFrequency(scale[0])
            
        if GPIO.input(SW[1]) == GPIO.HIGH :
            p.ChangeFrequency(scale[1])
            
        if GPIO.input(SW[2]) == GPIO.HIGH :
            p.ChangeFrequency(scale[2])
            
        if GPIO.input(SW[3]) == GPIO.HIGH :
            p.ChangeFrequency(scale[3])
            
        if GPIO.input(SW[4]) == GPIO.HIGH :
            p.ChangeFrequency(scale[4])
            
        if GPIO.input(SW[5]) == GPIO.HIGH :
            p.ChangeFrequency(scale[5])
            
        if GPIO.input(SW[6]) == GPIO.HIGH :
            p.ChangeFrequency(scale[6])
        GPIO.output(gpio_pin,True)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
      
finally:
    p.stop()
    GPIO.cleanup() # Finish
