#!/usr/bin/env python3

from time import time 
from sys import stderr

from util import robot
from util import constants

def run(targetSpeed, lightSensorPort, endTime, kP=constants.lineFollowkP):
    startTime = time()
    while time() - startTime < endTime:
        error = robot.sensors[lightSensorPort].reflected_light_intensity-constants.lineFollowThresh
        pTerm = error*kP
        robot.driveBase.on(targetSpeed+pTerm, targetSpeed-pTerm)  
    robot.driveBase.off(brake=True)
