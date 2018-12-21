# coding=utf-8
from servo import *
from com_socket import *


class Hexapod(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        # self.servo = ServoPwmConfigData().get_MG92B()  # ここでサーボを選択
        # self.pwm = SupportServoDriver(config_data=self.servo)

        self.state = 'ON_NEWTRAL'

        # self.forward = on_forward
        # self.backward = on_backward
        # self.left_turn = on_left_turn
        # self.right_turn = on_right_turn
        # self.stop = on_stop
        # self.neutral = on_neutral

        def func():
            if self.state == 'ON_FORWARD':
                self.on_forward()

            elif self.state == 'ON_RIGHT_TURN':
                self.on_right_turn()

            elif self.state == 'ON_LEFT_TURN':
                self.on_left_turn()

            elif self.state == 'ON_BACKWARD':
                self.on_backward()

            elif self.state == 'ON_STOP':
                self.on_stop()

            elif self.state == 'ON_NEWTRAL':
                self.on_neutral()

        self.exec = func

        while True:
            future = self.executor.submit(self.exec)
            result = future.result()
            # TODO : ここでエラーハンドリング

    def on_forward(self):
        print("前進")
        # TODO : 処理
        return True  # 成功したらTrue

    def on_backward(self):
        print("後進")
        # TODO : 処理

    def on_left_turn(self):
        print("左旋回")
        # TODO : 処理

    def on_right_turn(self):
        print("右旋回")
        # TODO : 処理

    def on_stop(self):
        print('ストップ')
        # TODO : 処理

    def on_neutral(self):
        print('ニュートラルポジション')
        # TODO : 処理


def control_tcp():
    # host = socket.gethostname()
    # ip = socket.gethostbyname(host) # 何故かlocalhost取ってくる...
    ip = '192.168.10.10'
    port = 55555
    connection = SupportSocketServer(ip, port)
    hexapod = Hexapod()

    try:
        while True:
            hexapod.exec()

            data = connection.recv_str()

            if data == 'QUIT':
                quit()

            hexapod.state = data

    finally:
        connection.close()


def test():
    hexapod = Hexapod()
    hexapod.state = 'ON_FORWARD'
    hexapod.exec()


if __name__ == '__main__':
    control_tcp()
