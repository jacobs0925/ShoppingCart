#Libraries
import RPi.GPIO as GPIO
import time, math
import Motor
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 26
 
#set GPIO direction (IN / OUT)
GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def adjustVelocity(pwmL,pwmR):
    d = distance()
    if  0 <= d <= 25:
        modpwm = math.floor(d)
        print("pwm", modpwm)
        pwmL.ChangeDutyCycle(modpwm)
        pwmR.ChangeDutyCycle(modpwm)
    else:
        pwmL.ChangeDutyCycle(60)
        pwmR.ChangeDutyCycle(60)
    
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime STUCK IN LOOP HERE
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        #print("stuck")
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print(distance)
    return distance

def velocity():
    d1 = distance()
    StartTime = time.time()
    
    time.sleep(.5)
    
    d2 = distance()
    StopTime = time.time()
    
    v = (d1 - d2)/(StopTime - StartTime)
    return v

 
if __name__ == '__main__':
    try:
        while True:
            print("test")
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()