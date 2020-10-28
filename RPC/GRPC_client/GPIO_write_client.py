import time
import grpc

#contatin the request and response classes
import GPIO_write_pb2
#contains the generated client and server classes
import GPIO_write_pb2_grpc

# Creating a global stub object for the wrapper functions
global stub
stub = 0 

class TestBench(object):
    
    #constructor
    def __init__(self):
        
        global stub
        #open a gRPC channel
        channel = grpc.insecure_channel('192.168.5.10:50051')
        #create a stub (client)
        stub = GPIO_write_pb2_grpc.PI_GPIOStub(channel)

    ## Defining function wrappers for the user ##
    
    ## Delay function -> ms ##
    def DelayMS (self,Delay_ms):
        t1 = time.perf_counter_ns()
    
        while True:
            t2 = time.perf_counter_ns()
            if ( ((t2 - t1) / (10 ** 6) ) >= (Delay_ms) ):
                break

    ## GPIO functions ##
    def GPIO_SetMode (self,GPIO_PinNumber,GPIO_Mode):
        #create a valid request message
        Mode_params = GPIO_write_pb2.ModeInputParams(gpio_pin=GPIO_PinNumber,gpio_mode=GPIO_Mode)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.set_mode(Mode_params)

    def GPIO_Write (self,GPIO_PinNumber,GPIO_Level):
        #create a valid request message
        Write_params = GPIO_write_pb2.SetInputParams(gpio_pin=GPIO_PinNumber,gpio_level=GPIO_Level)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.write(Write_params)
        
    def GPIO_Read (self,GPIO_PinNumber):
        #create a valid request message
        Read_params = GPIO_write_pb2.PinNumber(gpio_pin=GPIO_PinNumber)
        #make the call
        GPIO_reading = stub.read(Read_params)
        return GPIO_reading.gpio_pin_level

    def GPIO_SetPullUpDown (self,GPIO_PinNumber,GPIO_PullUpDown):
        #create a valid request message
        GPIO_PUD = GPIO_write_pb2.GPIO_PUD(gpio_pin=GPIO_PinNumber,gpio_pud=GPIO_PullUpDown)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.set_pull_up_down(GPIO_PUD)
        
    ## PWM functions ##
    def PWM_Configure (self,GPIO_PinNumber,PWM_Freq ,PWM_Duty):
        #create a valid request message
        PWM_Params = GPIO_write_pb2.PWM_params(gpio_pin=GPIO_PinNumber,PWMfreq=PWM_Freq , PWMduty=PWM_Duty)
        #make the call
        PWM_status = stub.hardware_PWM(PWM_Params)
        return PWM_status.PWM_return
        
    def PWM_InputInit (self,PWM_InputPin):
        #create a valid request message
        PWM_Pin = GPIO_write_pb2.PWM_Pin(pwm_pin = PWM_InputPin)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.PWM_InputInit(PWM_Pin)
        
    def PWM_GetDutyCycle (self,PWM_InputPin):
        #create a valid request message
        PWM_Pin = GPIO_write_pb2.PWM_Pin(pwm_pin = PWM_InputPin)
        #make the call
        Reading = stub.PWM_GetDutyCycle(PWM_Pin)
        return Reading.reading
        
    def PWM_GetFrequency (self,PWM_InputPin):
        #create a valid request message
        PWM_Pin = GPIO_write_pb2.PWM_Pin(pwm_pin = PWM_InputPin)
        #make the call
        Reading = stub.PWM_GetFrequency(PWM_Pin)
        return Reading.reading
    
    ## Serial functions ##
    def Serial_Open (self,TTY_Name, BaudRate ,SerialFlags):
        #create a valid request message
        SerialOpenParams = GPIO_write_pb2.SerialOpenParams(tty=TTY_Name,baud=BaudRate,ser_flags=SerialFlags)
        #make the call
        SerialHandleReturn = stub.serial_open(SerialOpenParams)
        return SerialHandleReturn.SerialHandle
    
    def Serial_Close (self,Handle):
        #create a valid request message
        SerialCloseParams = GPIO_write_pb2.SerialHandleMessage(SerialHandle = Handle)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.serial_close(SerialCloseParams)
        
    def Serial_Readbyte (self,Handle):
        #create a valid request message
        SerialReadByteParams = GPIO_write_pb2.SerialHandleMessage(SerialHandle = Handle)
        #make the call
        SerialByte = stub.serial_read_byte(SerialReadByteParams)
        return SerialByte.ReadByte
    
    def Serial_WriteByte (self,Handle,ByteVal):
        #create a valid request message
        SerialWriteByteParams = GPIO_write_pb2.SerialWriteByteParams(handle = Handle, byte_val=ByteVal)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.serial_write_byte(SerialWriteByteParams)
        
    def Serial_Write (self,Handle,Data):
        #create a valid request message
        SerialWriteParams = GPIO_write_pb2.SerialWriteParams(handle = Handle, data=Data)
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.serial_write(SerialWriteParams)
    
    def Serial_DataAvailable (self,Handle):
        #create a valid request message
        SerialDataAvailableParams = GPIO_write_pb2.SerialHandleMessage(SerialHandle = Handle)
        #make the call
        NumberofBytes = stub.serial_data_available(SerialDataAvailableParams)
        return NumberofBytes.NumofBytes
        
    def PIGPIO_Stop (self):
        #create an empty message
        EmptyResp = GPIO_write_pb2.Empty()
        #make the call
        EmptyResp = stub.stop(EmptyResp)
        
        
        
        