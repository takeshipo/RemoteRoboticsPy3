import socket

host = "192.168.1.100"
port = 49152  # wellknownにぶつからない適当なポート番号

print('クライアントからの接続待ち')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
server.bind((host, port))  # 紐付け?をする
server.listen(5)  # 接続の待受をする。キューの最大数を指定。（なんの？）

client_socket, client_info = server.accept()
date = client_socket.recv(4096)

print('データ取得',date)
