# coding=utf-8
from pwm import SupportServoDriver

AnkleLeft = 14  # 左足首
AnkleRight = 18  # 右足首
ElbowLeft = 5  # 左肘
ElbowRight = 9  # 右肘
FootLeft = 15  # 左足先
FootRight = 19  # 右足先
HandLeft = 7  # 左手
HandRight = 11  # 右手
# HandTipLeft = 21  # Tip of the left hand
# HandTipRight = 23 # Tip of the right hand
Head = 3  # 頭
HipLeft = 12  # 左ヒップ
HipRight = 16  # 右ヒップ
KneeLeft = 13  # 左ひざ
KneeRight = 17  # 右ひざ
Neck = 2  # 首
ShoulderLeft = 4  # 左肩
ShoulderRight = 8  # 右肩
SpineBase = 0  # 背骨
SpineMid = 1  # 腰
# SpineShoulder = 20  # Spine at the shoulder
# ThumbLeft = 22  # 左親指
# ThumbRight = 24  # 右親指
WristLeft = 6  # 左手首
WristRight = 10  # 右手首

# KHR-3HVを動作させるためのモーションなどをこのソースを利用して。
# クラスにするか、このまま通常の関数にするかは、まだ未定

# KHR-3HV Ver2はデフォルトでKRS-2552RHVを17軸搭載する。
# 問題点として、PCA9685は16チャンネルなのでKHRのすべてのサーボを動作させることができない
# 今回は「RICOH THETA」からの視点をHMDに投影する予定なので、首の軸は不要なので16chあればギリギリ足りるはず
# ただ、これから拡張する予定があるなら、PCA9685を複数利用を想定してライブラリのアドレスを定数ではなく変数にすることでおそらく応可


# KRS-2552RHVのデータシートより、
# PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec(=50Hz)とする。
# パルス幅は 700μsec〜2300μsec が 0°〜270°に対応する。
pulse_period = 20000
servo_max = 2300
servo_min = 700
range_angle = 270  # 全角度


# サーボに引数の角度を与える。第二引数はタプルで何も指定しなければすべてのサーボに出力される
def KRS2552RHV_PWM(angle, tuple_ch=range(0, 16)):
    pwm_support = SupportServoDriver(range_angle, pulse_period, servo_max, servo_min, False)
    pwm = pwm_support.get_instance()

    pulse_value = pwm_support.calc_pulse(angle)

    # 接続されているサーボすべてを中心位置（ホーム）にする
    for i in tuple_ch:
        print('チャンネル{0}に{1}\n'.format(i, pulse_value))
        pwm.set_pwm(i, 0, pulse_value)


def KRS2552RHV_Arduino(serial, id, rotate):
    value = int((rotate / 270) * (9500 - 5500) + 5500)
    low = value & 0xff
    high = value >> 8
    high = high & 0xff

    serial.write(b'C')
    serial.write(id)
    serial.write(b'V')
    serial.write(low)
    serial.write(high)


# FIXME: 0°に出力してもうまく出来ない。数値や計算は問題ない。+10°くらいで実際の0°になる。
def RS306MD(angle, tuple_ch=range(0, 16)):
    pwm_support = SupportServoDriver(288, 20000, 2480, 560, False)
    pwm = pwm_support.get_instance()

    pulse_value = pwm_support.calc_pulse(angle)

    # 接続されているサーボすべてを中心位置（ホーム）にする
    for i in tuple_ch:
        print('チャンネル{0}に{1}\n'.format(i, pulse_value))
        pwm.set_pwm(i, 0, pulse_value)
