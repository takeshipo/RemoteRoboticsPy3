from pwm import support_servo_driver
from sockrt import socket_communication
import khr3hv

# TODO: ソケット通信の際の例外処理が記述されていない！


if __name__ == '__main__':

    host = "192.168.1.100"
    port = 49152  # wellknownにぶつからない適当なポート番号
    socket = socket_communication(host, port)

    while True:
        message = socket.get_date()

        if message == 'KHR3HV':
            get_date = socket.get_date()
            khr3hv.KRS2552RHV_all(get_date)
