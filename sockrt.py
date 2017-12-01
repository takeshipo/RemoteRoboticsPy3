import socket


# TODO: 適切な例外処理がなされていない。

class support_socket_com(object):
    # TODO : 現在、TCP/IPのみしか対応しないが、コンストラクタの引数protocolでTCPかUDP（それ以外）に対応するようにする
    def __init__(self, host, port, recv=1024, protocol='TCP/IP'):
        self.host = host
        self.port = port
        self.recv = recv

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
        self.server_socket.bind((host, port))  # 紐付けする
        self.server_socket.listen(5)  # 接続の待受をする。キューの最大数を指定。（なんの？）

        self.client_socket, self.client_info = self.server_socket.accept()
        print("接続完了")

    def close_socket(self):
        print('通信を終了します。')
        self.client_socket.close()
        self.server_socket.close()

    def get_date(self):
        try:
            date = self.client_socket.recv(self.recv)
            return date

        except IOError:
            self.client_socket()
            print('エラー発生！通信を終了します。')

    def send_date(self, date):
        try:
            self.client_socket.send(date)

        except IOError:
            self.close_socket()
            print('エラー発生！通信を終了します。')
