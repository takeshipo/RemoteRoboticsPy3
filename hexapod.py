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

class Hexapod3axis(Robotics):

    def __init__(self):
        super().__init__()

        self.driver1 = SupportServoDriver(config_data=get_MG92B(), address=0x40)
        self.driver2 = SupportServoDriver(config_data=get_MG92B(), address=0x41)

    def on_forward(self):
        print("前進")
        # --------------------------------
        # 1段階目
        # --------------------------------
        self.driver1.to_angle(2, leftup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftup)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightn)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ---------------------------------
        # 2段階目
        # ---------------------------------
        self.driver1.to_angle(0, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, 30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, -5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, -5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, 5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, -5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

        # -------------------------------
        # 3段階目
        # -------------------------------
        self.driver1.to_angle(2, leftn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightup)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ------------------------------------
        # 4段階目
        # ------------------------------------
        self.driver1.to_angle(0, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, -30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, 5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, 5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, -5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, 5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

    def on_backward(self):
        print("後進")
        # ----------------------------------------
        # 1段階目
        # ----------------------------------------
        self.driver1.to_angle(2, leftup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftup)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightn)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ---------------------------------
        # 2段階目
        # ---------------------------------
        self.driver1.to_angle(0, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, -30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, 5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, 5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, -5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, 5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

        # -------------------------------
        # 3段階目
        # -------------------------------
        self.driver1.to_angle(2, leftn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightup)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ------------------------------------
        # 4段階目
        # ------------------------------------
        self.driver1.to_angle(0, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, 30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, -5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, -5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, 5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, -5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

    def on_left_turn(self):
        print("左旋回")
        # ----------------------------------------
        # 1段階目
        # ----------------------------------------
        self.driver1.to_angle(2, left_t_up)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, right_t_up)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, left_t_up)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightn)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ---------------------------------
        # 2段階目
        # ---------------------------------
        self.driver1.to_angle(0, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, 30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, 5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, 5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, 5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, 5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

        # -------------------------------
        # 3段階目
        # -------------------------------
        self.driver1.to_angle(2, leftn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver1.to_angle(2, right_t_up)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, left_t_up)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, right_t_up)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ------------------------------------
        # 4段階目
        # ------------------------------------
        self.driver1.to_angle(0, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, -30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, -5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, -5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, -5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, -5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)
    def on_right_turn(self):
        print("右旋回")
        # ----------------------------------------
        # 1段階目
        # ----------------------------------------
        self.driver1.to_angle(2, left_t_up)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, right_t_up)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, left_t_up)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, rightn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightn)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ------------------------------------
        # 2段階目
        # ------------------------------------
        self.driver1.to_angle(0, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, -30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, -5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, -30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, -5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, -5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, -5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, -30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, -5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)

        # -------------------------------
        # 3段階目
        # -------------------------------
        self.driver1.to_angle(2, leftn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(2, right_t_up)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, left_t_up)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, right_t_up)  # 左脚高さ初期値
        time.sleep(0.004)

        time.sleep(0.1)

        # ---------------------------------
        # 2段階目
        # ---------------------------------
        self.driver1.to_angle(0, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(3, 30)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, 5)  # 足の角度を前方向へ
        time.sleep(0.004)
        self.driver1.to_angle(6, 30)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, 5)  # 足の角度を前方向へ
        time.sleep(0.004)

        self.driver2.to_angle(0, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(1, 5)  # 右前脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(3, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(4, 5)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(6, 30)  # 右中脚を初期設定
        time.sleep(0.004)
        self.driver2.to_angle(7, 5)  # 右中脚を初期設定
        time.sleep(0.004)

        time.sleep(0.1)
    def on_stop(self):
        print('ストップ')

    def on_neutral(self):
        print('ニュートラルポジション')
        self.driver1.to_angle(2, leftn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, rightn)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, leftn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver1.to_angle(0, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(1, 0)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(3, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(4, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(6, 0)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver1.to_angle(7, 0)  # 右中脚を前に動かす
        time.sleep(0.004)

        self.driver2.to_angle(2, rightn)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftn)  # 右脚高さ初期値sudo
        time.sleep(0.004)
        self.driver2.to_angle(8, rightn)  # 左脚高さ初期値
        time.sleep(0.004)

        self.driver2.to_angle(0, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver2.to_angle(1, 0)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver2.to_angle(3, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver2.to_angle(4, 0)  # 右中脚を前に動かす
        time.sleep(0.004)
        self.driver2.to_angle(6, 0)  # 右前脚を前に動かす
        time.sleep(0.004)
        self.driver2.to_angle(7, 0)  # 右中脚を前に動かす
        time.sleep(0.004)

        time.sleep(0.1)


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(config_data=get_MG92B(), address=0x40)

    def on_forward(self):
        print("前進")
        # ---------------------------------------
        # ニュートラルポジション 0.05sec
        # ---------------------------------------
        '''
        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn) 
        time.sleep(0.004)
        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn) 
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        self.driver.to_angle(0, 30)
        time.sleep(0.004)
        self.driver.to_angle(6, 0) 
        time.sleep(0.004)
        self.driver.to_angle(8, -30)
        time.sleep(0.004)

        self.driver.to_angle(2, -30)
        time.sleep(0.004)
        self.driver.to_angle(4, 0)
        time.sleep(0.004)
        self.driver.to_angle(10, 30)
        time.sleep(0.004)

        time.sleep(0.05)
        '''
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.driver.to_angle(1, leftup)
        time.sleep(0.004)
        self.driver.to_angle(7, rightup)
        time.sleep(0.004)
        self.driver.to_angle(9, leftup)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.driver.to_angle(0, 45)
        time.sleep(0.004)
        self.driver.to_angle(6, -45)
        time.sleep(0.004)
        self.driver.to_angle(8, 45)
        time.sleep(0.004)

        self.driver.to_angle(2, 45)
        time.sleep(0.004)
        self.driver.to_angle(4, -45)
        time.sleep(0.004)
        self.driver.to_angle(10, 45)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, rightup)
        time.sleep(0.004)
        self.driver.to_angle(5, leftup)
        time.sleep(0.004)
        self.driver.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.driver.to_angle(0, -45)
        time.sleep(0.004)
        self.driver.to_angle(6, 45)
        time.sleep(0.004)
        self.driver.to_angle(8, -45)
        time.sleep(0.004)

        self.driver.to_angle(2, -45)
        time.sleep(0.004)
        self.driver.to_angle(4, 45)
        time.sleep(0.004)
        self.driver.to_angle(10, -45)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_backward(self):
        print("後進")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.driver.to_angle(1, leftup)
        time.sleep(0.004)
        self.driver.to_angle(7, rightup)
        time.sleep(0.004)
        self.driver.to_angle(9, leftup)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.driver.to_angle(0, -45)
        time.sleep(0.004)
        self.driver.to_angle(6, 45)
        time.sleep(0.004)
        self.driver.to_angle(8, -45)
        time.sleep(0.004)

        self.driver.to_angle(2, -45)
        time.sleep(0.004)
        self.driver.to_angle(4, 45)
        time.sleep(0.004)
        self.driver.to_angle(10, -45)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, rightup)
        time.sleep(0.004)
        self.driver.to_angle(5, leftup)
        time.sleep(0.004)
        self.driver.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.driver.to_angle(0, 45)
        time.sleep(0.004)
        self.driver.to_angle(6, -45)
        time.sleep(0.004)
        self.driver.to_angle(8, 45)
        time.sleep(0.004)

        self.driver.to_angle(2, 45)
        time.sleep(0.004)
        self.driver.to_angle(4, -45)
        time.sleep(0.004)
        self.driver.to_angle(10, 45)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_right_turn(self):
        print("右旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.driver.to_angle(1, left_t_up)
        time.sleep(0.004)
        self.driver.to_angle(7, right_t_up)
        time.sleep(0.004)
        self.driver.to_angle(9, left_t_up)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.driver.to_angle(0, 45)
        time.sleep(0.004)
        self.driver.to_angle(6, 45)
        time.sleep(0.004)
        self.driver.to_angle(8, 45)
        time.sleep(0.004)

        self.driver.to_angle(2, -45)
        time.sleep(0.004)
        self.driver.to_angle(4, -45)
        time.sleep(0.004)
        self.driver.to_angle(10, -45)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, right_t_up)
        time.sleep(0.004)
        self.driver.to_angle(5, left_t_up)
        time.sleep(0.004)
        self.driver.to_angle(11, right_t_up)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.driver.to_angle(0, -45)
        time.sleep(0.004)
        self.driver.to_angle(6, -45)
        time.sleep(0.004)
        self.driver.to_angle(8, -45)
        time.sleep(0.004)

        self.driver.to_angle(2, 45)
        time.sleep(0.004)
        self.driver.to_angle(4, 45)
        time.sleep(0.004)
        self.driver.to_angle(10, 45)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_left_turn(self):
        print("右旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.driver.to_angle(1, left_t_up)
        time.sleep(0.004)
        self.driver.to_angle(7, right_t_up)
        time.sleep(0.004)
        self.driver.to_angle(9, left_t_up)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.driver.to_angle(0, -45)
        time.sleep(0.004)
        self.driver.to_angle(6, -45)
        time.sleep(0.004)
        self.driver.to_angle(8, -45)
        time.sleep(0.004)

        self.driver.to_angle(2, 45)
        time.sleep(0.004)
        self.driver.to_angle(4, 45)
        time.sleep(0.004)
        self.driver.to_angle(10, 45)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, right_t_up)
        time.sleep(0.004)
        self.driver.to_angle(5, left_t_up)
        time.sleep(0.004)
        self.driver.to_angle(11, right_t_up)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.driver.to_angle(0, 45)
        time.sleep(0.004)
        self.driver.to_angle(6, 45)
        time.sleep(0.004)
        self.driver.to_angle(8, 45)
        time.sleep(0.004)

        self.driver.to_angle(2, -45)
        time.sleep(0.004)
        self.driver.to_angle(4, -45)
        time.sleep(0.004)
        self.driver.to_angle(10, -45)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_stop(self):
        print('ストップ')
        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        self.driver.to_angle(0, 0)
        time.sleep(0.004)
        self.driver.to_angle(6, 0)
        time.sleep(0.004)
        self.driver.to_angle(8, 0)
        time.sleep(0.004)

        self.driver.to_angle(2, 0)
        time.sleep(0.004)
        self.driver.to_angle(4, 0)
        time.sleep(0.004)
        self.driver.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.2)

    def on_neutral(self):
        print('ニュートラルポジション')
        self.driver.to_angle(1, leftn)
        time.sleep(0.004)
        self.driver.to_angle(7, rightn)
        time.sleep(0.004)
        self.driver.to_angle(9, leftn)
        time.sleep(0.004)

        self.driver.to_angle(3, rightn)
        time.sleep(0.004)
        self.driver.to_angle(5, leftn)
        time.sleep(0.004)
        self.driver.to_angle(11, rightn)
        time.sleep(0.004)

        self.driver.to_angle(0, 0)
        time.sleep(0.004)
        self.driver.to_angle(6, 0)
        time.sleep(0.004)
        self.driver.to_angle(8, 0)
        time.sleep(0.004)

        self.driver.to_angle(2, 0)
        time.sleep(0.004)
        self.driver.to_angle(4, 0)
        time.sleep(0.004)
        self.driver.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.2)
