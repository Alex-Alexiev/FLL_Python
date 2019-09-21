#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_3, INPUT_1

driveBase = MoveTank(OUTPUT_B, OUTPUT_C)
cl3 = ColorSensor(INPUT_3)
gy1 = GyroSensor(INPUT_1)