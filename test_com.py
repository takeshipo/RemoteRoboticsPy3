# coding=utf-8
# サーバー側で利用するテスト用ソースです。

from com_socket import *
from time import sleep

server = TcpServer('', 55555)

try:
    while True:
        rotate = int(input('input:'))
        rotate_l = (rotate & 0xff).to_bytes(1, 'big')
        rotate_h = ((rotate >> 8) & 0xff).to_bytes(1, 'big')

        data = bytearray(0x00.to_bytes(1, 'big') + 0x01.to_bytes(1, 'big') + rotate_h + rotate_l)

        # data = b'abcd'
        # server.send_str(data)
        server.send_bytes(data)
        print('送信')


except KeyboardInterrupt:
    print('通信を終了します。')
    pass

finally:
    server.close()
