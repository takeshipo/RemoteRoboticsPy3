# coding=utf-8
from pwm import SupportServoDriver
from com_server import SupportSocketCom
from servo import *
import socket
import time
import serial
import random

if __name__ == '__main__':

    host = ''  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    # socket_com = SupportSocketCom(host, port)

    # Arduinoとのシリアル通信を準備
    Arduino = serial.Serial('/dev/ttyUSB0', 9600)

    try:
        while True:

            print('接続完了\nメニュー名の入力を待ちます...')
            # menu = socket_com.recv_date()
            menu = input()
            print(menu)

            if menu == 'SERVO_TEST':
                while True:
                    # data = socket_com.recv_date()
                    data = input()
                    if data == 'QUIT':
                        break
                    data = data.split(':')
                    channel = int(data[0])
                    angle = int(data[1])
                    print('channel : {0}', channel)
                    print('angle : {0}\n', angle)
                    # RS306MD(int(angle))
                    KRS2552RHV_Arduino(Arduino, channel, angle)

            if menu == 'SERIAL_TEST':
                while True:
                    channel = random.randint(0, 17)
                    angle = random.randint(0, 270)
                    KRS2552RHV_Arduino(Arduino, channel, angle)
                    print("send")
                    time.sleep(0.01)

    except KeyboardInterrupt:
        print("ソケット通信を終了します。")
        pass

    finally:
        Arduino.close()
        pass
        # socket_com.close_socket()
