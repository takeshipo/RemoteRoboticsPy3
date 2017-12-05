import socket
from abc import ABCMeta, abstractmethod


# ソケット通信の基底クラス。Bluetoothもインヘリタンスして実装する。
# そもそも、こんなJava(型付け言語)くさいこと必要？
class support_communication(metaclass=ABCMeta):
    @abstractmethod
    def close_socket(self):
        raise NotImplementedError()

    @abstractmethod
    def recv_date(self):
        raise NotImplementedError()

    @abstractmethod
    def send_date(self, date):
        raise NotImplementedError()


# TCP,UDPを扱うクラス
# TODO: 適切な例外処理がなされていない。
class support_socket_com(support_communication):
    # TODO : 現在、TCP/IPのみしか対応しないが、コンストラクタの引数protocolでTCPかUDP（それ以外）に対応するようにする
    def __init__(self, host, port, recv_size=1024, protocol='TCP/IP'):
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
    def recv_date(self):
        try:
            date = self.client_socket.recv(self.recv_size)
            return bytes(date).decode('utf-8')

        except IOError:
            self.client_socket()
            print('エラー発生！通信を終了します。')

    def send_date(self, date):
        try:
            self.client_socket.send(date)

        except IOError:
            self.close_socket()
            print('エラー発生！通信を終了します。')
