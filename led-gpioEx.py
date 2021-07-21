import RPi.GPIO as GPIO
import time

def led(pin1, pin2, t):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)

    GPIO.output(pin1, True)
    ##GPIO.output(pin2, True)
    time.sleep(t) 

    ##GPIO.cleanup(pin1)
    GPIO.output(pin1, False)
    GPIO.output(pin2, True)
    time.sleep(t)
    GPIO.output(pin2, False)
    
for x in range(5):
    led(18, 16, 2) # 18번 핀에 끼운 LED를 5초동안 점등
    