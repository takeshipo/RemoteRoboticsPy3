from pwm import support_servo_driver

# KHR-3HVを動作させるためのモーションなどをこのファイル作成して行く。
# クラスにするか、このまま通常の関数にするかは、まだ未定

# KHR-3HV Ver2はデフォルトで17軸、サーボ はKRS-2552RHVを搭載する。
# 問題点として、PCA9685は16チャンネルなのでKHRのすべてのサーボを動作させることができない
# 今回は「RICOH THETA」からの視点をHMDに投影する予定なので、首の軸は不要なので16chあればギリギリ足りるはず
# ただ、これから拡張する予定があるなら、PCA9685を複数利用を想定してライブラリのアドレスを定数ではなく変数にすることで多分対応可


# KRS-2552RHVのデータシートより、
# PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec(=50Hz)とする。
# パルス幅は 700μsec〜2300μsec が 0°〜270°に対応する。
pulse_period = 20000
servo_max = 2300
servo_min = 700
range_angle = 270  # 全角度


# 接続されているすべてのサーボに引数の角度を与える
def KRS2552RHV_all(angle, tuple_ch=range(0, 15)):
    support = support_servo_driver(range_angle, pulse_period, servo_max, servo_min, False)
    pwm = support.get_instance()

    home_pulse = support.calcPulse(angle)

    while True:
        try:
            # 接続されているサーボすべてを中心位置（ホーム）にする
            for i in tuple_ch:
                pwm.set_pwm(i, 0, home_pulse)
        except KeyboardInterrupt:
            pass
