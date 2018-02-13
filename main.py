# coding=utf-8
from pwm import SupportServoDriver
from com_server import SupportSocketCom
from servo import *
import socket
import time
import serial
import random

# coding=utf-8
import smbus2
import time


def serial_test():
    try:
        socket_com = SupportSocketCom(host, port)
        # Arduinoとのシリアル通信を準備
        Arduino = serial.Serial('/dev/ttyUSB0', 9600)
        while True:
            data = socket_com.recv_date()
            if data == 'QUIT':
                break
            data = data.split(':')
            channel = int(data[0])
            angle = int(data[1])
            print('channel : {0}'.format(channel))
            print('angle : {0}\n'.format(angle))
            KRS2552RHV_Arduino(Arduino, channel, angle)
    finally:
        Arduino.close()


def servo_test():
    try:
        socket_com = SupportSocketCom(host, port)
        while True:
            data = socket_com.recv_date()
            if data == 'QUIT':
                break
            data = data.split(':')
            channel = int(data[0])
            angle = int(data[1])
            print('channel : {0}'.format(channel))
            print('angle : {0}\n'.format(angle))
            RS306MD(int(angle))
    finally:
        socket_com.close()


def i2c_test():
    try:
        socket_com = SupportSocketCom(host, port)
        while True:
            bus = smbus2.SMBus(1)

            SLAVE_ADDRESS = 0x04

            command = input("入力してください：")
            if command == '1':
                bus.write_byte(SLAVE_ADDRESS, ord('C'))
            elif command == 'r':
                reading = bus.read_byte(SLAVE_ADDRESS)
                print(reading)
    except KeyboardInterrupt:
        pass

    finally:
        socket_com.close_socket()


def com_i2c():
    try:
        SLAVE_ADDRESS = 0x04

        bus = smbus2.SMBus(1)
        # socket_com = SupportSocketCom(host, port)
        while True:
            # data = socket_com.recv_date()
            data = input("入力してください")
            data = data.split(':')

            channel = int(data[0])
            rotate = int(data[1]) + 135
            # rotate = int(data[1])

            value = int((rotate / 270) * (9500 - 5500) + 5500)
            low = value & 0xff
            high = value >> 8
            high = high & 0xff

            print('Log channel : {0}'.format(channel))
            print('Log rotate : {0}\n'.format(rotate))
            print('Log value : {0}\n'.format(value))

            bus.write_byte(SLAVE_ADDRESS, ord('D'))
            bus.write_byte(SLAVE_ADDRESS, channel)
            bus.write_byte(SLAVE_ADDRESS, low)
            bus.write_byte(SLAVE_ADDRESS, high)

    except KeyboardInterrupt:
        pass

    finally:
        # socket_com.close_socket()
        pass


if __name__ == '__main__':

    host = ''  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    # socket_com = SupportSocketCom(host, port)

    print('接続完了\nメニュー名の入力を待ちます...')
    # menu = socket_com.recv_date()
    menu = input()
    print(menu)

    if menu == 'COM_I2C':
        com_i2c()

    if menu == 'TEST_I2C':
        i2c_test()

    if menu == 'SERVO_TEST':
        servo_test()

    if menu == 'SERIAL_TEST':
        serial_test()
