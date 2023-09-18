import Helper as help
import RPi.GPIO as GPIO
import Controller
import Ultrasonic

def turn(direction,pwmL,pwmR):
    valueLeft = Controller.valueL
    valueRight = Controller.valueR
    def turnRight():
        GPIO.output(Controller.MotorLF,GPIO.HIGH)
        GPIO.output(Controller.MotorLR,GPIO.LOW)
        GPIO.output(Controller.MotorRF,GPIO.LOW)
        GPIO.output(Controller.MotorRR,GPIO.HIGH)

    def turnLeft():
        GPIO.output(Controller.MotorRF,GPIO.HIGH)
        GPIO.output(Controller.MotorRR,GPIO.LOW)
        GPIO.output(Controller.MotorLF,GPIO.LOW)
        GPIO.output(Controller.MotorLR,GPIO.HIGH)


    if direction == "right":
        if Controller.trace: print("turning right")
        turnRight()
    elif direction == "left":
        if Controller.trace: print("turning left")
        turnLeft()
    else:
        if Controller.trace: print("turning error")
        raise Exception('Invalid turning direction from motor')
    
def forward(pwmL,pwmR):
    GPIO.output(Controller.MotorLF,GPIO.HIGH)
    GPIO.output(Controller.MotorLR,GPIO.LOW)
    GPIO.output(Controller.MotorRF,GPIO.HIGH)
    GPIO.output(Controller.MotorRR,GPIO.LOW)
    GPIO.output(Controller.MotorLC,GPIO.HIGH)
    GPIO.output(Controller.MotorRC,GPIO.HIGH)
        

def backward():
    if Controller.trace: print("tVelocity satisfied")
    GPIO.output(Controller.MotorLF,GPIO.LOW)
    GPIO.output(Controller.MotorLR,GPIO.HIGH)
    GPIO.output(Controller.MotorRF,GPIO.LOW)
    GPIO.output(Controller.MotorRR,GPIO.HIGH)
    GPIO.output(Controller.MotorLC,GPIO.HIGH)
    GPIO.output(Controller.MotorRC,GPIO.HIGH)
        
def stop():
    if Controller.trace: print("stopping motor")
    GPIO.output(Controller.MotorLF,GPIO.LOW)
    GPIO.output(Controller.MotorLR,GPIO.LOW)
    GPIO.output(Controller.MotorRF,GPIO.LOW)
    GPIO.output(Controller.MotorRR,GPIO.LOW)
    GPIO.output(Controller.MotorLC,GPIO.LOW)
    GPIO.output(Controller.MotorRC,GPIO.LOW)