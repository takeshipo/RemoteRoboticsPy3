# coding=utf-8
import socket


# TCP扱うクラス
# TODO:このクラス一つにまとめる！
# TODO: 適切な例外処理がなされていない。

class SupportSocketServer:
    def __init__(self, host, port, recv_size=1024):
        self.host = host
        self.port = port
        self.recv_size = recv_size

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
        self.server_socket.bind((host, port))  # 紐付けする
        self.server_socket.listen(5)  # 接続の待受をする。キューの最大数を指定。（なんの？）

        print('クライアントからの接続を待ち....')
        self.client_socket, self.client_info = self.server_socket.accept()
        print("完了！")

    def close_socket(self):
        print('通信を終了します。')
        self.client_socket.close()
        self.server_socket.close()

    # 受け取ったbyteコードをutf8にデコードして返す
    def recv_str(self):
        try:
            date = self.client_socket.recv(self.recv_size)
            return bytes(date).decode('utf-8')

        except IOError:
            self.client_socket()
            print('受信でエラー発生！通信を終了します。')

    def send_str(self, date):
        try:
            self.client_socket.send(bytes(date.encode('utf-8')))

        except IOError:
            self.close_socket()
            print('送信でエラー発生！通信を終了します。')

    def close(self):
        self.server_socket.close()
        self.client_socket.close()


class SupportSocketClient:
    def __init__(self, address, port, recv_size=1024):
        self.host = address
        self.port = port
        self.recv_size = recv_size

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
        print('サーバーに接続します....')
        self.server_socket.connect((address, port))
        print('接続完了')

    def close_socket(self):
        print('通信を終了します。')
        self.server_socket.close()

    # 受け取ったbyteコードをutf8にデコードして返す
    def recv_str(self):
        try:
            date = self.server_socket.recv(self.recv_size)
            return bytes(date).decode('utf-8')

        except IOError:
            print('受信でエラー発生！通信を終了します。')
            self.server_socket.close()

    def send_str(self, date):
        try:
            self.server_socket.send(bytes(date.encode('utf-8')))

        except IOError:
            print('送信でエラー発生！通信を終了します。')
            self.close_socket()

    def close(self):
        self.server_socket.close()