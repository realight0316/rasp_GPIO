import paho.mqtt.client as mqtt         # MQTT
import drivers                          # LCD
from picamera import PiCamera           # Camera
from time import sleep                  # sleep
from subprocess import check_output     # IP

display = drivers.Lcd()
client = mqtt.Client()
IP = (check_output(["hostname", "-I"]).split()[0]).decode("utf-8") # 현 로컬IP를 utf-8로 변환하여 저장

def on_connect(clinet, userdata, flags, rc):
    print("Connected complete :", str(rc))
    client.subscribe("msg_pub")
    display.lcd_display_string('A:    Online    ', 1)
    
def on_message(client, userdata, msg):
    text = msg.payload.decode("utf-8")
    num_cols = 14       # LCD 16칸 - 'A:'
    
    print('Received:: ' + text)
    display.lcd_display_string('A:              ', 1)
    
    if(text == '/camera'):
        camera = PiCamera()
        camera.rotation = 180 # 카메라 180도 회전하여 촬영

        camera.start_preview()
        display.lcd_display_string('Smile :)', 1)
        sleep(5) # preview가 열린뒤 몇초뒤에 사진을 촬영해야한다
        camera.capture('/home/pi/Desktop/pycam.jpg')    # 해당위치, 파일명으로 사진 촬영
        camera.stop_preview()
        
        f = open('/home/pi/Desktop/pycam.jpg', 'rb')
        filecontent = f.read()              # 파일 읽어들인다음
        myphoto = bytearray(filecontent)    # 비트어레이로 변환
        client.publish('mypic', myphoto, 0) # 변환된 값을 해당 토픽으로 전송

        print("Please check image file!")
        display.lcd_display_string('___Thank you____', 1)
        display.lcd_display_string('____See ya!_____', 2)
        sleep(2)
        display.lcd_clear()
        
    if(text == '/ip'):      # /ip 입력시 로컬아이피 LCD에 출력
        for sec in range(5, 0, -1): # 5초 후 LCD 초기화
            display.lcd_display_string("_Let's check IP_", 1)
            display.lcd_display_string(IP + '  (' + str(sec), 2)
            sleep(1)
        display.lcd_clear()
        display.lcd_display_string('A:', 1)
        
    elif len(text) > num_cols:          # 해당 내용이 14자보다 길면 한칸씩 움직이면서 출력
            for do_triple in range(2):  # 2회 반복
                display.lcd_display_string('A:' + text[:num_cols], 1)
                sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i+num_cols]
                    display.lcd_display_string('A:'+ text_to_print, 1)
                    sleep(0.2)
                sleep(2)
            display.lcd_display_string('A:              ', 1)
             
    else:
        display.lcd_display_string('A:' + text, 1)
        sleep(7)
        display.lcd_display_string("A:              ", 1)
    
try:
    while True:
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("localhost")
        client.loop_forever()
        
except KeyboardInterrupt:
    print("\nCleaning up!")
    display.lcd_clear()
