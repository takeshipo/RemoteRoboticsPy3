# coding=utf-8
from com_socket import *

if __name__ == '__main__':

    # ドメイン名、もしくはIPアドレス。
    # ドメイン名は socket.gethostname() で取得することもできる。
    host = "192.168.10.7"

    # wellknownと衝突しない適当なポート番号
    port = 55555

    connection = TcpServer(host, port)

    try:
        while True:
            data = connection.recv_str()

            if data == 'LED_1_ON':
                # 何かしらの処理。例としてLEDを点灯
                print("LED_1_ON")

            elif data == 'LED_2_ON':
                print("LED_2_ON")

            elif data == 'QUIT':
                print("quit")
                quit()
                break

    finally:
        connection.close()
