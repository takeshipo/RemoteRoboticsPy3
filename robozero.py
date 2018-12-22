# coding=utf-8
from servo import *
from com_socket import *


def tcp_to_robo_zero():
    host = '192.168.43.181'  # ドメイン名、もしくはIPアドレス。socket.gethostname()を代入するとドメイン名を調べてくれる。
    port = 55555  # wellknownにぶつからない適当なポート番号。クライアント側とサーバー側でポート番号を合わせる
    connection = SupportSocketClient(host, port, 4)

    try:
        servo_config = get_RS306MD()
        pwm1 = SupportServoDriver(address=0x40, config_data=servo_config)  # 上半身
        pwm2 = SupportServoDriver(address=0x41, config_data=servo_config)  # 下半身

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

            if sign_flg == 0:
                angle = int(data[3])
            elif sign_flg == 1:
                angle = int(data[3]) * -1

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
