from khr import support_servo_driver

# KRS-2552RHV（サーボ）のデータシートより、
# PWMの周期は 3msec〜30msecに対応する。ここでは20000μsec = 50Hzとする。
# パルス幅は 700μsec〜2300μsec が 0°〜270°に対応する。
pulse_period = 20000
servo_max = 2300
servo_min = 700
range_angle = 270  # 全角度

if __name__ == '__main__':

    support = support_servo_driver(range_angle, pulse_period, servo_max, servo_min, False)
    pwm = support.get_instance()

    home_degree = range_angle/ 2  # 中心の角度
    home_pulse = support.calcPulse(home_degree)

    # 接続されているサーボすべてを中心位置（ホーム）にする
    for i in range(0, 15):
        pwm.set_pwm(i, 0, home_pulse)
