import KeyPressModule as kp
import time
import RPi.GPIO as GPIO
kp.init()
from Infrared_Line_Tracker_Sensor_Test import TRSensor
from AlphaBot import AlphaBot
Ab = AlphaBot()
TR = TRSensor()
Ab.stop()
key=0
f=0
obj=3
DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

while True:
    readings = TR.AnalogRead()
    if readings[0]<550:
        Ab.left()
        time.sleep(0.02)
    elif readings[4]<550:
        Ab.right()
        time.sleep(0.02)
    elif readings[2]<550 and readings[0]>550 and readings[4]>550:
        Ab.forward()
    elif readings[0]>550 and readings[1]>550 and readings[2]>550 and readings[3]>550 and readings[4]>600:
        Ab.stop()
    try:
        DR_status = GPIO.input(DR)
        DL_status = GPIO.input(DL)
        if DL_status==0 and DR_status==0:
            obj=3
        elif DL_status==1 and DR_status==0:
            obj=1
        elif DL_status==0 and DR_status==1:
            obj=2
        else:
            obj=0
    except:
        pass
    if kp.GetKey('LEFT'):
        f=1
    if key==0 and obj!=3 and obj!=1 and f==1:
        Ab.left()
        time.sleep(0.56)
        Ab.right()
        time.sleep(0.56)
        Ab.stop()
        key=1