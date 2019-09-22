#!/usr/bin/env python3

from util import (robot, constants)
from ev3dev2.sensor.lego import ColorSensor 
from sys import stderr
from time import sleep

def run():
    robot.driveBase.on(10, 10)

    colorSensorPorts = []
    for i in range(len(robot.sensors)):
        if isinstance(robot.sensors[i], ColorSensor):
            colorSensorPorts.append(i)

    lightMin = []
    lightMax = []

    for i in range(len(colorSensorPorts)):
        lightMin.append(1000)
        lightMax.append(-1000)

    initialPosition = robot.mtB.position
    while robot.mtB.position - initialPosition < 1000:
        for i in range(len(colorSensorPorts)):
            lightReading = robot.sensors[colorSensorPorts[i]].reflected_light_intensity
            if lightReading < lightMin[i]: lightMin[i] = lightReading
            if lightReading > lightMax[i]: lightMax[i] = lightReading

    robot.driveBase.off(brake=True)

    minMaxValues = open("util/calibrationValues.txt", "w+")
    for i in range(len(colorSensorPorts)):
        minMaxValues.write(str(lightMax[i]) + "\n")
        minMaxValues.write(str(lightMin[i]) + "\n")
    minMaxValues.close()

    # readValues = open("util/calibrationValues.txt", "r")
    # print(readValues.read())
    # readValues.close()    
