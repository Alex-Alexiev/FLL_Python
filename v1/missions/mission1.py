#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sensor.lego import ColorSensor

driveBase = MoveTank(OUTPUT_B, OUTPUT_C)
#cl1 = ColorSensor(INPUT_1)

def run():
    driveBase.on_for_rotations(50, 50, 3, True)

