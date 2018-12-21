# coding=utf-8
from servo import *
from com_socket import *


class Hexapod(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        # self.servo = ServoPwmConfigData().get_MG92B()  # ここでサーボを選択
        # self.pwm = SupportServoDriver(config_data=self.servo)

        self.state = 'ON_NEWTRAL'

        def on_forward():
            print("前進")
            # TODO : 処理

        def on_backward():
            print("後進")
            # TODO : 処理

        def on_left_turn():
            print("左旋回")
            # TODO : 処理

        def on_right_turn():
            print("右旋回")
            # TODO : 処理

        def on_stop():
            print('ストップ')
            # TODO : 処理

        def on_neutral():
            print('ニュートラルポジション')
            # TODO : 処理

        self.forward = on_forward
        self.backward = on_backward
        self.left_turn = on_left_turn
        self.right_turn = on_right_turn
        self.stop = on_stop
        self.neutral = on_neutral

    def exec(self):
        if self.state == 'ON_FORWARD':
            self.executor.submit(self.forward)

        elif self.state == 'ON_RIGHT_TURN':
            self.executor.submit(self.right_turn)

        elif self.state == 'ON_LEFT_TURN':
            self.executor.submit(self.left_turn)

        elif self.state == 'ON_BACKWARD':
            self.executor.submit(self.backward)

        elif self.state == 'ON_STOP':
            self.executor.submit(self.stop)

        elif self.state == 'ON_NEWTRAL':
            self.executor.submit(self.neutral)


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
