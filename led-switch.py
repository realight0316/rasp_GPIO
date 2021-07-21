import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.OUT)

try:
    while(1):
        if(GPIO.input(8)==1):
            GPIO.output(10, GPIO.HIGH)
        else:
            GPIO.output(10, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
#finally:
#    print("Finally!")
#    GPIO.cleanup()