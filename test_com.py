# サーバー側で利用するテスト用ソースです。

from com_socket import *

server = SupportSocketServer('', 55555)

try:
    while True:
        print('入力してください')
        date = input()
        server.send_str(date)

except KeyboardInterrupt:
    print('通信を終了します。')
    pass

finally:
    server.close()
