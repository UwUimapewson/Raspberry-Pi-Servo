#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  servo.py
#  
#  Copyright 2022  Sam Tessar
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03, 50)

pwm.start(0)

def SetAngle(angle):

	duty = angle / 18 + 2

	GPIO.output(03, True)

	pwm.ChangeDutyCycle(duty)

	sleep(1)

	GPIO.output(03, False)

	pwm.ChangeDutyCycle(0)

while True:

	SetAngle(180) 

	sleep(.02)

	SetAngle(0)
	
	sleep(.02)

pwm.stop()

GPIO.cleanup()
