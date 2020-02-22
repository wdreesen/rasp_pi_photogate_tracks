import RPi.GPIO as GPIO
import time

START = 12
END = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(START,GPIO.IN) #Start Gate
GPIO.setup(END,GPIO.IN)  #End Gate

second_stop = 0 
start = 0 
stop = 0 

flag = False
second_flag = False

try:
    while True:
        #if GPIO.input(11) != gate_state

        #print(GPIO.input(START),GPIO.input(END))
        if GPIO.input(START) == False :
            start = time.time()
            stop = start
        if GPIO.input(END) == True and flag == False:
            stop = time.time()
            flag = True
        if GPIO.input(END) == True and second_flag == False:
            second_stop = time.time()
            second_flag = True
        if (stop - start) > 0.001:
            print('Time 1: ', stop - start, 's')
            print('Speed 1: ', 3.3/ (stop - start),'cm/s')
        if (second_stop - start) > 0.001:
            print('Time 2: ',second_stop - start, 's')
            print('Speed 2: ', 3.3/ (second_stop - start),'cm/s')
            break

except KeyboardInterrupt:
    GPIO.cleanup()
