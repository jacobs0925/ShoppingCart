#!/usr/bin/bash
import RPi.GPIO as GPIO
import IRSensor as IR
from Helper import Direction
import SonicSensor as Sonic
import Motor
import time
import math
import Stop

trace = True
terminalVelocity = 50


IRLeft = 18
IRRight = 12

MotorLF = 24
MotorLR = 23
MotorLC = 25

MotorRF = 17
MotorRR = 27
MotorRC = 22
loop = True

UltrasonicPin =4 
Echo = 26

ButtonVar = 0
GPIO.setwarnings(False)
valueL = 60
valueR =60

def setup():
    if trace: print("Executing setup")
    global pwmL,pwmR
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IRLeft, GPIO.IN)
    GPIO.setup(IRRight, GPIO.IN)
    
    GPIO.setup(Echo, GPIO.IN)
    GPIO.setup(UltrasonicPin, GPIO.OUT)   
    GPIO.setup(MotorLF,GPIO.OUT)   # set pins to OUTPUT mode
    GPIO.setup(MotorLR,GPIO.OUT)
    GPIO.setup(MotorLC,GPIO.OUT)
    GPIO.setup(MotorRF,GPIO.OUT)   # set pins to OUTPUT mode
    GPIO.setup(MotorRR,GPIO.OUT)
    GPIO.setup(MotorLC,GPIO.OUT)
    GPIO.setup(MotorRC,GPIO.OUT)
    pwmL = GPIO.PWM(MotorLC,1000)
    pwmL.start(0)
    pwmR = GPIO.PWM(MotorRC,1000)
    pwmR.start(0)
    
	  
def start2():
    global valueR, valueL
    while loop:
        direction = IR.getDirection()
        Sonic.adjustVelocity(pwmL, pwmR)
        
        if trace: print("getDirection:",direction)
        if direction == "straight":
            Motor.forward(pwmL,pwmR)
            if trace: print("Moving forward")
        else:
            Motor.turn(direction, pwmL,pwmR)
            if trace: print("Turning", direction)
        time.sleep(.15)
    
def cleanup():
    if trace: print("Executing cleanup")
    Motor.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        time.sleep(2)
        start2()
    except Exception as e:
        print(e)
        cleanup()
        
                                                         