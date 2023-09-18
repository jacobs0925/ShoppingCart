import Controller
import RPi.GPIO as GPIO
import Helper as help


def getDirection():
    readings = (GPIO.input(Controller.IRLeft), GPIO.input(Controller.IRRight))
    
    if readings == (1,1):
        return "straight"
    elif readings == (1,0):
        return "right"
    elif readings == (0,1):
         return "left"