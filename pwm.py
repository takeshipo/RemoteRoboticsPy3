from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685


# TODO: isRiversがTrueだったときの処理が記述されていない
# ライブラリの利用をサポートするクラス
class support_servo_driver(object):
    # デフォルト値は一般的に利用されやすい値が入っている。
    # 引数に指定する時間の値はすべてマイクロ秒にしてください。
    def __init__(self, range_angle=180, pulse_period=20000, servo_max=2000, servo_min=700, isRivers=False):
        self.range_angle = range_angle  # 回転することができる角度
        self.pulse_period = pulse_period  # 一周期分のパルス幅
        self.servo_max = servo_max  # サーボの最大角に対応するパルス幅
        self.servo_min = servo_min  # サーボの最小角に対応するパルス幅
        self.isRivers = isRivers  # SG90のように逆回転するものはこれをTrueにする

    def get_instance(self):
        pwm = Adafruit_PCA9685.PCA9685()  # ライブラリをインスタンス化
        pwm.set_pwm_freq(1000000 / self.pulse_period)  # デフォルトのままなら50HZ
        return pwm

    # 角度を受け取ってPCA9685に対応した値を算出する
    def calcPulse(self, angle):
        # パルス幅よりDuty比を求める。
        min_duty = self.servo_min / self.pulse_period
        max_duty = self.servo_max / self.pulse_period

        # 全体に対して何％の角度か。例えば、フルが180°に対しての60°であれば33%。
        par_angle = (angle / self.range_angle)

        # 角度からDuty比を求める
        duty = ((max_duty - min_duty) * par_angle) + min_duty

        # PCA9685（サーボドライバ）は12bit扱うことができるのでDuty比を乗算して対応した値にする。
        pulse_value = duty * 4096

        # 少数は切り捨て打て整数で返すs
        return int(pulse_value)
