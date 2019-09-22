#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

driveBase = MoveTank(OUTPUT_B, OUTPUT_C)
mtB = LargeMotor(OUTPUT_B)

gy1 = GyroSensor(INPUT_1)
cl2 = ColorSensor(INPUT_2)
cl3 = ColorSensor(INPUT_3)
cl4 = ColorSensor(INPUT_4)

sensors = [None, gy1, cl2, cl3, cl4]

