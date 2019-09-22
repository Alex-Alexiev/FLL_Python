#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound 
from time import sleep
from sys import stderr
from util import (robot, calibration)

from missions import (mission1)

import os
os.system('setfont Lat15-TerminusBold32x16')  

btn = Button()
sound = Sound()

currProgram = 1
print(currProgram)

#array of missions 
missions = [mission1, calibration]

def left(state):
    global currProgram
    if state:
        currProgram -= 1
        print(currProgram)

def right(state): 
    global currProgram
    if state:
        currProgram += 1
        print(currProgram)

def enter(state):
    global currProgram
    if state:
        print("running mission " + str(currProgram))
        missions[currProgram-1].run()
    
btn.on_left = left
btn.on_right = right
btn.on_enter = enter

print("ready")
sound.beep()

while True: 
    btn.process()
    sleep(0.01)