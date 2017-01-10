import RPi.GPIO as GPIO
import time

inPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(inPin, GPIO.FALLING, bouncetime=100)

while True:
    value = GPIO.input(inPin)
    if value == GPIO.LOW:
        print "Magnetic Field Detected!"
        time.sleep(1)
    else:
        print "No Magnetic Field Detected!"
        time.sleep(1)  
GPIO.cleanup()        
        
