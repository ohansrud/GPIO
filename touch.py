#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)

while True:
    input_state = GPIO.input(22)
    #led = GPIO.output(25)
    GPIO.output(25, False)
    if input_state == False:
        GPIO.output(25, True)
        print('Button Pressed')
        time.sleep(0.2)
