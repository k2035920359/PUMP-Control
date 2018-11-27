#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

###### pin assign
#PCF8591 --------- Raspberry pi3
# SDA ------------ GPIO2/SDA1
# SCL ------------ GPIO3/SCL1
# VCC ------------- 3.3V
# GND ------------- GND
#
######

# Description
# in this program, Raspberry pi read a variable registers value(0-255) on PCF8591 default. And 
# Output to LED which is on PCF8591 using Digital analog converter.

import wiringpi
import time



class PCF8591:
	def __init__(self, addr):
		#wiringpi.wiringPiSetup() #setup wiringpi
		wiringpi.wiringPiSetupGpio() #setup wiringpi

		self.i2c = wiringpi.I2C() #get I2C
		self.dev = self.i2c.setup(addr) #setup I2C device

	def LED_ON(self):
		self.i2c.writeReg8(self.dev, 0x40, 0xFF)
		
	def LED_OFF(self):
		self.i2c.writeReg8(self.dev, 0x40, 0x00)
		
	def DAoutput(self,value):
		self.i2c.writeReg8(self.dev, 0x40, value)
		
	def analogRead0(self):
		self.i2c.writeReg8(self.dev, 0x48,0x40)
		self.i2c.readReg8(self.dev,0x48)	#read dummy
		return self.i2c.readReg8(self.dev,0x48)
		
	def analogRead1(self):
		self.i2c.writeReg8(self.dev, 0x48,0x41)
		self.i2c.readReg8(self.dev,0x48)	#read dummy
		return self.i2c.readReg8(self.dev,0x48)
		
	def analogRead2(self):
		self.i2c.writeReg8(self.dev, 0x48,0x42)
		self.i2c.readReg8(self.dev,0x48)	#read dummy
		return self.i2c.readReg8(self.dev,0x48)
	def analogRead3(self):
		self.i2c.writeReg8(self.dev, 0x48,0x43)
		self.i2c.readReg8(self.dev,0x48)	#read dummy
		return self.i2c.readReg8(self.dev,0x48)
	def analogRead(self,pin):
		self.i2c.writeReg8(self.dev, 0x48,0x40+pin)
		self.i2c.readReg8(self.dev,0x48)	#read dummy
		return self.i2c.readReg8(self.dev,0x48)

if __name__ == "__main__":
	pcf8591 = PCF8591(0x48)
	PWM_PIN = 19
	wiringpi.pinMode( PWM_PIN, 1 )
	T=10 #msec
	while True:
		value=pcf8591.analogRead0()
		ONtime=T*(value/255.0)
		OFFtime=T-ONtime
		print(ONtime)
		#pcf8591.DAoutput(value)
		wiringpi.digitalWrite( PWM_PIN, 1 )
		time.sleep(ONtime/1000)
		wiringpi.digitalWrite( PWM_PIN, 0 )
		time.sleep(OFFtime/1000)

	

