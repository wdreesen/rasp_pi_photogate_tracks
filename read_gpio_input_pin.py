import sys
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN) # Test Pin 12

while True:
    try:
        print(‘Start:',GPIO.input(<pin#>))
       
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()
