#!/usr/bin/env python3

from util import (robot, constants)
from time import sleep

def run(targetAngle, speed=constants.gyroTurnSpeed):
    initialAngle = robot.gy1.angle
    currAngle = initialAngle
    while currAngle - initialAngle < targetAngle:
        robot.driveBase.on(speed, -speed)
        currAngle = robot.gy1.angle
        sleep(0.01)
    robot.driveBase.off(brake=True)
