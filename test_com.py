# クライアント側で利用するテスト用ソースです。

from com_socket import SupportSocketClient

server = SupportSocketClient('192.168.43.120', 55555)

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
