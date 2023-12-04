import RPi.GPIO as GPIO
import time

if __name__ == '__main__':

	from AlphaBot import AlphaBot
	
	Ab = AlphaBot()

	while True:
                Ab.right()
                time.sleep(0.3)
                Ab.left()
                time.sleep(0.4)
                Ab.stop()
                break
                