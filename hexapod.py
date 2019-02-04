# coding=utf-8
from enum import IntEnum
from servo import *
import time

# 角度変数
# 左足の動作
leftn = 0  # 左足の高さ初期値
leftup = 60  # 左脚の上げる高さ
# 右足の動作
rightn = 0  # 右脚高さの初期値
rightup =60   # 右脚の上げる高さ


class State(IntEnum):
    ON_NEWTRAL = 199
    ON_FORWARD = 200
    ON_BACKWARD = 201
    ON_RIGHT_TURN = 202
    ON_LEFT_TURN = 203
    ON_STOP = 204


class Hexapod3axis(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.driver1 = SupportServoDriver(config_data=get_MG92B(), address=0x40)
        self.driver2 = SupportServoDriver(config_data=get_MG92B(), address=0x41)

        self.mState = State.ON_NEWTRAL

    # TODO : STOPやNEWTRALは繰り返されないようにしたい
    def start_control(self):
        if self.mState == State.ON_FORWARD:
            self.on_forward()

        elif self.mState == State.ON_RIGHT_TURN:
            self.on_right_turn()

        elif self.mState == State.ON_LEFT_TURN:
            self.on_left_turn()

        elif self.mState == State.ON_BACKWARD:
            self.on_backward()

        elif self.mState == State.ON_STOP:
            self.on_stop()

        elif self.mState == State.ON_NEWTRAL:
            self.on_neutral()

        self.executor.submit(fn=self.start_control)

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

        self.driver1.to_angle(2, rightup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(5, leftup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver1.to_angle(8, rightup)  # 左脚高さ初期値
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

        self.driver2.to_angle(2, rightup)  # 左脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(5, leftup)  # 右脚高さ初期値
        time.sleep(0.004)
        self.driver2.to_angle(8, rightup)  # 左脚高さ初期値
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
        # TODO : 処理

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


class Hexapod2axis(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.pwm = SupportServoDriver(config_data=get_MG92B(), address=0x40)

        self.mState = State.ON_NEWTRAL

    # TODO : STOPやNEWTRALは繰り返されないようにしたい
    def start_control(self):
        if self.mState == State.ON_FORWARD:
            self.on_forward()

        elif self.mState == State.ON_RIGHT_TURN:
            self.on_right_turn()

        elif self.mState == State.ON_LEFT_TURN:
            self.on_left_turn()

        elif self.mState == State.ON_BACKWARD:
            self.on_backward()

        elif self.mState == State.ON_STOP:
            self.on_stop()

        elif self.mState == State.ON_NEWTRAL:
            self.on_neutral()

        self.executor.submit(fn=self.start_control)

    def on_forward(self):
        print("前進")
        # ---------------------------------------
        # ニュートラルポジション 0.05sec
        # ---------------------------------------
        '''
        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftn) 
        time.sleep(0.004)
        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn) 
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        self.pwm.to_angle(0, 30)
        time.sleep(0.004)
        self.pwm.to_angle(6, 0) 
        time.sleep(0.004)
        self.pwm.to_angle(8, -30)
        time.sleep(0.004)

        self.pwm.to_angle(2, -30)
        time.sleep(0.004)
        self.pwm.to_angle(4, 0)
        time.sleep(0.004)
        self.pwm.to_angle(10, 30)
        time.sleep(0.004)

        time.sleep(0.05)
        '''
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.pwm.to_angle(1, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftup)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.pwm.to_angle(0, 60)
        time.sleep(0.004)
        self.pwm.to_angle(6, -30)
        time.sleep(0.004)
        self.pwm.to_angle(8, 0)
        time.sleep(0.004)

        self.pwm.to_angle(2, 0)
        time.sleep(0.004)
        self.pwm.to_angle(4, -30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 60)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftn)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.pwm.to_angle(0, 0)
        time.sleep(0.004)
        self.pwm.to_angle(6, 30)
        time.sleep(0.004)
        self.pwm.to_angle(8, -60)
        time.sleep(0.004)

        self.pwm.to_angle(2, -60)
        time.sleep(0.004)
        self.pwm.to_angle(4, 30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_backward(self):
        print("後進")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.pwm.to_angle(1, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftup)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.pwm.to_angle(0, 0)
        time.sleep(0.004)
        self.pwm.to_angle(6, 30)
        time.sleep(0.004)
        self.pwm.to_angle(8, -60)
        time.sleep(0.004)

        self.pwm.to_angle(2, -60)
        time.sleep(0.004)
        self.pwm.to_angle(4, 30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftn)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.pwm.to_angle(0, 60)
        time.sleep(0.004)
        self.pwm.to_angle(6, -30)
        time.sleep(0.004)
        self.pwm.to_angle(8, 0)
        time.sleep(0.004)

        self.pwm.to_angle(2, 0)
        time.sleep(0.004)
        self.pwm.to_angle(4, -30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 60)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_left_turn(self):
        print("左旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.pwm.to_angle(1, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftup)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------

        self.pwm.to_angle(0, 0)
        time.sleep(0.004)
        self.pwm.to_angle(6, -30)
        time.sleep(0.004)
        self.pwm.to_angle(8, -60)
        time.sleep(0.004)

        self.pwm.to_angle(2, 60)
        time.sleep(0.004)
        self.pwm.to_angle(4, 30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftn)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.pwm.to_angle(0, 60)
        time.sleep(0.004)
        self.pwm.to_angle(6, 30)
        time.sleep(0.004)
        self.pwm.to_angle(8, 0)
        time.sleep(0.004)

        self.pwm.to_angle(2, 0)
        time.sleep(0.004)
        self.pwm.to_angle(4, -30)
        time.sleep(0.004)
        self.pwm.to_angle(10, -60)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_right_turn(self):
        print("右旋回")
        # ---------------------------------------
        # 1段階動作
        # ---------------------------------------
        self.pwm.to_angle(1, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftup)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 2段階動作
        # --------------------------------------
        self.pwm.to_angle(0, 60)
        time.sleep(0.004)
        self.pwm.to_angle(6, 30)
        time.sleep(0.004)
        self.pwm.to_angle(8, 0)
        time.sleep(0.004)

        self.pwm.to_angle(2, 0)
        time.sleep(0.004)
        self.pwm.to_angle(4, -30)
        time.sleep(0.004)
        self.pwm.to_angle(10, -60)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 3段階動作
        # --------------------------------------

        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(7, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(9, leftn)
        time.sleep(0.004)

        self.pwm.to_angle(3, rightup)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftup)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightup)
        time.sleep(0.004)

        time.sleep(0.1)

        # --------------------------------------
        # 4段階動作
        # --------------------------------------
        self.pwm.to_angle(0, 0)
        time.sleep(0.004)
        self.pwm.to_angle(6, -30)
        time.sleep(0.004)
        self.pwm.to_angle(8, -60)
        time.sleep(0.004)

        self.pwm.to_angle(2, 60)
        time.sleep(0.004)
        self.pwm.to_angle(4, 30)
        time.sleep(0.004)
        self.pwm.to_angle(10, 0)
        time.sleep(0.004)

        time.sleep(0.1)

    def on_stop(self):
        print('ストップ')
        # TODO : 処理

    def on_neutral(self):
        print('ニュートラルポジション')
        # self.pwm.to_angle(1, leftn)
        # time.sleep(0.004)
        # self.pwm.to_angle(7, rightn)
        # time.sleep(0.004)
        # self.pwm.to_angle(9, leftn)
        # time.sleep(0.004)

        self.pwm.to_angle(2, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(5, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(8, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(0, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(1, leftn)
        time.sleep(0.004)

        '''
        self.pwm.to_angle(3, rightn)
        time.sleep(0.004)
        self.pwm.to_angle(5, leftn)
        time.sleep(0.004)
        self.pwm.to_angle(11, rightn)
        time.sleep(0.004)

        self.pwm.to_angle(0, 30)
        time.sleep(0.004)
        self.pwm.to_angle(6, 0)
        time.sleep(0.004)
        self.pwm.to_angle(8, -30)
        time.sleep(0.004)

        self.pwm.to_angle(2, -30)
        time.sleep(0.004)
        self.pwm.to_angle(4, 0)
        time.sleep(0.004)
        self.pwm.to_angle(10, 30)
        time.sleep(0.004)

        time.sleep(0.2)
        '''
