#!/usr/bin/python3.4

from time import sleep
from sys import exit
from random import randint

from GPIOclass import GPIOpin

from generic import base


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
            if (cpuTemp > tempThreshold):
                if not(gpio7.getGPIOoutput()):
                    gpio7.setGPIOoutput(True)
                if not(gpio11.getGPIOoutput()):
                    gpio11.setGPIOoutput(True)
                sleepTime = sleepTimeFanOn
                print('CPU temperature crossed threshold: %s' % str(cpuTemp))
            elif (cpuTemp < tempThreshold):
                if gpio7.getGPIOoutput():
                    gpio7.setGPIOoutput(False)
                if gpio11.getGPIOoutput():
                    gpio11.setGPIOoutput(False)
                sleepTime = sleepTimeFanOff
                print('CPU temperature in limit: %s' % str(cpuTemp))
            print('Rechecking in %d seconds' % sleepTime)
            sleep(sleepTime)
    except (KeyboardInterrupt, Exception) as e:
        if e:
            print('UnknownException: %s' % str(e))
        gpio7.resetGPIOPin()
        gpio11.resetGPIOPin()
        gpio7.cleanupGPIO()  # Can use any of the GPIOpin object to call
        exit(0)

if __name__ == '__main__':
    main()
