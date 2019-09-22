#!/usr/bin/env python3

from sys import stderr
from time import sleep
from util import robot
from movements import (gyroTurn, pidLineFollow)

def run():

    pidLineFollow.run(20, 2, 100)

    #gyroTurn.run(180, 20)

    # robot.driveBase.on_for_rotations(50, 50, 3, True)

    # while True:
    #     print(cl3.reflected_light_intensity, file=stderr)
    #     sleep(1)

    # robot.driveBase.on(20, 20)
    # while robot.cl3.reflected_light_intensity > 30:
    #     sleep(0.01)
    # robot.driveBase.off(brake=True)

