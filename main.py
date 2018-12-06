# coding=utf-8
from com_socket import *
from hexapod import Hexapod

if __name__ == '__main__':

    # ドメイン名、もしくはIPアドレス。
    # ドメイン名は socket.gethostname() で取得することもできる。
    host = "192.168.10.7"

    # wellknownと衝突しない適当なポート番号
    port = 55555

    connection = SupportSocketServer(host, port)

    hexapod = Hexapod()

    try:
        while True:
            data = connection.recv_str()

            if data == 'ON_FORWARD':
                print("ON_FORWARD")
                hexapod.on_foward()

            if data == 'ON_BACKWARD':
                print("ON_BACKWARD")
                hexapod.on_bacnkward()

            elif data == 'ON_RIGHT_TURN':
                print("ON_RIGHT_TURN")
                hexapod.on_right_turn()

            elif data == 'ON_LEFT_TURN':
                print("ON_LEFT_TURN")
                hexapod.on_left_turn()

            elif data == 'QUIT':
                quit()

    finally:
        connection.close()
