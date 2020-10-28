/*
   pwm.c

   gcc -o pwm pwm.c -lpigpio -lrt -lpthread

   sudo ./pwm
*/

#include <stdio.h>
#include <stdint.h>
#include "pigpio.h"


#define PWM_INPUT		23
#define PWM_OUTPUT		18
#define ERROR_PIGPIO_INIT			1

static uint32_t rise_tick = 0;    // Pulse rise time tick value
static uint32_t On_Time = 0;  // Last measured pulse width (us)

static uint32_t falling_tick = 0;
static uint32_t Off_Time = 0;

// Callback function for measuring PWM input
void pwm_cbfunc(int user_gpio, int level, uint32_t tick)
 {
    if (level == 1) 
	{  
		// rising edge
        rise_tick = tick;
		Off_Time = tick - falling_tick;
    }
    else if (level == 0) 
	{  
		// falling edge
        On_Time = tick - rise_tick;  // TODO: Handle 72 min wrap-around
		falling_tick = tick;
    }
}

int main(void)
{	
	/* Setting up the libarary */
	if (gpioInitialise() < 0)
	{
		fprintf(stderr, "pigpio initialisation failed\n");
		return ERROR_PIGPIO_INIT;
	}
	
	/* Setting Pin Modes */
	gpioSetMode(PWM_INPUT, PI_INPUT);
	gpioSetMode(PWM_OUTPUT, PI_OUTPUT);
	
	/* 1 Hz .. 40% DutyCycle */
	gpioHardwarePWM(PWM_OUTPUT, 5, 400000);
	
	// Set up callback for PWM input 
    gpioSetAlertFunc(PWM_INPUT, pwm_cbfunc);

	while(1) 
	{
        //printf("PWM pulse width: %u\n", On_Time);
        
        printf("ON TIME: %d\n", On_Time);
        printf("OFF TIME: %d\n", Off_Time);
        printf("Duty Cycle: %f \n", ((On_Time * 100) / (On_Time + Off_Time) );
		printf("Frequency: %f\n", (1000000 / (On_Time+Off_Time));
        gpioDelay(500000);
    }
	
}


