#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound 
from time import sleep

from missions import (mission1)

import os
os.system('setfont Lat15-TerminusBold32x16')  

btn = Button()
sound = Sound()

currProgram = 0
print(currProgram)

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
        if currProgram == 1:
            print("running 1")
            mission1.run()
    
btn.on_left = left
btn.on_right = right
btn.on_enter = enter


print("ready")
sound.beep()

while True: 
    btn.process()
    sleep(0.01)