import RPi.GPIO as GPIO
import time
from Infrared_Line_Tracker_Sensor_Test import TRSensor
from AlphaBot import AlphaBot
Ab = AlphaBot()
TR = TRSensor()
while True:
    readings = TR.AnalogRead()
    print(readings)
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