import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import time
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from adafruit_bus_device.spi_device import SPIDevice

GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24



feedTime = "18:00:00"

GPIO.setup(25, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

dc = digitalio.DigitalInOut(board.D16)
cs1 = digitalio.DigitalInOut(board.CE1)
reset = digitalio.DigitalInOut(board.D26)
display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate = 1000000)
display.bias = 4
display.contrast = 60
display.invert = True

display.fill(0)
display.show()

font = ImageFont.load_default()

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    print ("Waiting For Sensor To Settle")
    while True:
    
        GPIO.output(TRIG, False)
        time.sleep(1)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")


        distance = round(distance, 2)
        print ("Distance:", distance,"cm")
        print(current_time)

        image = Image.new('1', (display.width, display.height))
        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, display.width, display.height), outline=255, fill=255)

        draw.text((1,0), "Tijd: " + current_time, font=font)
        draw.text((1,10), str(distance) + " CM", font=font)
        if (GPIO.input(25) == 0):
            draw.text((1,20), "Dropping Food", font=font)
        if (GPIO.input(8) == 0):
            draw.text((1,20), "Dropping Food", font=font)
        if (GPIO.input(21) == 0):
            draw.text((1,30), "LIGHT ON", font=font)
        if (GPIO.input(21) == 1):
            draw.text((1,30), "LIGHT OFF", font=font)
        display.image(image)
        display.show()

        

        if current_time == feedTime:
            print ("Feeding the fishes at", current_time)
            StepPins = [17,22,5,6]
            for pin in StepPins:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin, False)
            Seq = [[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]
            
            for i in range(512):
                for Seq2 in range(8):
                    for pin in range(4):
                        GPIO.output(StepPins[pin], Seq[Seq2][pin])
                    time.sleep(0.001)
        
        if (GPIO.input(25) == 0):
            GPIO.output(22, 1)
            print("Stepper motor is dropping food in forward direction at", current_time)

            StepPins = [17,22,5,6]
            for pin in StepPins:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin, False)
            Seq = [[1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]]
            
            for i in range(512):
                for Seq2 in range(8):
                    for pin in range(4):
                        GPIO.output(StepPins[pin], Seq[Seq2][pin])
                    time.sleep(0.001)

        else:
            GPIO.output(22, 0)
        

        if (GPIO.input(8) == 0):
            GPIO.output(5, 1)
            print("Stepper motor is dropping food in backward direction at", current_time)
            StepPins = [17,22,5,6]
            for pin in StepPins:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin, False)
            Seq = [[1,0,0,1],
                    [0,0,0,1],
                    [0,0,1,1],
                    [0,0,1,0],
                    [0,1,1,0],
                    [0,1,0,0],
                    [1,1,0,0],
                    [1,0,0,0]]
            
            for i in range(512):
                for Seq2 in range(8):
                    for pin in range(4):
                        GPIO.output(StepPins[pin], Seq[Seq2][pin])
                    time.sleep(0.001)
        else:
            GPIO.output(5, 0)
        
        if (GPIO.input(21) == 1):
            GPIO.output(20, 1)
        
        else:
            GPIO.output(20, 0)
            print("Light ON")
            

except KeyboardInterrupt:
    print("Cleaning up!")
    GPIO.cleanup()