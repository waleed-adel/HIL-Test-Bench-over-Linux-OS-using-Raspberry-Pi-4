import sys
 
def GenerateFile (option, path):

    f= open (path + "\TestCase.py","w+")
    ## File imports ##
    #f.write ("import time \n")
    f.write ("import GPIO_write_client \n")
    f.write ("from GPIO_macros import * \n")
    
    ## Empty TestCase ##
    if option == 1:
        f.write ("\n\n\n")
        ## Test script main function ##
        f.write ("def Test_main (): \n")
        f.write ("\t## Write Test cases here ##\n")
        f.write ("\n\n\n\n\n")
        
    elif option == 2:
        f.write ("\n\n\n")
        f.write ("def Test_main (): \n")
        ## Blinky example ##
        f.write ("\t## Blinky example ##\n")
        f.write ("\tprint(\"STARTING CODE\")\n")
        f.write ("\tTestBench.GPIO_SetMode(12, OUTPUT) \n")
        f.write ("\tprint(\"SETTING PIN 12 as OUTPUT\")\n")
        f.write ("\twhile 1 :\n")
        f.write ("\t\tTestBench.GPIO_Write(12, HIGH) \n")
        f.write ("\t\tprint(\"PIN 12 - HIGH\")\n")
        f.write ("\t\tTestBench.DelayMS(1000)\n")
        f.write ("\t\tTestBench.GPIO_Write(12, LOW) \n")
        f.write ("\t\tprint(\"PIN 12 - LOW\")\n")
        f.write ("\t\tTestBench.DelayMS(1000)\n")
        f.write ("\n\n\n\n")
        
    
    f.write ("if __name__ == '__main__': \n")
    
    f.write ( "\tglobal TestBench\n")
    f.write ( "\tTestBench = GPIO_write_client.TestBench()\n")
    f.write ( "\tTest_main()\n")
    f.write ( "\tTestBench.PIGPIO_Stop()\n")

    f.close()

if __name__ == '__main__':
  
  if sys.argv[1] == '1' or sys.argv[1] == '2' and sys.argv[2] != 0: 
      GenerateFile(int(sys.argv[1]), sys.argv[2])
  else:
      print("Wrong Parameters")
      sys.exit(1)
 
