import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(<pin#>,GPIO.IN) # Test Pin

try:
    while True:
        print(‘Start:',GPIO.input(<pin#>))
       
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
