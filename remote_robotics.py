# coding=utf-8
from com_socket import *
from hexapod import *


def control_hexapod():
    # host = socket.gethostname()
    # ip = socket.gethostbyname(host) # 何故かlocalhost取ってくる...
    ip = '192.168.10.10'
    port = 55555
    CMD_QUIT = 999

    connection = SupportSocketServer(ip, port)

    hexapod = Hexapod2axis()
    hexapod.on_neutral()
    hexapod.start_control()

    try:
        while True:

            data = int.from_bytes(connection.recv_raw(), 'big')

            if data == CMD_QUIT:
                quit()

            hexapod.mState = data

    finally:
        connection.close()


def test_hexapod():
    hexapod = Hexapod2axis()
    hexapod.on_forward()


if __name__ == '__main__':
    control_hexapod()
