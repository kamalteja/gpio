#!/usr/bin/python3.4

#import
import os
import time

#from
from sys import exit

class base:
    '''
    A base class with generic methods
    '''

    def __init__(self):
        self.tempThreshold = 40.0
        self.plinus = 10.0  # plus or minus tempThreshold
        self.sup_formats = ["time", "localtime", "asctime"]
        self.format = self.sup_formats[0]

    def getTempThreshold(self):
        return self.tempThreshold

    def getPlinus(self):
        return self.plinus

    def getCPUtemperature(self):
        '''
        Return CPU temperature as a float
        '''
        self.res = os.popen('vcgencmd measure_temp').readline()
        return(float(self.res.replace("temp=", "").replace("'C\n", "")))

    def currentTime(self, format=None):
        '''
        Returns current time in asc format
        Supported formats: time, localtime, asctime
        '''
        if format is None:
            format = self.format
        try:
            assert type(format) is str and (format in self.sup_formats)
            return str(getattr(time, format)())
        except Exception as e:
            print (str(e) + self.timeUsage())
            exit(0)

    def timeUsage(self):
        '''
        Prints the usage information to use currentTIme function
        '''
        usage = ""
        usage += "Supported formats: "
        for item in self.sup_formats:
            usage += item + ", "
        return usage
