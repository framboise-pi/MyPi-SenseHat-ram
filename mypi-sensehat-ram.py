#!/usr/bin/env python3
############################################ mpsram : MyPiSensehatRAM
#
#	Copyright(C) LAFONTAINE CÃ©dric Camille 2020
#	contact@codelibre.fr
#	https://github.com/framboise-pi/MyPi-SenseHat-cpu/blob/master/mypi-sensehat-ram.py
#
#           _        _ _ _             ___
#  ___ ___ _| |___   | |_| |_ ___ ___  |  _|___
# |  _| . | . | -_|  | | | . |  _| -_|_|  _|  _|
# |___|___|___|___|  |_|_|___|_| |___|_|_| |_|
#
# ASCII art generator: http://patorjk.com/software/taag/
#
########################################################################
# USAGE EXAMPLE:
# python3 mypi-sensehat-ram.py
########################################################################
from sense_hat import SenseHat
import random
from random import randint
import psutil
import time

sense = SenseHat()
sense.rotation = 0
sense.low_light = True
sense.clear()
tour = 0
DELAY_SEC = 2
print("...starting SenseHat ram script...")

def PixelRam(ram):
	global tour
	if tour > 7:
		tour = 0
		sense.clear()
	percent = int(ram)
	thresholds = [
		(0, 12, 7, 100),
		(12, 25, 6, 120),
		(25, 37, 5, 140),
		(37, 40, 4, 160),
		(40, 52, 3, 180),
		(52, 65, 2, 200),
		(65, 77, 1, 220),
		(77, 100, 0, 255)
	]
	y = None
	for lower, upper, y_value, green_value in thresholds:
		if lower < percent <= upper:
			if green_value is not None and int(y_value):
				green = (0,green_value,0)
				sense.set_pixel(tour,y_value,green)
				tour += 1
				# DEBUG print ("ram_load:",percent,"tour:",tour,"pixel y:",y_value)
	
while True:
	ram = psutil.virtual_memory().percent
	if float(ram):
		PixelRam(ram)
		time.sleep(DELAY_SEC)
