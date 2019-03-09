# coding=utf-8
from enum import IntEnum
from servo import *
import time
from robotics import Robotics

# 角度変数
# 左足の動作
leftn = -30  # 左足の高さ初期値
leftup = 40  # 左脚の上げる高さ
left_t_up = 80
# 右足の動作
rightn = -30  # 右脚高さの初期値
rightup = 40  # 右脚の上げる高さ
right_t_up = 80


class Arm2axis:
    def __init__(self, yaw, pitch):
        self.yaw_type = yaw["config_data"]
        self.yaw_channel = yaw["channel"]
        self.yaw_driver = yaw["driver"]

        self.pitch_type = pitch["config_data"]
        self.pitch_channel = pitch["channel"]
        self.pitch_driver = pitch["driver"]

    def set_yaw_angle(self, angle):
        self.yaw_driver.to_angle(self.yaw_type, self.yaw_channel, angle)
        return self

    def set_pitch_angle(self, angle):
        self.pitch_driver.to_angle(self.pitch_type, self.pitch_channel, angle)
        return self


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(address=0x40)

        self.arm1 = Arm2axis(
            pitch={"channel": 0, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm2 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm3 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm4 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm5 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm6 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

    def on_forward(self):
        print("前進")

        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(40)
        self.arm4.set_pitch_angle(40)
        self.arm5.set_pitch_angle(40)

        self.arm2.set_pitch_angle(-30)
        self.arm3.set_pitch_angle(-30)
        self.arm6.set_pitch_angle(-30)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(45)
        self.arm4.set_yaw_angle(-45)
        self.arm5.set_yaw_angle(45)

        self.arm2.set_yaw_angle(-45)
        self.arm3.set_yaw_angle(45)
        self.arm6.set_yaw_angle(-45)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(-45)
        self.arm4.set_yaw_angle(45)
        self.arm5.set_yaw_angle(-45)

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(45)

        time.sleep(0.1)

    def on_backward(self):
        print("後進")

        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(45)
        self.arm4.set_yaw_angle(-45)
        self.arm5.set_yaw_angle(45)

        self.arm2.set_yaw_angle(-45)
        self.arm3.set_yaw_angle(45)
        self.arm6.set_yaw_angle(-45)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------
        self.arm1.set_pitch_angle(40)
        self.arm4.set_pitch_angle(40)
        self.arm5.set_pitch_angle(40)

        self.arm2.set_pitch_angle(-30)
        self.arm3.set_pitch_angle(-30)
        self.arm6.set_pitch_angle(-30)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(-45)
        self.arm4.set_yaw_angle(45)
        self.arm5.set_yaw_angle(-45)

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(45)

        time.sleep(0.1)

    def on_right_turn(self):
        print("右旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------

    def on_right_turn(self):
        print("右旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(-45)
        self.arm4.set_yaw_angle(-45)
        self.arm5.set_yaw_angle(-45)

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(45)
        self.arm6.set_yaw_angle(45)

        time.sleep(0.1)

        # ---------------------------------------
        # 3段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(45)
        self.arm4.set_yaw_angle(45)
        self.arm5.set_yaw_angle(45)

        self.arm2.set_yaw_angle(-45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(-45)

        time.sleep(0.1)
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(45)
        self.arm4.set_yaw_angle(45)
        self.arm5.set_yaw_angle(45)

        self.arm2.set_yaw_angle(-45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(-45)

        time.sleep(0.1)

        # ---------------------------------------
        # 3段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(40)
        self.arm3.set_pitch_angle(40)
        self.arm6.set_pitch_angle(40)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(-45)
        self.arm4.set_yaw_angle(-45)
        self.arm5.set_yaw_angle(-45)

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(45)
        self.arm6.set_yaw_angle(45)

        time.sleep(0.1)

    def on_stop(self):
        print('ストップ')

    def on_neutral(self):
        print('ニュートラルポジション')
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(-30)
        self.arm4.set_pitch_angle(-30)
        self.arm5.set_pitch_angle(-30)

        self.arm2.set_pitch_angle(-30)
        self.arm3.set_pitch_angle(-30)
        self.arm6.set_pitch_angle(-30)

        self.arm1.set_yaw_angle(0)
        self.arm4.set_yaw_angle(0)
        self.arm5.set_yaw_angle(0)

        self.arm2.set_yaw_angle(0)
        self.arm3.set_yaw_angle(0)
        self.arm6.set_yaw_angle(0)

        time.sleep(0.1)
