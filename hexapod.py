# coding=utf-8
from enum import IntEnum
from servo import *
import time
from robotics import Robotics

#角度変数
#左足の動作
leftn=90   #左足の高さ初期値
leftup=-60 #左脚の上げる高さ
#右足の動作
rightn=-90 #右脚高さの初期値
rightup=60 #右脚の上げる高さ

class Hexapod3axis(Robotics):

    def __init__(self):
        super().__init__()

        self.driver1 = SupportServoDriver(config_data=get_MG92B(), address=0x40)
        self.driver2 = SupportServoDriver(config_data=get_MG92B(), address=0x41)

    def on_forward(self):
        print("前進")

    def on_backward(self):
        print("後進")  

    def on_left_turn(self):
        print("左旋回")
   
    def on_right_turn(self):
        print("右旋回")
   
    def on_stop(self):
        print('ストップ')

    def on_neutral(self):
        print('ニュートラルポジション')


class Hexapod2axis(Robotics):

    def __init__(self):
        super().__init__()
        self.driver = SupportServoDriver(config_data=get_MG92B(), address=0x40)

    def on_forward(self):
        print("前進")
        #---------------------------------------
        # ニュートラルポジション 0.05sec
        #---------------------------------------
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
        #---------------------------------------
        # 1段階動作
        #---------------------------------------
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
        
        #--------------------------------------
        # 2段階動作
        #--------------------------------------

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

        #--------------------------------------
        # 3段階動作
        #--------------------------------------

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
                
        #--------------------------------------
        # 4段階動作
        #--------------------------------------
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
        #---------------------------------------
        # 1段階動作
        #---------------------------------------
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
        
        #--------------------------------------
        # 2段階動作
        #--------------------------------------

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

        #--------------------------------------
        # 3段階動作
        #--------------------------------------

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
                
        #--------------------------------------
        # 4段階動作
        #--------------------------------------
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
        #---------------------------------------
        # 1段階動作
        #---------------------------------------
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
        
        #--------------------------------------
        # 2段階動作
        #--------------------------------------

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

        #--------------------------------------
        # 3段階動作
        #--------------------------------------

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
                
        #--------------------------------------
        # 4段階動作
        #--------------------------------------
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
                #---------------------------------------
        # 1段階動作
        #---------------------------------------
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
        
        #--------------------------------------
        # 2段階動作
        #--------------------------------------
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
 
        #--------------------------------------
        # 3段階動作
        #--------------------------------------

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
                
        #--------------------------------------
        # 4段階動作
        #--------------------------------------
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

        time.sleep(0.2)
