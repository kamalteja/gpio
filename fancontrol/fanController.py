#!/usr/bin/python3.4

#from
from time import time, sleep, localtime, asctime
from sys import exit
from random import randint

from GPIO.GPIOclass import GPIOpin
from common.generic import base


def main():
    try:
        # Creating base class object
        gl = base()

        # localvariables
        sleepTimeFanOn = sleepTime = 30
        sleepTimeFanOff = 1800
        tempThreshold = gl.getTempThreshold()
        assert type(tempThreshold) is int or type(
            tempThreshold) is float, 'Invalid tempThreshold: %d' % tempThreshold

        # Creating GPIOpin class objects
        gpio7 = GPIOpin(7, 'OUT', 'BOARD')  # Instantiatin gpio7
        gpio11 = GPIOpin(11, 'OUT', 'BOARD')  # Instantiatin gpio7
        print(gpio7)
        print(gpio11)

        # Fancontroll loop
        while(True):
            cpuTemp = gl.getCPUtemperature()
            time = gl.currentTime("asctime")
            if (cpuTemp > tempThreshold):
                if not(gpio7.getGPIOoutput()):
                    gpio7.setGPIOoutput(True)
                if not(gpio11.getGPIOoutput()):
                    gpio11.setGPIOoutput(True)
                sleepTime = sleepTimeFanOn
                print('%s: CPU temperature crossed threshold: %s'
                    %(time, str(cpuTemp)))
            elif (cpuTemp < tempThreshold):
                if gpio7.getGPIOoutput():
                    gpio7.setGPIOoutput(False)
                if gpio11.getGPIOoutput():
                    gpio11.setGPIOoutput(False)
                sleepTime = sleepTimeFanOff
                print('%s: CPU temperature in limit: %s' % (time, str(cpuTemp)))
            print('%s: Rechecking in %d seconds' % (time, sleepTime))
            sleep(sleepTime)
    except (KeyboardInterrupt, Exception) as e:
        if e:
            print('%s: UnknownException: %s' % (time, str(e)))
        gpio7.resetGPIOPin()
        gpio11.resetGPIOPin()
        gpio7.cleanupGPIO()  # Can use any of the GPIOpin object to call
        exit(0)

if __name__ == '__main__':
    main()
