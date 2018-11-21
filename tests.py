# coding=utf-8
from servo import *


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
