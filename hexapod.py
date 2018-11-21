
from servo import *

def hexapod_forward():
    servo = ServoPwmConfigData().get_MG92B()
    pwm = SupportServoDriver(config_data=servo)
    pwm.to_angle(0, 0)  # 第一引数がチャンネル、第二引数が角度
