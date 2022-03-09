import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

while True:
    if (GPIO.input(17) == 1):
        GPIO.output(24, 1)
        print("led blinks")
        time.sleep(0.3)
    else:
        GPIO.output(24, 0)
        print("LED not flashing")
        time.sleep(0.3)


GPIO.cleanup()