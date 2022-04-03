# import RPi.GPIO as GPIO
# import time
# GPIO.setmode(GPIO.BOARD)
# control_pins = [7,11,13,15]
# for pin in control_pins:
#   GPIO.setup(pin, GPIO.OUT)
#   GPIO.output(pin, 0)
# halfstep_seq = [
#   [1,0,0,0],
#   [1,1,0,0],
#   [0,1,0,0],
#   [0,1,1,0],
#   [0,0,1,0],
#   [0,0,1,1],
#   [0,0,0,1],
#   [1,0,0,1]
# ]
# for i in range(512):
#   for halfstep in range(8):
#     for pin in range(4):
#       GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
#     time.sleep(0.001)
# GPIO.cleanup()



import RPi.GPIO as GPIO
from datetime import datetime
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    print ("Waiting For Sensor To Settle")
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

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

        distance = round(distance, 2)
        print ("Distance:", distance,"cm")
        print(current_time)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()