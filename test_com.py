# サーバー側で利用するテスト用ソースです。

from com_socket import *
from time import sleep

server = SupportSocketServer('', 55555)

try:
    while True:
        sleep(10)
        data = {b'a',b'c',b'd',b'e'}
        server.send_byte(data)
        print('送信')


except KeyboardInterrupt:
    print('通信を終了します。')
    pass

finally:
    server.close()
