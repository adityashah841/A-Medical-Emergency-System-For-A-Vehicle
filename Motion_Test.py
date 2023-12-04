#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

if __name__ == '__main__':

	from AlphaBot import AlphaBot
	
	Ab = AlphaBot()
	Ab.stop()
	print("Motion Testing")

	while True:
                Ab.forward()
                time.sleep(1)
                Ab.backward()
                time.sleep(1)
                Ab.left()
                time.sleep(1)
                Ab.right()
                time.sleep(1)
