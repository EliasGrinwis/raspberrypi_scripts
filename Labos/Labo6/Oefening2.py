#!/usr/bin/env python3 
import cgitb ; cgitb.enable() 
import spidev 
import time
import busio
import digitalio
import board
from adafruit_bus_device.spi_device import SPIDevice
import RPi.GPIO as GPIO

# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate= 1000000)
 
# read SPI data 8 possible adc's (0 thru 7) 
def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    with adc:
        r = bytearray(3)
        spi.write_readinto([1,(8+adcnum)<<4,0], r)
        time.sleep(0.000005)
        adcout = ((r[1]&3) << 8) + r[2] 
        return adcout 
 
def blink(tmp0, tmp1):
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    if (tmp0 - 5 > tmp1 + 5):
        GPIO.output(18, 1)
        GPIO.output(17, 0)
    else:
        GPIO.output(17, 1)
        GPIO.output(18, 0)

while True:
    tmp0 = readadc(0) # read channel 0 
    tmp1 = readadc(1) # read channel 1
    print ("input0:",tmp0)
    print ("input1:",tmp1)
    blink(tmp0, tmp1)
    time.sleep(0.2)