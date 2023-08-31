#!/usr/bin/env python3

from RPi import GPIO


class GPIOBoard:
    """
    This class defines a GPIO BOARD. It even contais getters and setters.
    """

    def __init__(self, board_type):
        self.board_type = board_type
        GPIO.setmode(self.board_type)

    def cleanup(self):
        """GPIO clean up"""
        GPIO.cleanup()


class GPIOPin(GPIOBoard):
    """
    This class defines a gpioPin characteristics. List of GPIO pins as per 'BOARD' mode are:
    [7, 11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35, 36, 38, 40]
    """

    def __init__(self, pin, pin_mode=GPIO.IN, board_type=GPIO.BOARD, pin_value=False):
        super().__init__(board_type)
        self.pin = pin
        self.pin_mode = pin_mode
        self.pin_value = pin_value

    def output(self, pin_value: bool):
        GPIO.output(self.pin, pin_value)

    def setup(self, pin_mode):
        GPIO.setup(self.pin, pin_mode)
