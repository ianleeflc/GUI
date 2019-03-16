import RPi.GPIO as GPIO
from time import sleep

led_pin=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm=GPIO.PWM(led_pin, 100) # created a PWM object
pwm.start(0) # started PWM at 0% duty cycle

try:
    while 1: # loop will run forever
        for x in range(100): # this loop will run 100 times
            pwm.ChangeDutyCycle(x)
            sleep(0.01)

        for x in range(100,0,-1):
            pwm.ChangeDutyCycle(x)
            sleep(0.01)
# if keyboard interrupt ctrl+c is pressed
except KeyboardInterrupt:
    pass
pwm.stop() # stop PWM
GPIO.cleanup() # make all output pin low
