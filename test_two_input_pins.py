import RPi.GPIO as GPIO
import time

START = 12
END = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(START,GPIO.IN) #Start Gate
GPIO.setup(END,GPIO.IN)  #End Gate

start = 0 
stop = 0 

try:
    while True:
        print('Start:',GPIO.input(START))
        print('Stop:',GPIO.input(END))
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
