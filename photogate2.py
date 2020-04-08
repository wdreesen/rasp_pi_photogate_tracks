import RPi.GPIO as GPIO
import time
import sys 

print('place marbles on track and realse gate when ready')

START = 12
END = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(START,GPIO.IN) #Start Gate
GPIO.setup(END,GPIO.IN)  #End Gate
start = 0 
stop = 0 
stop2  = 0 

# Initialize gate change state
start_gate_flag = False
first_marble_flag = True
second_marble_flag = False
done = False

try:
    while True:
        if GPIO.input(START) == False and start_gate_flag == False:
            start = time.time()
            start_gate_flag = True
            print("Start", start)
        if (
            GPIO.input(END) == True and 
            second_marble_flag == False and 
            first_marble_flag == True
            ):
            stop = time.time()
            first_marble_flag = False
            #second_marble_flag = True
            print("Stop1:",stop)
        if (
            GPIO.input(END) == True and 
            first_marble_flag == False and 
            second_marble_flag == False
            ):
            while GPIO.input(END) == True:
                pass
            second_marble_flag = True
        if (
            GPIO.input(END) == True and 
            second_marble_flag == True and 
            first_marble_flag == False
        ):
            stop2 = time.time()
            done = True
            second_marble_flag == False
            print("Stop2:",stop2)
        if done == True:
            print(start, stop, stop2)
            print('Marble 1 Time: ', stop - start, 's')
            print('Marble 2 Time: ', stop2- start, 's')
            GPIO.cleanup()
            sys.exit(0)
            GPIO.cleanup()
            sys.exit(0)

except KeyboardInterrupt:
    GPIO.cleanup()
