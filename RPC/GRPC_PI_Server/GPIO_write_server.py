
from concurrent import futures
import grpc
import pigpio
import PWM_Input

#contatin the request and response classes
import GPIO_write_pb2
#contains the generated client and server classes
import GPIO_write_pb2_grpc

pi1 = pigpio.pi()

#class that subclasses the generated class
class PI_GPIOServicer(GPIO_write_pb2_grpc.PI_GPIOServicer):

    ## GPIO functions ##
    def set_mode(self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.set_mode( request.gpio_pin,request.gpio_mode )
        return response

    def write(self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.write( request.gpio_pin,request.gpio_level )
        return response

    def read(self, request, context):
        response = GPIO_write_pb2.GPIO_Level()
        response.gpio_pin_level = pi1.read( request.gpio_pin )
        return response

    def set_pull_up_down(self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.set_pull_up_down( request.gpio_pin,request.gpio_pud )
        return response

    ## PWM functions ##
    def hardware_PWM (self, request, context):
        response = GPIO_write_pb2.PWM_Status()
        response.PWM_return = pi1.hardware_PWM( request.gpio_pin , request.PWMfreq ,request.PWMduty )
        return response

    def PWM_InputInit (self, request, context):
        response = GPIO_write_pb2.Empty()
        PWM_Input.CalculatePWM_Init(request.pwm_pin)
        return response

    def PWM_GetDutyCycle (self, request, context):
        response = GPIO_write_pb2.Reading()
        response.reading = PWM_Input.GetDutyCycle(request.pwm_pin)
        return response

    def PWM_GetFrequency (self, request, context):
        response = GPIO_write_pb2.Reading()
        response.reading = PWM_Input.GetFrequency(request.pwm_pin)
        return response


    ## Serial functions ##
    def serial_open (self, request, context):
        response = GPIO_write_pb2.SerialHandleMessage()
        response.SerialHandle = pi1.serial_open ( str(request.tty) , request.baud ,request.ser_flags )
        return response

    def serial_close (self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.serial_close ( request.SerialHandle )
        return response

    def serial_read_byte (self, request, context):
        response = GPIO_write_pb2.SerialByte()
        response.ReadByte = pi1.serial_read_byte ( request.SerialHandle )
        return response

    def serial_write_byte (self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.serial_write_byte ( request.handle , request.byte_val )
        return response

    def serial_write (self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.serial_write ( request.handle , request.data )
        return response

    def serial_data_available (self, request, context):
        response = GPIO_write_pb2.NumberofBytes()
        response.NumofBytes = pi1.serial_data_available ( request.handle )
        return response

    def stop (self, request, context):
        response = GPIO_write_pb2.Empty()
        pi1.stop()
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    GPIO_write_pb2_grpc.add_PI_GPIOServicer_to_server(PI_GPIOServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()