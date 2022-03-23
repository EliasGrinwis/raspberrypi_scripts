import time
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from adafruit_bus_device.spi_device import SPIDevice

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate= 1000000)

def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    with adc:
        r = bytearray(3)
        spi.write_readinto([1,(8+adcnum)<<4,0], r)
        time.sleep(0.000005)
        adcout = ((r[1]&3) << 8) + r[2] 
        return adcout 

dc = digitalio.DigitalInOut(board.D23)
cs1 = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D24)
display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate = 1000000)
display.bias = 4
display.contrast = 30
display.invert = True

display.fill(0)
display.show()

font = ImageFont.load_default()

while True:
    tmp0 = readadc(0) # read channel 0 
    tmp1 = readadc(1)

    image = Image.new('1', (display.width, display.height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, display.width, display.height), outline=255, fill=255)

    draw.text((1,8), 'ADC value', font=font)
    draw.text((1,16), 'on display', font=font)
    draw.text((1,24), 'in0=' + str(tmp0), font=font)
    draw.text((1, 32), 'in1=' + str(tmp1), font=font)

    display.image(image)
    display.show()