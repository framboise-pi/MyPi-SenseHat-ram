#!/usr/bin/env python
#coding=utf-8
#
#*	MyPi-SenseHat-ram
#*	https://github.com/framboise-pi/MyPi-SenseHat-ram
#*	Copyright(C) 2020 Cedric Camille Lafontaine http://www.framboise-pi.fr,
#*	version 0.0.1
#

from sense_hat import SenseHat
import random
from random import randint
import psutil
import time

global tour

tour = 0
sense = SenseHat()
sense.rotation = 270
sense.low_light = True
sense.clear()

print("...starting SenseHat ram script...")

def PixelRam(tour,ram):
	green = [0,255,0]
	y = 0
	percent = int(ram)
	if (percent <= 12):
		y = 7
		green[0] = 100
	if (percent > 12 and percent <= 25):
		y = 6
		green[0] = 120
	if (percent > 25 and percent <= 37):
		y = 5
		green[0] = 140
	if (percent > 37 and percent <= 40):
		y = 4
		green[0] = 160
	if (percent > 40 and percent <= 52):
		y = 3
		green[0] = 180
	if (percent > 52 and percent <= 65):
		y = 2
		green[0] = 200
	if (percent > 65 and percent <= 77):
		y = 1
		green[0] = 220
	if (percent > 77 and percent <= 100):
		y = 0
	#debug
	#print ("ram:",percent,"tour:",tour,"pixel h:",y,"bright:",green[0])
	sense.set_pixel(tour,y,green)

while True:
	ram = psutil.virtual_memory().percent
	if (ram is not None):
		if (tour >= 7):
			sense.clear()
			tour = 0
		else: tour = tour + 1
		PixelRam(tour,ram)
		time.sleep(1)
