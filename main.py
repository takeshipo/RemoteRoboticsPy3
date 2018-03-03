# coding=utf-8
from com_socket import *
from servo import *


def behavior_servo(connection):
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

            sub_cmd = data[0]  # int.from_bytes((data[0]), 'big')
            id = data[1]
            # rotate = int((data[2] << 8) or data[3])  # シフトできる？
            sign_flg = data[2]
            if sign_flg == 0:
                rotate = int(data[2])
            elif sign_flg == 1:
                rotate = int(data[2]) * -1

            print('[Receive]')
            print('id : {0}'.format(id))
            print('rotate : {0}\n'.format(rotate))

            # 16以下なら上半身
            if id < 16:
                pulse_value = support_RS306MD.calc_pulse(rotate)
                pwm1.set_pwm(id, 0, pulse_value)

            else:
                id -= 16
                pulse_value = support_RS306MD.calc_pulse(rotate)
                pwm2.set_pwm(id, 0, pulse_value)

    finally:
        connection.close()


if __name__ == '__main__':
    host = '192.168.43.181'  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    connection = SupportSocketClient(host, port, 4)

    # Arduino = serial.Serial('/dev/ttyUSB0', 9600)

    behavior_servo(connection)
