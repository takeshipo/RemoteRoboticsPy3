import socket


class socket_communication(object):
    # TODO : 現在、TCP/IPのみしか対応しないが、コンストラクタの引数protocolでTCPかUDP（それ以外）に対応するようにする
    def __init__(self, host_num, port_num, recv=1024, protocol='TCP/IP'):
        self.host = host_num
        self.port = port_num
        self.recv = recv

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
        self.server_socket.bind((host_num, port_num))  # 紐付けする
        self.server_socket.listen(5)  # 接続の待受をする。キューの最大数を指定。（なんの？）

        self.client_socket, self.client_info = self.server_socket.accept()
        print("接続完了")

    def close_socket(self):
        print('通信を終了します。')
        self.client_socket.close()
        self.server_socket.close()

    def get_date(self):
        date = self.client_socket.recv(self.recv)
        return date

    def send_date(self, date):
        self.client_socket.send(date)
