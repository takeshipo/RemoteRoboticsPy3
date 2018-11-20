# coding=utf-8

from servo import *
from pwm import *


def hexapod_forward():
    servo = PwmServoConfigData().get_MG92B()
    pwm = SupportServoDriver(config_data=servo)


if __name__ == '__main__':
    hexapod_forward()
