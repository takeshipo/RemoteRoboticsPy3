# coding=utf-8
from com_socket import *
from pwm import *

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

def pwm_driver_test(config_data):
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


def kinect_to_robo_zero():
    host = '192.168.43.181'  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    connection = SupportSocketClient(host, port, 4)

    try:
        servo = PwmServoConfigData().get_RS306MD()
        pwm1 = SupportServoDriver(address=0x40, config_data=servo)
        pwm2 = SupportServoDriver(address=0x41, config_data=servo)

        while True:
            data = connection.recv_raw()

            if data == b'':
                break

            # data = data.split(':')
            # channel = int(data[0])
            # angle = int(data[1])

            sub_cmd = data[0]  # int.from_bytes((data[0]), 'big')
            channel = data[1]
            sign_flg = data[2]  # ここは符号を表す

            # FIXME: あれ？ここのdata[2]はdata[3]の間違いじゃない？
            if sign_flg == 0:
                angle = int(data[2])
            elif sign_flg == 1:
                angle = int(data[2]) * -1

            print('[Receive]')
            print('id : {0}'.format(channel))
            print('rotate : {0}\n'.format(angle))

            # FIXME: 0°に出力してもうまく出来ない。数値や計算は問題ない。+12°くらいで実際の0°になる。
            angle += 12

            # 16以下なら上半身
            if channel < 16:
                pwm1.to_angle(channel, angle)

            else:
                channel -= 16
                pwm2.to_angle(channel, angle)
    finally:
        connection.close()
