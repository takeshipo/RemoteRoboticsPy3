# coding=utf-8

from pwm import *


def hexapod_forward():
    servo = PwmServoConfigData().get_MG92B()
    pwm = SupportServoDriver(config_data=servo)
    pwm.to_angle(0, 0)  # 第一引数がチャンネル、第二引数が角度


if __name__ == '__main__':
    hexapod_forward()
