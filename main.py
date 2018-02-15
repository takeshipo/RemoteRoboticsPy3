# coding=utf-8
from pwm import SupportServoDriver
from com_socket import SupportSocketClient
from servo import *
import serial
import smbus2
import time


def serial_send(socket_com):
    # Arduinoとのシリアル通信を準備
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    try:
        while True:
            data = socket_com.recv_str()
            if data == 'QUIT':
                break
            data = data.split(':')
            id = int(data[0])
            rotate = int(data[1])
            print('channel : {0}'.format(id))
            print('angle : {0}\n'.format(rotate))

            arduino.write(b'A')  # 文字を送信
            num = 1
            arduino.write(num.to_bytes(1, 'big'))  # 数字を送信

    finally:
        arduino.close()
        socket_com.close()


def servo_test(socket_com):
    try:
        while True:
            data = socket_com.recv_str()

            data = data.split(':')
            channel = int(data[0])
            angle = int(data[1])
            print('[Receive]')
            print('channel : {0}'.format(channel))
            print('angle : {0}\n'.format(angle))

            # RS306MD(int(angle))　# ここで呼び出すサーボモータを変える
    finally:
        socket_com.close()

def i2c_test():
    try:
        bus = smbus2.SMBus(1)
        SLAVE_ADDRESS = 0x04
        while True:

            cmd = input("入力してください：")
            if cmd == 'send':
                bus.write_byte(SLAVE_ADDRESS, ord('A'))
            elif cmd == 'receive':
                read_data = bus.read_byte(SLAVE_ADDRESS)
                print(read_data)

    except KeyboardInterrupt:
        print("プログラムを終了します...")
        pass


def i2c_krs2552rhv(socket_com):
    try:
        SLAVE_ADDRESS = 0x04
        bus = smbus2.SMBus(1)
        while True:
            data = socket_com.recv_str()
            data = data.split(':')

            channel = int(data[0])
            rotate = int(data[1]) + 135
            # rotate = int(data[1])

            value = int((rotate / 270) * (9500 - 5500) + 5500)
            low = value & 0xff
            high = value >> 8
            high = high & 0xff

            print('Log channel : {0}'.format(channel))
            print('Log rotate : {0}'.format(rotate))
            print('Log value : {0}\n'.format(value))

            bus.write_byte(SLAVE_ADDRESS, ord('D'))
            bus.write_byte(SLAVE_ADDRESS, channel)
            bus.write_byte(SLAVE_ADDRESS, low)
            bus.write_byte(SLAVE_ADDRESS, high)
            bus.close()

    except KeyboardInterrupt:
        pass

    finally:
        socket_com.close_socket()
        pass


if __name__ == '__main__':
    host = '192.168.43.120'  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    socket_com = SupportSocketClient(host, port)

    # Arduino = serial.Serial('/dev/ttyUSB0', 9600)

    servo_test(socket_com)

    # print('接続完了\nメニュー名の入力を待ちます...')
    # # menu = socket_com.recv_date()
    # menu = input()
    # print(menu)
    #
    # if menu == 'COM_I2C':
    #     i2c_krs2552rhv(socket_com)
    #
    # elif menu == 'TEST_I2C':
    #     i2c_test()
    #
    # elif menu == 'SERVO_TEST':
    #     servo_test(socket_com)
    #
    # elif menu == 'SERIAL_TEST':
    #     serial_send(socket_com)

