import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO


def on_connect(clinet, userdata, flags, rc):
    print("Connected ", str(rc))
    client.subscribe("message")
    client.subscribe("ledctrl")
    
def on_message(client, userdata, msg):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    print(str(msg.payload))
    print(msg.payload)
    if(msg.payload == b'led_on123'):
        GPIO.output(11, GPIO.HIGH)
    elif(msg.payload == b'led_off123'):
        GPIO.output(11, GPIO.LOW)
    

    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_subscribe = ctrl_led

client.connect("192.168.1.22")
client.loop_forever()