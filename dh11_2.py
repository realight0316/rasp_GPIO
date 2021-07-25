import time
import adafruit_dht
import RPi.GPIO as GPIO
import board

sensor = adafruit_dht.DHT11(board.D18)
print(sensor)

try:

    while True :
        c = sensor.temperature
        h = sensor.humidity
        
        if h is not None and c is not None :
            print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(c, h))
        
        else :
            print('Read error')
                
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.clear(sensor)