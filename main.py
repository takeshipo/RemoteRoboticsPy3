from pwm import support_servo_driver
from sockrt import support_socket_com
from khr3hv import *
import socket

if __name__ == '__main__':

    host = socket.gethostname()  # ドメイン名を調べる
    port = 49152  # wellknownにぶつからない適当なポート番号
    socket_com = support_socket_com(host, port)

    while True:
        message = socket_com.get_date()

        if message == 'SERVO_TEST':
            while True:
                value = socket_com.get_date()
                KRS2552RHV(value)
                if value == 'QUIT':
                    break

        if message == 'COM_TEST':
            while True:
                value = socket_com.get_date()
                print(value)
                if value == 'QUIT':
                    break