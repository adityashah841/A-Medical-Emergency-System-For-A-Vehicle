import RPi.GPIO as GPIO
import time

SERVO_A = 27
SERVO_B = 22

GPIO.setup(SERVO_A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SERVO_B, GPIO.OUT, initial=GPIO.LOW) 
p = GPIO.PWM(SERVO_A,50)
p.start(0)
q = GPIO.PWM(SERVO_B,50)
q.start(0)

def ServoAngle_A(angle):
	p.ChangeDutyCycle(2.5 + 10.0 * angle / 180)

def ServoAngle_B(angle):
	q.ChangeDutyCycle(2.5 + 10.0 * angle / 180)

ServoAngle_A(90)		
ServoAngle_B(90)		
print("Servo_Motor_Testing")
try:
    while True:
        ServoAngle_A(5)
        ServoAngle_B(5)
        time.sleep(1)
        ServoAngle_A(180)
        ServoAngle_B(180)
        time.sleep(1)  
        ServoAngle_A(90)
        ServoAngle_B(90)
        time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup();


