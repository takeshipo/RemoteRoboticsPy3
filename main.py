from pwm import SupportServoDriver
from com_server import SupportSocketCom
from khr3hv import *
import socket
import time

if __name__ == '__main__':

    host = ''  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    socket_com = SupportSocketCom(host, port)

    try:
        while True:

            print('接続完了\nメニュー名の入力を待ちます...')
            menu = socket_com.recv_date()
            print(menu)

            if menu == 'SERVO_TEST':
                while True:
                    data = socket_com.recv_date()
                    if data == 'QUIT':
                        break
                    data = data.split(':')
                    channel = data[0]  # .split(',')
                    angle = data[1]
                    print('channel : ', channel)
                    print('angle : ', int(angle))
                    RS306MD(int(angle))

    except KeyboardInterrupt:
        print("ソケット通信を終了します。")
        pass

    finally:
        socket_com.close_socket()
