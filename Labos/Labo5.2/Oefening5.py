import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


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
    if (GPIO.input(17) == 1):
        GPIO.output(22, 1)
        time.sleep(0.5)
        GPIO.output(22, 0)
        time.sleep(0.5)
        GPIO.output(27, 1)
        time.sleep(0.5)
        GPIO.output(27, 0)
        time.sleep(0.5)
        GPIO.output(23, 1)
        time.sleep(0.5)
        GPIO.output(23, 0)
        time.sleep(0.5)
        GPIO.output(24, 1)
        time.sleep(0.5)
        GPIO.output(24, 0)

        print("Right to Left")
        time.sleep(0.5)
    else:
        GPIO.output(24, 1)
        time.sleep(0.5)
        GPIO.output(24, 0)
        time.sleep(0.5)
        GPIO.output(23, 1)
        time.sleep(0.5)
        GPIO.output(23, 0)
        time.sleep(0.5)
        GPIO.output(27, 1)
        time.sleep(0.5)
        GPIO.output(27, 0)
        time.sleep(0.5)
        GPIO.output(22, 1)
        time.sleep(0.5)
        GPIO.output(22, 0)

        print("Left to Right")
        time.sleep(0.3)


GPIO.cleanup()