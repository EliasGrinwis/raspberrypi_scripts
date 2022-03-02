import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


for i in raneg(1, 10):
    blink(24)

GPIO.cleanup()
