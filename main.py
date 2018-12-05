# coding=utf-8
from tests import *
from servo import *
from com_socket import *

if __name__ == '__main__':

    host = "192.168.10.7"  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    connection = SupportSocketServer(host, port)

    try:

        while True:
            data = connection.recv_raw()

            if data == b'a':
                print("aaa")
                break

            elif data == b'b':
                print("bbb")
                break

            elif data == b'q':
                print("quit")
                break

    finally:
        connection.close()
