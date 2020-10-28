import pigpio
from GPIO_macros import *


Pins = []

# Pulse rise time tick value
rise_tick = []
#Tick at which falling edge happens
falling_tick = []
# Last measured pulse width (us)
On_Time = []
# Low time of the pulse
Off_Time = []

# Callback function for measuring PWM input
def pwm_cbfunc(PWM_Pin,level,tick):
    if (level == 1) :
        # rising edge
        rise_tick[Pins.index(PWM_Pin)] = tick;
        Off_Time[Pins.index(PWM_Pin)] = tick - falling_tick[Pins.index(PWM_Pin)];
    
    elif (level == 0): 
        # falling edge
        On_Time[Pins.index(PWM_Pin)] = tick - rise_tick[Pins.index(PWM_Pin)]
        falling_tick[Pins.index(PWM_Pin)] = tick

def CalculatePWM_Init(PWM_Pin):
    ## Setting up the libarary ##
    pi2 = pigpio.pi()
    
    pi2.set_mode (PWM_Pin, INPUT);
    
    # adding the pin number to the array
    Pins.append(PWM_Pin)
    
    #Adding entries for Rise,Fall ticks and On , off times
    rise_tick.append(0)
    falling_tick.append(0)
    On_Time.append(0)
    Off_Time.append(0)
    
    ## Set up callback for PWM input ##
    pi2.callback(PWM_Pin, EITHER_EDGE , pwm_cbfunc)

def GetDutyCycle (PWM_Pin):
    
    Desired_On_Time = On_Time[Pins.index(PWM_Pin)]
    Desired_Off_Time = Off_Time[Pins.index(PWM_Pin)]
    
    return ((Desired_On_Time * 100) / (Desired_On_Time + Desired_Off_Time) )

def GetFrequency (PWM_Pin):

    Desired_On_Time = On_Time[Pins.index(PWM_Pin)]
    Desired_Off_Time = Off_Time[Pins.index(PWM_Pin)]
    
    return (1000000 / (Desired_On_Time+Desired_Off_Time))
