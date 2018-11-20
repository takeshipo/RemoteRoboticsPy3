# coding=utf-8

from pwm import SupportServoDriver


# TODO : きれいにDataClassにする
class PwmServoConfigData:

    def __init__(self):
        # ---デフォルト値は一般的に利用されやすい値が入っている。---
        # 値はすべてマイクロ秒で指定する

        # サーボの最大角
        self.range_angle = 180

        # PWMの一周期。
        self.pulse_period = 20000

        # サーボの最大角に対応するパルス幅
        self.servo_max = 2000

        # サーボの最小角に対応するパルス幅
        self.servo_min = 700

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


# --- KHR3HVv2のID設定 ---
# AnkleLeft = 14  # 左足首
# AnkleRight = 18  # 右足首
# ElbowLeft = 5  # 左肘
# ElbowRight = 9  # 右肘
# FootLeft = 15  # 左足先
# FootRight = 19  # 右足先
# HandLeft = 7  # 左手
# HandRight = 11  # 右手
# # HandTipLeft = 21  # Tip of the left hand
# # HandTipRight = 23 # Tip of the right hand
# Head = 3  # 頭
# HipLeft = 12  # 左ヒップ
# HipRight = 16  # 右ヒップ
# KneeLeft = 13  # 左ひざ
# KneeRight = 17  # 右ひざ
# Neck = 2  # 首
# ShoulderLeft = 4  # 左肩
# ShoulderRight = 8  # 右肩
# SpineBase = 0  # 背骨
# SpineMid = 1  # 腰
# # SpineShoulder = 20  # Spine at the shoulder
# # ThumbLeft = 22  # 左親指
# # ThumbRight = 24  # 右親指
# WristLeft = 6  # 左手首
# WristRight = 10  # 右手首

def pwm_servo_driver_test(config_data):
    pwm = SupportServoDriver(config_data=config_data)

    while True:
        # [チャンネル : 角度] の形式で入力を受け付ける。チャンネルに[all]と入力すると全てに出力する。
        data = input()
        data = data.split(':')

        channel = data[0]
        angle = data[1]

        if channel == 'all':
            print('[Receive]')
            print('channel : all')
            print('angle : {0}\n'.format(angle))

            # 接続されているサーボすべてを中心位置（ホーム）にする
            for i in range(0, 16):
                pwm.to_angle(i, int(angle + 12))

        else:
            print('[Receive]')
            print('channel : {0}'.format(channel))
            print('angle : {0}\n'.format(angle))

            pwm.to_angle(int(channel), int(angle + 12))


def i2c_test():
    try:
        bus = smbus2.SMBus(1)
        SLAVE_ADDRESS = 0x08
        while True:

            cmd = input("入力してください：")
            if cmd == 'send':
                bus.write_byte(SLAVE_ADDRESS, ord('A'))
            elif cmd == 'receive':
                read_data = bus.read_byte(SLAVE_ADDRESS)
                print(read_data)

    except KeyboardInterrupt:
        print("プログラムを終了します...")
        pass

    finally:
        bus.close()
        # socket_com.close_socket()
        pass


def serial_test(socket_com):
    # Arduinoとのシリアル通信を準備
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    try:
        while True:
            data = socket_com.recv_str()
            if data == 'QUIT':
                break
            data = data.split(':')
            id = int(data[0])
            rotate = int(data[1])
            print('channel : {0}'.format(id))
            print('angle : {0}\n'.format(rotate))

            arduino.write(b'A')  # 文字を送信
            num = 1
            arduino.write(num.to_bytes(1, 'big'))  # 数字を送信

    finally:
        arduino.close()
        socket_com.close()
