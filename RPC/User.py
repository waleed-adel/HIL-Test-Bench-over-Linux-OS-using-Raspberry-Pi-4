import time
import GPIO_write_client
from GPIO_macros import *

## GPIO pins ##
# 25 o/p -> 2 i/p
# 24 o/p -> 3 i/p
# 16 o/p -> 5 i/p

## PWM pins ##
# 18 PWM1
# 13 PWM2

#define PWM_GPIO		18
#define PWM2_GPIO		13
#define PWM_INPUT		23
#define PWM2_INPUT		6

def Test_main ():
    
    ## Write Test cases starting from here ##
    TestBench.GPIO_SetMode(25, OUTPUT)
    
    TimeBeforeExec = time.time()
    TestBench.GPIO_SetMode(2, INPUT)
    TimeAfterExec = time.time()
    print ( "Time taken for GPIO SetMode : " + str( (TimeAfterExec - TimeBeforeExec) *1000) +" ms" )
    
    TimeBeforeExec = time.time()
    TestBench.GPIO_Write(25, HIGH)
    TimeAfterExec = time.time()
    print ( "Time taken for GPIO write : " + str( (TimeAfterExec - TimeBeforeExec) *1000) +" ms")
    
    TimeBeforeExec = time.time()
    value = TestBench.GPIO_Read(2)
    TimeAfterExec = time.time()
    print ( "Time taken for GPIO Read : " + str( (TimeAfterExec - TimeBeforeExec) *1000) +" ms" )
    print ("Pin 2 reading : " + str(value) )
    
    TimeBeforeExec = time.time()
    TestBench.GPIO_SetMode(24, OUTPUT)
    TimeAfterExec = time.time()
    print ( "Time taken for GPIO SetMode 2 (true): " + str( (TimeAfterExec - TimeBeforeExec) *1000) +" ms" )
    
    TestBench.GPIO_SetMode(3, INPUT)
    TestBench.GPIO_Write(24, LOW)
    value = TestBench.GPIO_Read(3)
    print ("Pin 3 reading : " + str(value) )
    
    TestBench.GPIO_SetMode(16, OUTPUT)
    TestBench.GPIO_SetMode(5, INPUT)
    TestBench.GPIO_Write(16, HIGH)
    value = TestBench.GPIO_Read(5)
    print ("Pin 5 reading : " + str(value) )

    #PI PWM Output
    TestBench.GPIO_SetMode(18, ALT5)
    TestBench.PWM_Configure(18, 1, 500000)
    
    TestBench.GPIO_SetMode(13, ALT5)
    TestBench.PWM_Configure(13, 5000,300000)
    
    
    #PI PWM Input
    TestBench.PWM_InputInit(23)
    TestBench.PWM_InputInit(6)
    while(1):
      time.sleep(0.5)
      Dutycycle1 = TestBench.PWM_GetDutyCycle(23)
      Frequency1 = TestBench.PWM_GetFrequency(23)
      
      Dutycycle2 = TestBench.PWM_GetDutyCycle(6)
      Frequency2 = TestBench.PWM_GetFrequency(6)
      
      print("PWM_INPUT_DC1: " + str(Dutycycle1))
      print("PWM_INPUT_F1: \n" + str(Frequency1))
      
      print("PWM_INPUT_DC2: " + str(Dutycycle2))
      print("PWM_INPUT_F2: \n" + str(Frequency2))
      
    
    
    ##TESTING SERIAL   
    # SerialHandle = TestBench.Serial_Open(HIGH_PERFORMANCE_SERIAL, BAUD_RATE, SERIAL_FLAGS)
    # Message = b'MY NAME IS LORD VOLDMORT'
    # TestBench.Serial_Write(SerialHandle, Message)
    
if __name__ == '__main__':
    global TestBench
    TestBench = GPIO_write_client.TestBench()
    Test_main()
    #TestBench.PIGPIO_Stop()
    
    
    
    