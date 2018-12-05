# coding=utf-8
import socket
import concurrent.futures


# SOCK_STREAMでTCP、SOCK_DGRAMでUDP
# socket.AF_INET

class TcpServer:
    def __init__(self, address, port, recv_size=1024):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address, port))
        self.socket.listen(5)

        print('クライアントデバイスからの接続待ち....')
        self.client_socket, self.client_info = self.socket.accept()
        print("接続完了")

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.recv_func = lambda: self.client_socket.recv(recv_size)
        self.send_func = lambda data: self.client_socket.send(data)

    def recv_str(self):
        future = self.executor.submit(self.recv_func)
        result = future.result()
        # 受け取ったデータをutf8にデコードする
        return bytes(result).decode('utf-8')

    def send_str(self, data):
        self.executor.submit(self.send_func, bytes(data.encode('utf-8')))

    def recv_raw(self):
        future = self.executor.submit(self.recv_func)
        return future.result()

    def send_str(self, data):
        self.executor.submit(self.send_func, bytes(data.encode('utf-8')))

    def send_bytes(self, data):
        self.executor.submit(self.send_func, data)

    def close(self):
        print('通信を終了します。')
        self.socket.close()
        self.client_socket.close()


class SupportSocketClient:
    def __init__(self, address, port, recv_size=1024):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAMでTCPを指定している。
        print('サーバーに接続します....')

        # 関数を定義して代入
        # TODO : Lambdaで定義できない？

        # 受け取ったbyteコードをutf8にデコードして返す
        def r_func():
            try:
                data = self.socket.recv(recv_size)
                return data

            except IOError:
                print('受信でエラー発生！通信を終了します。')
                self.socket.close()

        self.recv_func = r_func

        def s_func(data):
            try:
                self.socket.send(data)

            except IOError:
                print('送信でエラー発生！通信を終了します。')
                socket()

        self.send_func = s_func

        # 接続処理
        try:
            self.socket.connect((address, port))
            print('接続完了')
        except IOError:
            print('コネクトでエラー発生。')

    def close(self):
        print('通信を終了します。')
        self.socket.close()

    def recv_str(self):
        future = self.executor.submit(self.recv_func)
        result = future.result()
        return bytes(result).decode('utf-8')

    def recv_raw(self):
        future = self.executor.submit(self.recv_func)
        return future.result()

    def send_str(self, data):
        self.executor.submit(self.send_func, bytes(data.encode('utf-8')))

    def send_byte(self, data):
        self.executor.submit(data)
