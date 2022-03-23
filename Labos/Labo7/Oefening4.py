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

dc = digitalio.DigitalInOut(board.D23)
cs1 = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D24)
display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate = 1000000)
display.bias = 4
display.contrast = 30
display.invert = True


display.fill(0)
display.show()


image = Image.open(...).resize((display.width, display.height), Image.ANTIALIAS).convert('1')

display.image(image)
display.show()
