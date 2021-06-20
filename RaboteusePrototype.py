import RPi.GPIO as GPIO                    #Import GPIO library
import time

#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
# programming the GPIO by BCM pin numbers

i=0
TRIG = 3
ECHO = 5
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
pwm1=GPIO.PWM(11,100) # configuring Enable pin means GPIO-11 for PWM
pwm2=GPIO.PWM(19,100) # configuring Enable pin means GPIO-19 for PWM

m11=13
m12=15
m21=21
m22=23
en1=11
en2=19

def setup():
    GPIO.setup(m11,GPIO.OUT)
    GPIO.setup(m12,GPIO.OUT)
    GPIO.setup(m21,GPIO.OUT)
    GPIO.setup(m22,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(19,GPIO.OUT)



def stop():
    print ("stop")
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("Forward")

def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print ("back")

def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("left")

def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print ("right")

#count=0
flag=0

# sensor
GPIO.output(TRIG, False)
print ("Calibrating.....")
print ("Place the object")

while True:
    setup()
    pwm1.start(20) # starting it with 50% dutycycle
    pwm2.start(20) # starting it with 50% dutycycle
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance+1.15, 2)
    print (distance)
    
    if distance > 30:
        forward()
        time.sleep(0.5)
        
    elif (distance < 30 and i%2==0):
        left()
        time.sleep(2)
        i=i+1
        print(i)
        
    elif (distance < 30 and i%2!=0):
        right()
        time.sleep(2)
        i=i+1
        print(i)
        
GPIO.cleanup()