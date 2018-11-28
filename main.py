# coding=utf-8
from hexapod import *
from tests import *
from servo import *

if __name__ == '__main__':
    pwm_driver_test(ServoPwmConfigData().get_SG90())
