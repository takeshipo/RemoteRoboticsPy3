# coding=utf-8
from enum import IntEnum
from servo import *
import time

class State(IntEnum):
    ON_NEWTRAL = 199
    ON_FORWARD = 200
    ON_BACKWARD = 201
    ON_RIGHT_TURN = 202
    ON_LEFT_TURN = 203
    ON_STOP = 204


class Arm2axis:
    def __init__(self, pitch, roll):
        self.pitch_type = pitch["config_data"]
        self.pitch_channel = pitch["channel"]
        self.pitch_driver = pitch["driver"]

        self.roll_type = roll["config_data"]
        self.roll_channel = roll["channel"]
        self.roll_driver = roll["driver"]

    

    def set_pitch_angle(self, angle):
        self.set_pitch_angle(self.pitch_type, self.pitch_channel, angle)
        return self

    def set_roll_angle(self, angle):
        self.set_roll_angle(self.roll_type, self.roll_channel, angle)
        return self


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(address=0x40)

        self.arm1 = Arm2axis(
            pitch={"channel": 0, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm2 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm3 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm4 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm5 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

        self.arm6 = Arm2axis(
            pitch={"channel": 2, "driver": self.driver, "config_data": get_MG92B()},
            roll={"channel": 2, "driver": self.driver, "config_data": get_MG92B()})

  
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

        #--------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(45)
        self.arm4.set_roll_angle(-45)
        self.arm5.set_roll_angle(45)

        self.arm2.set_roll_angle(-45)
        self.arm3.set_roll_angle(45)
        self.arm6.set_roll_angle(-45)

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
        self.arm1.set_roll_angle(-45)
        self.arm4.set_roll_angle(45)
        self.arm5.set_roll_angle(-45)

        self.arm2.set_roll_angle(45)
        self.arm3.set_roll_angle(-45)
        self.arm6.set_roll_angle(45)

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

        #--------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(45)
        self.arm4.set_roll_angle(-45)
        self.arm5.set_roll_angle(45)

        self.arm2.set_roll_angle(-45)
        self.arm3.set_roll_angle(45)
        self.arm6.set_roll_angle(-45)

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
        self.arm1.set_roll_angle(-45)
        self.arm4.set_roll_angle(45)
        self.arm5.set_roll_angle(-45)

        self.arm2.set_roll_angle(45)
        self.arm3.set_roll_angle(-45)
        self.arm6.set_roll_angle(45)

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

        #--------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(45)
        self.arm4.set_roll_angle(45)
        self.arm5.set_roll_angle(45)

        self.arm2.set_roll_angle(-45)
        self.arm3.set_roll_angle(-45)
        self.arm6.set_roll_angle(-45)

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

        #--------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(-45)
        self.arm4.set_roll_angle(-45)
        self.arm5.set_roll_angle(-45)

        self.arm2.set_roll_angle(45)
        self.arm3.set_roll_angle(45)
        self.arm6.set_roll_angle(45)

        time.sleep(0.1)

    def on_left_turn(self):
        print("左旋回")
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

        #--------------------------------------
        # 2段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(-45)
        self.arm4.set_roll_angle(-45)
        self.arm5.set_roll_angle(-45)

        self.arm2.set_roll_angle(45)
        self.arm3.set_roll_angle(45)
        self.arm6.set_roll_angle(45)

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

        #--------------------------------------
        # 4段階動作
        # --------------------------------------
        self.arm1.set_roll_angle(45)
        self.arm4.set_roll_angle(45)
        self.arm5.set_roll_angle(45)

        self.arm2.set_roll_angle(-45)
        self.arm3.set_roll_angle(-45)
        self.arm6.set_roll_angle(-45)

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

        self.arm1.set_roll_angle(0)
        self.arm4.set_roll_angle(0)
        self.arm5.set_roll_angle(0)

        self.arm2.set_roll_angle(0)
        self.arm3.set_roll_angle(0)
        self.arm6.set_roll_angle(0)

        time.sleep(0.1)