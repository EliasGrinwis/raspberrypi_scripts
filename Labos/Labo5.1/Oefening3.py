import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin1, pin2, pin3, pin4):
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)
    GPIO.output(pin3, 1)
    GPIO.output(pin4, 1)
    time.sleep(0.5)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)
    GPIO.output(pin3, 0)
    GPIO.output(pin4, 0)

    time.sleep(0.5)


while True:
    blink(18, 23, 24, 25)

GPIO.cleanup()
