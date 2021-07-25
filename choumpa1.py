import RPi.GPIO as GPIO
import time

print("HC-SR04 Start")

GPIO.setmode(GPIO.BCM)
# green : Pin 11 : 17(Trig)
GPIO.setup(23, GPIO.OUT)
# blue : Pin 12 : 18(Echo)
GPIO.setup(24, GPIO.IN)

try:
    while True:
        
        GPIO.output(23, False)
        time.sleep(0.5)

        GPIO.output(23, True)
        time.sleep(0.00001)
        GPIO.output(23, False)

        # 18번이 OFF가 되는 시점을 시작시간으로 설정
        while GPIO.input(24) == 0:
            start = time.time()

        # 18번이 ON이 되는 시점을 반사파 수신시간으로 설정
        while GPIO.input(24) == 1:
            stop = time.time()

        # 초음파가 되돌아오는 시간차로 거리를 계산한다
        time_interval = stop - start
        distance = time_interval * 17000
        distance = round(distance, 2)

        print("Distance => ", distance, "cm")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("HC-SR04 End")