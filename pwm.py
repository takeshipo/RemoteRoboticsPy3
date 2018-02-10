# coding=utf-8
from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685


# TODO: isRiversがTrueだったときの処理が記述されていない
# ライブラリの利用をサポートするクラス
class SupportServoDriver(object):
    # 引数の時間の値はすべてマイクロ秒で指定する
    # range_angle: サーボの最大角
    # pulse_period: PWMの一周期。
    # servo_max: サーボの最大角に対応するパルス幅
    # servo_min: サーボの最小角に対応するパルス幅
    # is_rivers: SG92Rのようにサーボの値が逆転するものはtrueに
    # ---デフォルト値は一般的に利用されやすい値が入っている。---
    def __init__(self, range_angle=180, pulse_period=20000, servo_max=2000, servo_min=700, is_rivers=False):
        self.range_angle = range_angle
        self.pulse_period = pulse_period
        self.servo_max = servo_max
        self.servo_min = servo_min
        self.isRivers = is_rivers
        # HACK:↓このインスタンス保持する必要ある？
        self.pwm = None  # get_instanceで生成されるPCA9685インスタンスを用意

    def get_instance(self):
        self.pwm = Adafruit_PCA9685.PCA9685()  # ライブラリ(PCA9685)をインスタンス化
        self.pwm.set_pwm_freq(1000000 / self.pulse_period)  # デフォルトのままなら50HZ
        return self.pwm

    # 角度を受け取ってPCA9685に対応した値を算出する
    def calc_pulse(self, angle):
        # パルス幅よりDuty比を求める。
        min_duty = self.servo_min / self.pulse_period
        max_duty = self.servo_max / self.pulse_period

        # 全体に対して何％の角度か。例えば、フルが180°に対しての60°であれば33%。
        # par_angle = (angle / self.range_angle)  # 中心を90°として角度を指定する場合
        par_angle = ((angle + self.range_angle / 2) / self.range_angle)  # 中心を0°として角度を指定する場合
        # print(angle + self.range_angle / 2)

        # 角度からDuty比を求める
        duty = ((max_duty - min_duty) * par_angle) + min_duty

        # PCA9685（サーボドライバ）は12bit扱うことができるのでDuty比を乗算して対応した値にする。
        pulse_value = duty * 4096

        # 少数は切り捨て打て整数で返すs
        return int(pulse_value)
