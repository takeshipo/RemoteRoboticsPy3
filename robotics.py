# coding=utf-8
from enum import IntEnum
from servo import *


class State(IntEnum):
    ON_NEWTRAL = 199
    ON_FORWARD = 200
    ON_BACKWARD = 201
    ON_RIGHT_TURN = 202
    ON_LEFT_TURN = 203
    ON_STOP = 204


class Robotics(object):

    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        self.state = 0
        self.previous_state = -1

    def control(self, state):
        self.state = state
        func = self.on_neutral

        if self.state == State.ON_FORWARD:
            func = self.on_forward

        elif self.state == State.ON_RIGHT_TURN:
            func = self.on_right_turn

        elif self.state == State.ON_LEFT_TURN:
            func = self.on_left_turn

        elif self.state == State.ON_BACKWARD:
            func = self.on_backward

        elif self.state == State.ON_STOP and self.previous_state != State.ON_STOP:
            func = self.on_stop

        elif self.state == State.ON_NEWTRAL and self.previous_state != State.ON_NEWTRAL:
            func = self.on_neutral

        self.previous_state = self.state

        self.executor.submit(fn=func)

    def on_forward(self):
        print("前進")

    def on_backward(self):
        print("後進")

    def on_left_turn(self):
        print("左旋回")

    def on_right_turn(self):
        print("右旋回")

    def on_stop(self):
        print('ストップ')

    def on_neutral(self):
        print('ニュートラルポジション')
