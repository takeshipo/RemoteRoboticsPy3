# coding=utf-8
from servo import *


class Hexapod(object):

    def __init__(self):
        self.servo = ServoPwmConfigData().get_MG92B()  # ここでサーボを選択
        self.pwm = SupportServoDriver(config_data=self.servo)

    def on_foward(self):
        print("前進")

    def on_bacnkward(self):
        print("後進")

    def on_left_turn(self):
        print("前進")

    def on_right_turn(self):
        print("前進")
