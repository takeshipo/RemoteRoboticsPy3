from pwm import support_servo_driver
from com_server import support_socket_com
from khr3hv import *
import socket
import time

if __name__ == '__main__':

    # host = socket.gethostname()  # ドメイン名を調べる
    host = ''
    port = 55555  # wellknownにぶつからない適当なポート番号
    socket_com = support_socket_com(host, port)

    try:
        while True:

            print('接続完了\nメニューを入力してください。')
            message = socket_com.recv_date()

            print(message)

            if message == 'SERVO_TEST':
                while True:
                    angle = socket_com.recv_date()
                    print('degree:',int(angle))
                    KRS2552RHV(int(angle))
                    if angle == 'QUIT':
                        break

            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        print('Log:finally')
        socket_com.close_socket()
