# coding=utf-8
from __future__ import division

import Adafruit_PCA9685


# ライブラリの利用をサポートするクラス
class SupportServoDriver(object):

    def __init__(self, config_data, address=0x40):
        self.config_data = config_data
        self.pwm = Adafruit_PCA9685.PCA9685(address)  # ライブラリ(PCA9685)をインスタンス化
        self.pwm.set_pwm_freq(1000000 / self.config_data.pulse_period)  # デフォルトのままなら50HZ

    def to_angle(self, channel, angle):
        pulse_value = self.calc_pulse(angle)
        self.pwm.set_pwm(channel, 0, pulse_value)

    # 角度を受け取ってPCA9685に対応した値を算出する
    def calc_pulse(self, angle):
        # パルス幅よりDuty比を求める。
        min_duty = self.config_data.servo_min / self.config_data.pulse_period
        max_duty = self.config_data.servo_max / self.config_data.pulse_period

        # 全体に対して何％の角度か求める。例えば、フルが180°に対しての60°であれば33%。
        # par_angle = (angle / self.range_angle)  # 中心を90°として角度を指定する場合
        par_angle = (angle / self.config_data.range_angle) + 0.5  # 中心を0°として角度を指定する場合

        # 角度からDuty比を求める
        duty = ((max_duty - min_duty) * par_angle) + min_duty

        # PCA9685（サーボドライバ）は12bit扱うことができるのでDuty比を乗算して対応した値にする。
        pulse_value = duty * 4096

        # 少数は切り捨て打て整数で返す
        return int(pulse_value)


# TODO : きれいなDataClassにする。要リファクタリング。
class ServoPwmConfigData:

    def __init__(self):
        # ---デフォルト値は一般的に利用されやすい値が入っている。---
        # 値はすべてマイクロ秒で指定する

        # サーボの最大角
        self.range_angle = None

        # PWMの一周期。
        self.pulse_period = None

        # サーボの最大角に対応するパルス幅
        self.servo_max = None

        # サーボの最小角に対応するパルス幅
        self.servo_min = None

    def get_SG92R(self):
        # FIXME: データシートが見つからないので正しい値が不明。要検証。
        self.range_angle = 180  # 可動域（角度）
        self.pulse_period = 20000
        self.servo_max = 2000
        self.servo_min = 700
        return self

    def get_MG92B(self):
        # FIXME: データシートが見つからないので正しい値が不明。要検証。
        self.range_angle = 365  # 可動域（角度）
        self.pulse_period = 20000
        self.servo_max = 2000
        self.servo_min = 700
        return self

    def get_RS306MD(self):
        self.range_angle = 288  # 可動域（角度）
        self.pulse_period = 20000
        self.servo_max = 2480
        self.servo_min = 560
        return self

    def get_KRS2552RHV(self):
        # KRS-2552RHVのデータシートより、
        # PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec(=50Hz)とする。
        # パルス幅は 700μsec〜2300μsec が 0°〜270°に対応する。
        self.pulse_period = 20000
        self.servo_max = 2300
        self.servo_min = 700
        self.range_angle = 270  # 可動域（角度）
        return self
