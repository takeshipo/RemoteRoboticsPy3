# coding=utf-8
from __future__ import division

import concurrent.futures
import dataclasses

import Adafruit_PCA9685


# サーボのPWM値のデータクラス
@dataclasses.dataclass
class ServoPwmConfigData:
    # ---デフォルト値は一般的に利用されやすい値が入っている。---
    # 値はすべてマイクロ秒で指定する

    # PWMの一周期。
    pulse_period: int = 20000

    # サーボの最大角（可動域）
    range_angle: int = 180

    # サーボの最大角に対応するパルス幅
    servo_max: int = 2000

    # サーボの最小角に対応するパルス幅
    servo_min: int = 1000


def get_SG90():
    return ServoPwmConfigData(20000, 180, 2000, 1000)


def get_SG92R():
    return ServoPwmConfigData(20000, 180, 2400, 500)


def get_MG92B():
    # FIXME: データシートが見つからないので正しい値が不明。要検証。
    return ServoPwmConfigData(20000, 365, 2000, 700)


def get_RS306MD():
    return ServoPwmConfigData(20000, 288, 2480, 560)


def get_KRS2552RHV():
    # KRS-2552RHVのデータシートより、
    # PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec(=50Hz)とする。
    return ServoPwmConfigData(20000, 270, 2300, 700)


# ライブラリの利用をサポートするクラス
class SupportServoDriver(object):

    def __init__(self, freq=20000, address=0x40):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.pwm = Adafruit_PCA9685.PCA9685(address)  # ライブラリ(PCA9685)をインスタンス化
        self.pwm.set_pwm_freq(1000000 / freq)  # デフォルトのままなら50HZ

    def to_angle(self, channel, config_data, angle):
        pulse_value = self.calc_pulse(angle, config_data)
        self.executor.submit(fn=self.pwm.set_pwm(channel, 0, pulse_value))

    # 角度を受け取ってPCA9685に対応した値を算出する
    def calc_pulse(self, angle, config_data):
        # パルス幅よりDuty比を求める。
        min_duty = config_data.servo_min / config_data.pulse_period
        max_duty = config_data.servo_max / config_data.pulse_period

        # 全体に対して何％の角度か求める。例えば、フルが180°に対しての60°であれば33%。
        # par_angle = (angle / self.range_angle)  # 中心を90°として角度を指定する場合
        par_angle = (angle / config_data.range_angle) + 0.5  # 中心を0°として角度を指定する場合

        # 角度からDuty比を求める
        duty = ((max_duty - min_duty) * par_angle) + min_duty

        # PCA9685（サーボドライバ）は12bit扱うことができるのでDuty比を乗算して対応した値にする。
        pulse_value = duty * 4096

        # 少数は切り捨て打て整数で返す
        return int(pulse_value)
