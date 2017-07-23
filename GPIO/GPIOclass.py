#!/usr/bin/python3.4

import RPi.GPIO as gpio


class GPIOboard():
    '''
    This class defines a GPIO BOARD. It even contais getters and setters.
    '''

    def __init__(self, boardType):
        self.setGPIOboard(boardType)

    def getGPIOboardType(self):
        return self.boardType

    def setGPIOboardType(self, boardType):
        try:
            assert type(boardType) is str
            self.boardType = boardType
            gpio.setmode(getattr(gpio, self.boardType))
        except AssertionError:
            print('Error: Invalid GPIO board %s' % boardType)
        except Exception as e:
            print('UnknownException: %s' % str(e))

    def cleanupGPIO(self):
        gpio.cleanup()


class GPIOpin(GPIOboard):
    '''
    This class defines a gpioPin characetristics. List of GPIO pins as per 'BOARD' mode are:
    [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 38, 40]
    '''

    def __init__(self, pin, pinMode, boardType, val=False):
        self.setGPIOboardType(boardType)
        self.setGPIOpin(pin)
        self.setGPIOmode(pinMode)
        self.setGPIOoutput(val)

    def __str__(self):
        return "A GPIO board of type '%s' with GPIO pin number '%d' is instantiated as '%s' pin" % (self.getGPIOboardType(), self.gpioPin, self.gpioPinMode)

    def getGPIOpin(self):
        return self.gpioPin

    def setGPIOpin(self, pin):
        try:
            assert type(pin) is int and (pin <= 40)
            self.gpioPin = pin
        except AssertionError:
            print(
                'Error: Provided Pin: "%s", is not an integer or integer is greater than 40' % str(pin))
        except Exception as e:
            print('UnknownException: %s' % str(e))

    def getGPIOmode(self):
        return self.gpioPinMode

    def setGPIOmode(self, pinMode):
        try:
            assert type(pinMode) is str and (
                pinMode == 'IN' or pinMode == 'OUT')
            self.gpioPinMode = pinMode
            gpio.setup(self.gpioPin, getattr(gpio, self.gpioPinMode))
        except AssertionError:
            print('Error: Invalid GPIO Mode: %s' % pinMode)
        except Exception as e:
            print('UnknownException: %s' % str(e))

    def getGPIOoutput(self):
        return self.gpioOutputVal

    def setGPIOoutput(self, val):
        try:
            assert type(val) is bool
            self.gpioOutputVal = val
            gpio.output(self.gpioPin, self.gpioOutputVal)
        except AssertionError:
            print('Error: Invalid GPIO output %s' % str(val))
        except Exception as e:
            print('UnknownException: %s' % str(e))

    def resetGPIOPin(self):
        print("Turning down pin: %d" % self.gpioPin)
        self.setGPIOoutput(False)
