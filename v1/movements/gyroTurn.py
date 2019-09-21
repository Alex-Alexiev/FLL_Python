#!/usr/bin/env python3

from util import robot
from time import sleep

def target(targetAngle, speed):
    initialAngle = robot.gy1.angle
    currAngle = initialAngle
    while currAngle - initialAngle < targetAngle:
        robot.driveBase.on(speed, -speed)
        currAngle = robot.gy1.angle
        sleep(0.01)
    robot.driveBase.off(brake=True)
