# kクライアント側で利用するテスト用ソースです。

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('接続を開始します。')
client.connect(('192.168.1.100', 55555))

print('メニュー')
date = input()
client.send(bytes(date.encode('utf-8')))

try:
    while True:
        print('入力してください。')
        date = input()
        client.send(bytes(date.encode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    print('通信を終了します。')
    client.close()