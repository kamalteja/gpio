#!/usr/bin/python3.4

import os

class base:
	'''
	A base class with generic methods
	'''
	def __init__(self):
		self.tempThreshold = 40.0
		self.plinus = 10.0	#plus or minus tempThreshold

	def getTempThreshold(self):
		return self.tempThreshold

	def getPlinus(self):
		return self.plinus

	def getCPUtemperature(self):
		'''
		Return CPU temperature as a float
		'''
		self.res = os.popen('vcgencmd measure_temp').readline()
		return(float(self.res.replace("temp=","").replace("'C\n","")))
