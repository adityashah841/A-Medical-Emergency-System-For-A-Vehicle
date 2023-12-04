import RPi.GPIO as GPIO
import time

class AlphaBot(object):
    def __init__(self,in1=12,in2=13,ena=6,in3=20,in4=21,enb=26):
        self.IN1 = 12
        self.IN2 = 13
        self.IN3 = 20
        self.IN4 = 21
        self.ENA = 6
        self.ENB = 26

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)
        GPIO.setup(self.ENA,GPIO.OUT)
        GPIO.setup(self.ENB,GPIO.OUT)
        self.forward()
        self.PWMA = GPIO.PWM(self.ENA,500)
        self.PWMB = GPIO.PWM(self.ENB,500)
        self.PWMA.start(50)
        self.PWMB.start(50)

    def forward(self):
        servo2 = GPIO.PWM(12, 50)
        servo1 = GPIO.PWM(13, 50)
        servo1.start(0)
        servo2.start(0)
        duty=100
        while duty>50:
            print(duty)
            servo1.ChangeDutyCycle(duty)
            servo2.ChangeDutyCycle(duty)
            time.sleep(1.3)
            servo1.ChangeDutyCycle(0)
            servo2.ChangeDutyCycle(0)
            time.sleep(0.3)
            duty-=2
            

Ab = AlphaBot()
Ab.forward()