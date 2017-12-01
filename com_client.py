# kクライアント側で利用するテスト用ソースです。

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('接続を開始します。')
client.connect(('192.168.1.100',49152))

while True:
    print('入力してください。')
    date = input()
    client.send(date)
