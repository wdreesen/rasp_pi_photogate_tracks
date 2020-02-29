import sys
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(<pin#>,GPIO.IN) # Test Pin

while True:
    try:
        print(‘Start:',GPIO.input(<pin#>))
       
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
