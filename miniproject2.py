import paho.mqtt.client as mqtt         # MQTT
import drivers                          # LCD
from time import sleep                  # sleep
from subprocess import check_output     # IP

display = drivers.Lcd()         # 숏컷 생성
client = mqtt.Client()          # 숏컷 생성
IP = (check_output(["hostname", "-I"]).split()[0]).decode("utf-8") # 현 로컬IP를 utf-8로 변환하여 저장

display.lcd_display_string('B:              ', 2)
try:
    num_cols = 14               # LCD 16칸 - 'B:'
    client.connect("localhost") # 현 IP로 연결

    while True:
        text = input()
        print('send:: ' + text)
        client.publish('msg_sub', text) # 토픽'msg_sub'으로 입력 메세지 전송

        if(text == '/ip'):      # /ip 입력시 로컬아이피 LCD에 출력
            for sec in range(5, 0, -1): # 5초 후 LCD 초기화
                display.lcd_display_string("_Let's check IP_", 1)
                display.lcd_display_string(IP + '  (' + str(sec), 2)
                sleep(1)
            display.lcd_clear()
            display.lcd_display_string('B:', 2)

        elif len(text) > num_cols:      # 해당 내용이 14자보다 길면 한칸씩 움직이면서 출력
            for do_triple in range(2):  # 2회 반복
                display.lcd_display_string('B:' + text[:num_cols], 2)
                sleep(1)
                for i in range(len(text) - num_cols + 1):
                    text_to_print = text[i:i+num_cols]
                    display.lcd_display_string('B:'+ text_to_print, 2)
                    sleep(0.2)
                sleep(2)
            display.lcd_display_string('B:              ', 2)
             
        else:
            display.lcd_display_string('B:' + text, 2)
            sleep(7)
            display.lcd_display_string("B:              ", 2)
        
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()

