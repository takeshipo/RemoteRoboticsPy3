# coding=utf-8
from enum import IntEnum
from servo import *
from robotics import Robotics


class Hexapod3axis(Robotics):

    def __init__(self):
        super().__init__()

        self.driver1 = SupportServoDriver(config_data=get_MG92B(), address=0x40)
        self.driver2 = SupportServoDriver(config_data=get_MG92B(), address=0x40)

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


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(config_data=get_MG92B(), address=0x40)

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
