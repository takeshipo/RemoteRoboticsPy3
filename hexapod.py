# coding=utf-8
from com_socket import *
from enum import IntEnum


class Hexapod(object):
    class State(IntEnum):
        ON_NEWTRAL = 199
        ON_FORWARD = 200
        ON_BACKWARD = 201
        ON_RIGHT_TURN = 202
        ON_LEFT_TURN = 203
        ON_STOP = 204

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        # self.servo = ServoPwmConfigData().get_MG92B()  # ここでサーボを選択
        # self.pwm = SupportServoDriver(config_data=self.servo)

        self.mState = Hexapod.State.ON_NEWTRAL

    # TODO : STOPやNEWTRALは繰り返されないようにしたい
    def start_control(self):
        if self.mState == Hexapod.State.ON_FORWARD:
            self.on_forward()

        elif self.mState == Hexapod.State.ON_RIGHT_TURN:
            self.on_right_turn()

        elif self.mState == Hexapod.State.ON_LEFT_TURN:
            self.on_left_turn()

        elif self.mState == Hexapod.State.ON_BACKWARD:
            self.on_backward()

        elif self.mState == Hexapod.State.ON_STOP:
            self.on_stop()

        elif self.mState == Hexapod.State.ON_NEWTRAL:
            self.on_neutral()

        self.executor.submit(fn=self.start_control)

    def on_forward(self):
        print("前進")
        # TODO : 処理

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
    CMD_QUIT = 999

    connection = SupportSocketServer(ip, port)

    hexapod = Hexapod()
    hexapod.on_neutral()
    hexapod.start_control()

    try:
        while True:

            data = int.from_bytes(connection.recv_raw(), 'big')

            if data == CMD_QUIT:
                quit()

            hexapod.mState = data

    finally:
        connection.close()


def test():
    hexapod = Hexapod()
    hexapod.on_forward()


if __name__ == '__main__':
    control_tcp()
