from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# TODO:以下のグローバルの値はクラスを作成してそのフィールドにする
# KRS-2552RHV（サーボ）のデータシートより、
# PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec = 50Hzとする。
# パルス幅は 700μsec〜2300μsec が 0°〜270°に対応する。
pulse_period = 20000
max_micro_sec = 2300
min_micro_sec = 700
full_degree = 270  # 全角度


#  角度を受け取ってPCA9685に対応した値を算出する
def calcPulse(angle):
    # パルス幅よりDuty比を求める。
    min_duty = min_micro_sec / pulse_period
    max_duty = max_micro_sec / pulse_period

    # 全体に対して何％の角度か。例えば、フルが270°に対しての60°であれば22%。
    par_angle = (angle / full_degree)

    # 角度からDuty比を求める
    duty = ((max_duty - min_duty) * par_angle) + min_duty

    # PCA9685（サーボドライバ）は12bit扱うことができるのでDuty比を乗算して対応した値にする。
    pulse_value = duty * 4096

    return pulse_value


if __name__ == '__main__':
    pwm = Adafruit_PCA9685.PCA9685()  # ライブラリをインスタンス化
    pwm.set_pwm_freq(1000000 / pulse_period)  # 50HZ

    home_degree = 270 / 2  # 中心の角度
    home_pulse = calcPulse(home_degree)

    # 接続されているサーボすべてを中心位置（ホーム）にする
    for i in range(0, 15):
        pwm.set_pwm(i, 0, home_pulse)
