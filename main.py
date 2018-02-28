# coding=utf-8
from com_socket import *
from servo import *


def move_servo(connection):
    try:
        support_RS306MD = SupportServoDriver(288, 20000, 2480, 560)
        pwm1 = support_RS306MD.get_instance(address=0x40)
        pwm2 = support_RS306MD.get_instance(address=0x41)

        while True:
            data = connection.recv_raw()

            if data == b'':
                break

            # data = data.split(':')
            # channel = int(data[0])
            # angle = int(data[1])

            sub_cmd = int(data[0])
            rotate = int(data[1])
            channel = int((int(data[2]) << 8) + data[3])  # シフトできる？

            print('[Receive]')
            print('channel : {0}'.format(channel))
            print('angle : {0}\n'.format(rotate))

            # 16以下なら上半身
            if channel < 16:
                pulse_value = support_RS306MD.calc_pulse(rotate)
                pwm1.set_pwm(channel, 0, pulse_value)

            else:
                channel -= 16
                pulse_value = support_RS306MD.calc_pulse(rotate)
                pwm2.set_pwm(channel, 0, pulse_value)

    finally:
        connection.close()


if __name__ == '__main__':
    host = '192,168.43.181'  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    connection = SupportSocketClient(host, port, 2)

    # Arduino = serial.Serial('/dev/ttyUSB0', 9600)

    move_servo(connection)
    # テストSlack
    # test_servo()
