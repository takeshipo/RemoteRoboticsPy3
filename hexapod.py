# coding=utf-8
from enum import IntEnum
from servo import *


class State(IntEnum):
    ON_NEWTRAL = 199
    ON_FORWARD = 200
    ON_BACKWARD = 201
    ON_RIGHT_TURN = 202
    ON_LEFT_TURN = 203
    ON_STOP = 204


class Hexapod3axis(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.driver1 = SupportServoDriver(config_data=get_MG92B(), address=0x40)
        self.driver2 = SupportServoDriver(config_data=get_MG92B(), address=0x40)

        self.mState = State.ON_NEWTRAL

    # TODO : STOPやNEWTRALは繰り返されないようにしたい
    def start_control(self):
        if self.mState == State.ON_FORWARD:
            self.on_forward()

        elif self.mState == State.ON_RIGHT_TURN:
            self.on_right_turn()

        elif self.mState == State.ON_LEFT_TURN:
            self.on_left_turn()

        elif self.mState == State.ON_BACKWARD:
            self.on_backward()

        elif self.mState == State.ON_STOP:
            self.on_stop()

        elif self.mState == State.ON_NEWTRAL:
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


class Hexapod2axis(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.pwm = SupportServoDriver(config_data=get_MG92B(), address=0x40)

        self.mState = State.ON_NEWTRAL

    # TODO : STOPやNEWTRALは繰り返されないようにしたい
    def start_control(self):
        if self.mState == State.ON_FORWARD:
            self.on_forward()

        elif self.mState == State.ON_RIGHT_TURN:
            self.on_right_turn()

        elif self.mState == State.ON_LEFT_TURN:
            self.on_left_turn()

        elif self.mState == State.ON_BACKWARD:
            self.on_backward()

        elif self.mState == State.ON_STOP:
            self.on_stop()

        elif self.mState == State.ON_NEWTRAL:
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
