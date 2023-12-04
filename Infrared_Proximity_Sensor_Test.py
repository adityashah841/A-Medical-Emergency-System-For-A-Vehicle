import RPi.GPIO as GPIO
import time

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

print("Proximity Sensor Testing")

try:
	while True:
		DR_status = GPIO.input(DR)
		DL_status = GPIO.input(DL)
		if((DL_status == 0) and (DR_status == 0)):
			print("No Object in Front")
		elif((DL_status == 1) and (DR_status == 0)):
			print("Alert!! Object in Right")
		elif((DL_status == 0) and (DR_status == 1)):
			print("Alert!! Object in Left")

except KeyboardInterrupt:
	GPIO.cleanup();
