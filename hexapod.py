# coding=utf-8
from servo import *


# 前進
def hexapod_forward():
    servo = ServoPwmConfigData().get_MG92B()  # ここでサーボを選択
    pwm = SupportServoDriver(config_data=servo)

    # 第一引数がチャンネル、第二引数が角度
    pwm.to_angle(0, 0)
    pwm.to_angle(1, 0)
