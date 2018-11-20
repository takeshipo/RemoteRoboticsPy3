# coding=utf-8
from __future__ import division

import Adafruit_PCA9685


# TODO: isRiversがTrueだったときの処理が記述されていない
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
