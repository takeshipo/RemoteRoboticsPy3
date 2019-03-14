# coding=utf-8
from enum import IntEnum
from servo import *
import time
from robotics import Robotics


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

    # def set_yaw_angle(self, angle, speed):
    #     self.yaw_driver.to_angle(self.yaw_type, self.yaw_channel, angle, speed)
    #     return self
    #
    # def set_pitch_angle(self, angle, speed):
    #     self.pitch_driver.to_angle(self.pitch_type, self.pitch_channel, angle, speed)
    #     return self


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(address=0x40)

        self.arm1 = Arm2axis(
            pitch={"channel": 1, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 0, "driver": self.driver, "config_data": get_MG92B()})

        self.arm2 = Arm2axis(
            pitch={"channel": 3, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm3 = Arm2axis(
            pitch={"channel": 5, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 4,"driver": self.driver, "config_data": get_MG92B()})

        self.arm4 = Arm2axis(
            pitch={"channel": 7, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 6, "driver": self.driver, "config_data": get_MG92B()})

        self.arm5 = Arm2axis(
            pitch={"channel": 9, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 8, "driver": self.driver, "config_data": get_MG92B()})

        self.arm6 = Arm2axis(
            pitch={"channel": 11, "driver": self.driver, "config_data": get_MG92B()},
            yaw={"channel": 10, "driver": self.driver, "config_data": get_MG92B()})

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

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(45)

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

        self.arm2.set_yaw_angle(-45)
        self.arm3.set_yaw_angle(45)
        self.arm6.set_yaw_angle(-45)

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
        self.arm1.set_yaw_angle(-45)
        self.arm4.set_yaw_angle(45)
        self.arm5.set_yaw_angle(-45)

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
        self.arm1.set_yaw_angle(45)
        self.arm4.set_yaw_angle(-45)
        self.arm5.set_yaw_angle(45)

        self.arm2.set_yaw_angle(45)
        self.arm3.set_yaw_angle(-45)
        self.arm6.set_yaw_angle(45)

        time.sleep(0.1)

    def on_left_turn(self):
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

    def move_test(self):
        print("テスト前進")

        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.arm1.set_pitch_angle(40, 1)
        self.arm4.set_pitch_angle(40, 1)
        self.arm5.set_pitch_angle(40, 1)

        self.arm2.set_pitch_angle(-30, 1)
        self.arm3.set_pitch_angle(-30, 1)
        self.arm6.set_pitch_angle(-30, 1)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(45, 1)
        self.arm4.set_yaw_angle(-45, 1)
        self.arm5.set_yaw_angle(45, 1)

        self.arm2.set_yaw_angle(-45, 1)
        self.arm3.set_yaw_angle(45, 1)
        self.arm6.set_yaw_angle(-45, 1)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------
        self.arm1.set_pitch_angle(-30, 1)
        self.arm4.set_pitch_angle(-30, 1)
        self.arm5.set_pitch_angle(-30, 1)

        self.arm2.set_pitch_angle(40, 1)
        self.arm3.set_pitch_angle(40, 1)
        self.arm6.set_pitch_angle(40, 1)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_yaw_angle(-45, 1)
        self.arm4.set_yaw_angle(45, 1)
        self.arm5.set_yaw_angle(-45, 1)

        self.arm2.set_yaw_angle(45, 1)
        self.arm3.set_yaw_angle(-45, 1)
        self.arm6.set_yaw_angle(45, 1)

        time.sleep(0.1)

    def move_set(self):
        print("テスト前進")

        self.arm4.set_yaw_angle(0, 1)
        self.arm5.set_yaw_angle(0, 1)

        self.arm2.set_yaw_angle(0, 1)
        self.arm3.set_yaw_angle(0, 1)
        self.arm6.set_yaw_angle(0, 1)
