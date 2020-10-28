/**
 *  @file Application.c
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief Linux Server Application Source File
 */
 
/* File includes */
#include <pigpio.h>
#include "server.h"
#include "Frame.h"

/*****************************************************************************/
/********************* RASPBERRYPI CONFIGURATIONS MACROS *********************/
/*****************************************************************************/

/* RaspberryPi pigpio library init status macros */
#define PIGPIO_INIT_SUCCESSFUL			0
#define ERROR_PIGPIO_INIT				1
#define ERROR_PIGPIO_UART_INIT			2
#define ERROR_PIGPIO_SPI_CH1_INIT		3
#define ERROR_PIGPIO_SPI_CH2_INIT		4

/* RaspberryPi Server Pinout map */
/* DIO */
#define DIO_OUT1				24
#define DIO_OUT2				25
#define DIO_OUT3				26
#define DIO_OUT4				27
#define DIO_INPUT1				5
#define DIO_INPUT2				6
#define DIO_INPUT3				22
#define DIO_INPUT4				23
/* PWM */
#define PWM0_OUT				12
#define PWM1_OUT				13
#define PWM0_INPUT				0
#define PWM1_INPUT				1
/* UART */
#define UART_TX					14	
#define UART_RX					15
/* SPI */
/* SPI_CH1: Main SPI channel(0), SPI_CH2: Aux SPI channel(0) */
#define SPI_CH1_MOSI			10
#define SPI_CH1_MISO			9
#define SPI_CH1_SCLK			11
#define SPI_CH1_CE0				8
#define SPI_CH1_CE1				7
#define SPI_CH2_MOSI			20
#define SPI_CH2_MISO			19
#define SPI_CH2_SCLK			21
#define SPI_CH2_CE0				18
#define SPI_CH2_CE1				17
#define SPI_CH2_CE2				16
/* I2C */
#define I2C_SDA					2
#define I2C_SCLK				3

/* RaspberryPi Serial Ports configurations */
#define DEFAULT_UART_HANDLER	"/dev/ttyAMA0"
#define UART_FLAGS				0
#define UART_SIMPLEX_RX			((UART_Info.SerialStatus == 1))
#define UART_SIMPLEX_TX			((UART_Info.SerialStatus == 2))
#define UART_DUPLEX				((UART_Info.SerialStatus == 3))
#define UART_INIT_BAUDRATE		9600

#define SPI_CH1_CHANNEL			0
#define SPI_CH1_FLAGS			0x00
#define SPI_CH1_RX				((SPI_CH1_Info.SerialStatus == 1))
#define SPI_CH1_TX				((SPI_CH1_Info.SerialStatus == 2))
#define SPI_CH1_INIT_BAUDRATE	32000

#define SPI_CH2_CHANNEL			1
#define SPI_CH2_FLAGS			0x1E0
#define SPI_CH2_RX				((SPI_CH2_Info.SerialStatus == 1))
#define SPI_CH2_TX				((SPI_CH2_Info.SerialStatus == 2))
#define SPI_CH2_INIT_BAUDRATE	32000

/*****************************************************************************/
/************************ RASPBERRYPI TYPE DEFINITIONS ***********************/
/*****************************************************************************/

typedef struct
{
	/* Serial Communication Handler */
	int	SerialHandle;
	/* Serial Communication status whether enabled or not */
	uint32_t SerialStatus;
	/* Serial Communication Baudrate */
	uint32_t SerialBaudrate;
	/* Serial Communication Baudrate */
	uint32_t SerialDataSize;
	/* Serial Communication Tx Buffer */
	uint8_t *Tx_Buffer;
	/* Serial Communication Rx Buffer */
	uint8_t *Rx_Buffer;
}SerialInfo_t;

typedef struct
{
	/* Input Pulse rise time tick value */
	uint32_t RiseTick;
	/* Input Pulse On Time */
	uint32_t OnTime;
	/* Input Pulse fall time tick value */
	uint32_t FallingTick;
	/* Input Pulse Off Time */
	uint32_t OffTime;
	/* Input Pulse Duty Cycle */
	uint32_t DutyCycleReading;
	/* Input Pulse Frequency */
	uint32_t FrequencyReading;
}PWM_InputInfo_t;


/*****************************************************************************/
/******************** RASPBERRYPI FUNCTIONS DECLARATIONS *********************/
/*****************************************************************************/

static int gpio_Init(void);
static void gpio_DeInit(void);
/* Callback function for measuring PWM input */
static void PWM0_CallbackFn(int user_gpio, int level, uint32_t tick);
static void PWM1_CallbackFn(int user_gpio, int level, uint32_t tick);

static void RPi_ReadInputs(void);
static void RPi_WriteOutputs(void);


/*****************************************************************************/
/************************ RASPBERRYPI GLOBAL VARIABLES ***********************/
/*****************************************************************************/

/* External variable from server.c file showing the client availability */
extern uint8_t ClientAvailable;


/* Buffer holding the messages from the client */
static uint8_t FrameDataBuffer[FRAME_DATA_LEN] = {0};

/* RaspberryPi Serial Communication Buffers */
static uint8_t UART_Tx_Buffer[RX_BUFF_LEN] 		= {0};
static uint8_t UART_Rx_Buffer[RX_BUFF_LEN] 		= {0};
static uint8_t SPI_CH1_Tx_Buffer[RX_BUFF_LEN] 	= {0};
static uint8_t SPI_CH1_Rx_Buffer[RX_BUFF_LEN] 	= {0};
static uint8_t SPI_CH2_Tx_Buffer[RX_BUFF_LEN] 	= {0};
static uint8_t SPI_CH2_Rx_Buffer[RX_BUFF_LEN] 	= {0};


static SerialInfo_t UART_Info = {
	.SerialStatus 		= 0,
	.SerialBaudrate 	= UART_INIT_BAUDRATE,
	.SerialDataSize		= 0,
	.SerialHandle		= -1,	
	.Tx_Buffer			= UART_Tx_Buffer,
	.Rx_Buffer			= UART_Rx_Buffer
	
};

static SerialInfo_t SPI_CH1_Info = {
	.SerialStatus 		= 0,
	.SerialBaudrate 	= SPI_CH1_INIT_BAUDRATE,
	.SerialDataSize		= 0,
	.SerialHandle		= -1,	
	.Tx_Buffer			= SPI_CH1_Tx_Buffer,
	.Rx_Buffer			= SPI_CH1_Rx_Buffer
};

static SerialInfo_t SPI_CH2_Info = {
	.SerialStatus 		= 0,
	.SerialBaudrate 	= SPI_CH2_INIT_BAUDRATE,
	.SerialDataSize		= 0,
	.SerialHandle		= -1,	
	.Tx_Buffer			= SPI_CH2_Tx_Buffer,
	.Rx_Buffer			= SPI_CH2_Rx_Buffer
};

/* RaspberryPi Pulse Width Modulation Input Info */
static PWM_InputInfo_t PWM0 = {
	.RiseTick			= 0,
	.OnTime             = 0,
	.FallingTick        = 0,
	.OffTime            = 0,
	.DutyCycleReading   = 0,
	.FrequencyReading   = 0
};

static PWM_InputInfo_t PWM1 = {
	.RiseTick			= 0,
	.OnTime             = 0,
	.FallingTick        = 0,
	.OffTime            = 0,
	.DutyCycleReading   = 0,
	.FrequencyReading   = 0
};

/* RaspberryPi Readings Variables */
/* RaspberryPi Readings Header Frame */
static FrameHeader_t Readings_FrameHeader = {
	.Signature 			= 	SIGNATURE,	
	.NumOfPeripherals	= 	NUM_READINGS_PERIPH,
	.TotalDataSize		= 	TOTAL_READINGS_DATA_SIZE
};

/* RaspberryPi Readings Data Frames */
static FrameData_t DIO_ReadingsFrameData = {
	.PeripheralID		= DIO_PERIPHERAL_ID,
	.DataSize			= DIO_DATA_SIZE,
	.PeripheralData	    = 0
};
static FrameData_t PWM_ReadingsFrameData = {
	.PeripheralID		= PWM_PERIPHERAL_ID,
	.DataSize			= PWM_DATA_SIZE,
	.PeripheralData	    = 0
};
static uint32_t ReadingsFrame[(TOTAL_READINGS_DATA_SIZE/sizeof(uint32_t))] = {0};

/* Number of program runs */
static uint32_t ProgramCounter = 0;

/* General Iterator */
static uint32_t Iterator = 0;

int main(void) 
{ 	
	/*****************************************************************************/
	/************************ RASPBERRYPI LOCAL VARIABLES ************************/
	/*****************************************************************************/
	
	/* Server socket structure */
	struct sockaddr_in servaddr;
	/* Client socket structure */
	struct sockaddr_in cliaddr;
	/* Socket File Descriptor */
	uint32_t sockfd = 0;
	/* Socket structure size */
	uint32_t SocketSize = sizeof(struct sockaddr_in); 
	
	/* Server Data Transfer Status */
	uint8_t Status = NACK;
	/* Serial Data Receiving Counter */
	uint32_t Rx_Counter = 0;
	/* Received Client Frame Header */
	FrameHeader_t RxFrameHeader;
	
	/************************** Server Initializations **************************/
	/* Initializing pigpio and pin modes */
	if(gpio_Init() != PIGPIO_INIT_SUCCESSFUL)
		return ERROR_PIGPIO_INIT;
	
	//~ /* Running the RPC Pyhton Script in background */
	//~ printf("BEFORE INVOKE\n");
	//system("python ../RPC/GRPC_PI_Server/GPIO_write_server.py");
	//system(". ../Run_Server.sh");
	//~ execl("../RPC/GRPC_PI_Server", "sh", "-c", "python GPIO_write_server.py &", (char *)0);
	//~ printf("AFTER INVOKE\n");
	
	/* Initializing the UDP connection*/
	UDP_ServerInit(&sockfd, &servaddr, &cliaddr);
	
	/* RaspberryPi Application super loop */
	while(1)
	{
		/************************** Client Key Validation **************************/
		if(UDP_ValidateKey(&sockfd, &servaddr, &cliaddr) == 1)
		{
			while(ClientAvailable)
			{
				ProgramCounter++;
#if TRACE_PRINT_ENABLE == 1
				printf("\n***********Program Count: %d***********\n", ProgramCounter);
#endif				
				/********************* Receiving Data/Configs Frame from client *********************/
				/* Receiving Frame Header */
				if(ClientAvailable)
				{
					UDP_ServerReceive(&sockfd, (uint8_t*)&RxFrameHeader, &cliaddr, (uint32_t *)&SocketSize, sizeof(FrameHeader_t));
				}
				else
				{
					gpio_DeInit();
					break;
				}
#if TRACE_PRINT_ENABLE == 1				
				/* Printing header frame received from the PC */
				printf("RECEIVING RX HEADER\n");
				for(Iterator = 0; Iterator < sizeof(FrameHeader_t); Iterator++)
				{
					printf("Rx_FrameHeader_Byte[%d]: %d\n", Iterator, ((uint8_t*)&RxFrameHeader)[Iterator]);	
				}
#endif				
				/* Checking the client's signature */
				if(RxFrameHeader.Signature == SIGNATURE)
				{
					Status = ACK;
					/* Sending an ACK message to client */
					UDP_ServerSend(&sockfd, &Status, &cliaddr, SocketSize, STATUS_SIZE);
#if TRACE_PRINT_ENABLE == 1					
					printf("Sent Rx_FrameHeader Status: %d\n", Status);
					printf("Signature is Valid\n");
					printf("Total Data size(Rx_FrameHeader): %d\n", RxFrameHeader.TotalDataSize);		
#endif					
					/* Receiving Frame Data */
					if(ClientAvailable)
					{
						UDP_ServerReceive(&sockfd, (uint8_t *)FrameDataBuffer, &cliaddr, (uint32_t *)&SocketSize, RxFrameHeader.TotalDataSize);
					}
					else
					{
						gpio_DeInit();
						break;
					}
#if TRACE_PRINT_ENABLE == 1							
					/* Printing the FRAME Data received from PC */
					for(Iterator = 0; Iterator < RxFrameHeader.TotalDataSize; Iterator++)
					{
						printf("Rx_DataFrame_Byte[%d]: %d\n", Iterator, FrameDataBuffer[Iterator]);	
					}
#endif
					/********************* Updating RaspberryPi Outputs *********************/
					RPi_WriteOutputs();
				}
				else
				{
					Status = NACK;
					/* Sending a NACK message to client */
					UDP_ServerSend(&sockfd, &Status, &cliaddr, SocketSize, STATUS_SIZE);
#if TRACE_PRINT_ENABLE == 1	
					printf("Sent Rx_FrameHeader Status: %d\n", Status);
					printf("Signature Invalid\n");
#endif	
				}
				
				/********************* Sending Readings to the client *********************/
				/* Sending Readings Frame Header */
				UDP_ServerSend(&sockfd, (uint8_t *)&Readings_FrameHeader, &cliaddr, SocketSize, sizeof(FrameHeader_t));
				
#if TRACE_PRINT_ENABLE == 1	
				printf("/*********** SENDING DATA FROM RASPBERRY PI TO PC ***************/\n\n");
#endif			
				/* Wait on the Frame Header acknowledgement */
				if(ClientAvailable)
				{
					Status = NACK;
					UDP_ServerReceive(&sockfd, &Status, &cliaddr, (uint32_t *)&SocketSize, STATUS_SIZE);
				
				}
				else
				{
					gpio_DeInit();
					break;
				}
				
				if(Status == ACK)
				{
#if TRACE_PRINT_ENABLE == 1	
					printf("Received an ACK from PC to send RPi Readings\n");
#endif
					RPi_ReadInputs();
					
					/* Sending Readings Frame Data */
					UDP_ServerSend(&sockfd, (uint8_t*)ReadingsFrame, &cliaddr, SocketSize, Readings_FrameHeader.TotalDataSize);
#if TRACE_PRINT_ENABLE == 1			
					printf("DATA FRAME SENT: \n");
					for(Iterator = 0; Iterator < (Readings_FrameHeader.TotalDataSize/sizeof(uint32_t)); Iterator++)
					{
						printf("Tx_FrameData_Byte[%d]: %d\n", Iterator, ReadingsFrame[Iterator]);
					}
#endif
				}
				else
				{
#if TRACE_PRINT_ENABLE == 1
					printf("Received an NACK from PC on sending the RPi Readings\n");
#endif
				}
				
				/**************************** Setting Up Communication Protocols ****************************/

				/******************************************* UART *******************************************/

				/* Opening the UART Serial Port */
				UART_Info.SerialHandle = serOpen(DEFAULT_UART_HANDLER, UART_Info.SerialBaudrate, UART_FLAGS);
				/* Check whether the UART Serial Port is opened or not */
				if(UART_Info.SerialHandle < 0)
				{
					fprintf(stderr, "UART Serial port initialisation failed\n");
					return ERROR_PIGPIO_UART_INIT;	
				}
#if TRACE_PRINT_ENABLE == 1
				printf("OPENED HANDLER UART: %d\n", UART_Info.SerialHandle);
#endif
				/* Check whether the UART Tx is enabled or not */
				if(UART_SIMPLEX_TX || UART_DUPLEX)
				{
					/* Check whether there's data other than the Peripheral ID or not */
					if(UART_Info.SerialDataSize > PERIPH_ID_SIZE)
					{
						if(ClientAvailable)
						{
							/* Receiving Data from PC to be sent over UART (Close Loop) */
							UDP_ServerReceive(&sockfd, UART_Info.Tx_Buffer, &cliaddr, (uint32_t *)&SocketSize, UART_Info.SerialDataSize);
#if TRACE_PRINT_ENABLE == 1			
							for(Iterator = 0; Iterator < UART_Info.SerialDataSize ; Iterator++)
							{
								printf("SERIAL_RX[%d]: %02X\n", Iterator, UART_Info.Tx_Buffer[Iterator]);
							}
#endif
							/* Sending data over UART */
							serWrite(UART_Info.SerialHandle, (char *)UART_Info.Tx_Buffer, UART_Info.SerialDataSize);		
						}
						else
						{
							gpio_DeInit();
							break;
						}			
					}
					/* Delay required here for the Rx to sense the data on its buffer (100msec is an enough dummy value) */
					gpioDelay(100000); //100msec
				}
				
				/* Check whether the UART Rx is enabled or not */
				if(UART_SIMPLEX_RX || UART_DUPLEX)
				{
					/* Re-setting the Serial Data Receiving Counter */
					Rx_Counter = 0;
					/* Reading received data untill the buffer is empty */
					while(serDataAvailable(UART_Info.SerialHandle) > 0)
					{
						UART_Info.Rx_Buffer[Rx_Counter] = serReadByte(UART_Info.SerialHandle);
						Rx_Counter++;
					}
					
#if TRACE_PRINT_ENABLE == 1	
					if(Rx_Counter > 0)	
						printf("Rx_Counter Value: %d\n\n", Rx_Counter);				
					for(Iterator = 0; Iterator < Rx_Counter; Iterator++)
					{
						printf("UART_Rx_BUFFER[%d]: %d\n", Iterator, UART_Info.Rx_Buffer[Iterator]);
					}
#endif			
					/* Sending the size of Data Received over UART to the client */
					UDP_ServerSend(&sockfd, (uint8_t*)&Rx_Counter, &cliaddr, SocketSize, sizeof(uint32_t));
					/* Sending the Data Received over UART back to the client to be presented on GUI if size more than 0 */
					if(Rx_Counter > 0)
					{
						UDP_ServerSend(&sockfd, (uint8_t*)UART_Info.Rx_Buffer, &cliaddr, SocketSize, UART_Info.SerialDataSize);
					}
				}
				/* Closing the UART Serial Port */
				if(UART_Info.SerialHandle >= 0)
				{
#if TRACE_PRINT_ENABLE == 1
					printf("CLOSING HANDLER UART: %d\n", UART_Info.SerialHandle);
#endif		
					serClose(UART_Info.SerialHandle);
					UART_Info.SerialHandle = -1;
				}			
				
				/**************************************** SPI_CH1 ****************************************/
				/* Opening the SPI_CH1 Serial Port */
				SPI_CH1_Info.SerialHandle = spiOpen(SPI_CH1_CHANNEL, SPI_CH1_Info.SerialBaudrate, SPI_CH1_FLAGS);
				if(SPI_CH1_Info.SerialHandle < 0)
				{
					fprintf(stderr, "SPI_CH1 port initialisation failed\n");
					return ERROR_PIGPIO_SPI_CH1_INIT;	
				}
#if TRACE_PRINT_ENABLE == 1
				printf("OPENED HANDLER SPI_CH1: %d\n", SPI_CH1_Info.SerialHandle);
#endif
				/* Check whether the SPI is enabled or not */
				if(SPI_CH1_RX || SPI_CH1_TX)
				{
					/* Re-setting the Serial Data Receiving Counter */
					Rx_Counter = 0;
					/* Check whether there's data other than the Peripheral ID or not */
					if(SPI_CH1_Info.SerialDataSize > PERIPH_ID_SIZE)
					{
						if(ClientAvailable)
						{
							/* Receiving Data from PC to be sent over SPI_CH1 (Close Loop) */
							UDP_ServerReceive(&sockfd, SPI_CH1_Info.Tx_Buffer, &cliaddr, (uint32_t *)&SocketSize, SPI_CH1_Info.SerialDataSize);
#if TRACE_PRINT_ENABLE == 1	
							for(Iterator = 0; Iterator < SPI_CH1_Info.SerialDataSize ; Iterator++)
							{
								printf("SPI_CH1_TX_BUFFER[%d]: %02X\n", Iterator, SPI_CH1_Info.Tx_Buffer[Iterator]);
							}
#endif
							/* Exchanging Data over SPI_CH1 */
							spiXfer(SPI_CH1_Info.SerialHandle, (char *)SPI_CH1_Info.Tx_Buffer, (char *)SPI_CH1_Info.Rx_Buffer, SPI_CH1_Info.SerialDataSize);
#if TRACE_PRINT_ENABLE == 1								
							for(Iterator = 0; Iterator < SPI_CH1_Info.SerialDataSize ; Iterator++)
							{
								printf("SPI_CH1_RX_BUFFER[%d]: %02X\n", Iterator, SPI_CH1_Info.Rx_Buffer[Iterator]);
							}
#endif					
							/* Sending the size of Data Received over SPI_CH1 to the client */							
							UDP_ServerSend(&sockfd, (uint8_t*)&SPI_CH1_Info.SerialDataSize, &cliaddr, SocketSize, sizeof(uint32_t));
							
							/* Sending Data Received over SPI_CH1 back to the client to be presented on GUI if size more than 0 */
							UDP_ServerSend(&sockfd, (uint8_t*)SPI_CH1_Info.Rx_Buffer, &cliaddr, SocketSize, SPI_CH1_Info.SerialDataSize);
							
						}
						else
						{
							gpio_DeInit();
							break;
						}			
					}
					else
					{
						/* Sending Data Received over SPI_CH1 back to the client to be presented on GUI if size equal 0 */
						UDP_ServerSend(&sockfd, (uint8_t*)&Rx_Counter, &cliaddr, SocketSize, sizeof(uint32_t));
					}
				}
				/* Closing the SPI_CH1 Serial Port */
				if(SPI_CH1_Info.SerialHandle >= 0)
				{
#if TRACE_PRINT_ENABLE == 1
					printf("CLOSING HANDLER SPI_CH1: %d\n", SPI_CH1_Info.SerialHandle);
#endif
					spiClose(SPI_CH1_Info.SerialHandle);
					SPI_CH1_Info.SerialHandle = -1;
				}

				/**************************************** SPI_CH2 ****************************************/
				/* Opening the SPI_CH2 Serial Port */
				SPI_CH2_Info.SerialHandle = spiOpen(SPI_CH2_CHANNEL, SPI_CH2_Info.SerialBaudrate, SPI_CH2_FLAGS);
				if(SPI_CH2_Info.SerialHandle < 0)
				{
					fprintf(stderr, "SPI_CH2 port initialisation failed\n");
					return ERROR_PIGPIO_SPI_CH2_INIT;	
				}
#if TRACE_PRINT_ENABLE == 1
				printf("OPENED HANDLER SPI_CH2: %d\n", SPI_CH2_Info.SerialHandle);
#endif
				/* Check whether the SPI is enabled or not */
				if(SPI_CH2_RX || SPI_CH2_TX)
				{
					/* Re-setting the Serial Data Receiving Counter */
					Rx_Counter = 0;
					/* Check whether there's data other than the Peripheral ID or not */
					if(SPI_CH2_Info.SerialDataSize > PERIPH_ID_SIZE)
					{
						if(ClientAvailable)
						{

							/* Receiving Data from PC to be sent over SPI_CH2 (Close Loop) */
							UDP_ServerReceive(&sockfd, SPI_CH2_Info.Tx_Buffer, &cliaddr, (uint32_t *)&SocketSize, SPI_CH2_Info.SerialDataSize);
#if TRACE_PRINT_ENABLE == 1	
							for(Iterator = 0; Iterator < SPI_CH2_Info.SerialDataSize ; Iterator++)
							{
								printf("SPI_CH2_TX_BUFFER[%d]: %02X\n", Iterator, SPI_CH2_Info.Tx_Buffer[Iterator]);
							}
#endif
							/* Exchanging Data over SPI_CH2 */
							spiXfer(SPI_CH2_Info.SerialHandle, (char *)SPI_CH2_Info.Tx_Buffer, (char *)SPI_CH2_Info.Rx_Buffer, SPI_CH2_Info.SerialDataSize);
#if TRACE_PRINT_ENABLE == 1								
							for(Iterator = 0; Iterator < SPI_CH2_Info.SerialDataSize ; Iterator++)
							{
								printf("SPI_CH2_RX_BUFFER[%d]: %02X\n", Iterator, SPI_CH2_Info.Rx_Buffer[Iterator]);
							}
#endif		
							/* Sending the size of Data Received over SPI_CH2 to the client */	
							UDP_ServerSend(&sockfd, (uint8_t*)&SPI_CH2_Info.SerialDataSize, &cliaddr, SocketSize, sizeof(uint32_t));
							
							/* Sending Data Received over SPI_CH2 back to the client to be presented on GUI if size more than 0 */
							UDP_ServerSend(&sockfd, (uint8_t*)SPI_CH2_Info.Rx_Buffer, &cliaddr, SocketSize, SPI_CH2_Info.SerialDataSize);
							
						}
						else
						{
							gpio_DeInit();
							break;
						}			
					}
					else
					{
						/* Sending Data Received over SPI_CH2 back to the client to be presented on GUI if size equal 0 */
						UDP_ServerSend(&sockfd, (uint8_t*)&Rx_Counter, &cliaddr, SocketSize, sizeof(uint32_t));
					}
				}
				/* Closing the SPI_CH2 Serial Port */
				if(SPI_CH2_Info.SerialHandle >= 0)
				{
#if TRACE_PRINT_ENABLE == 1
					printf("CLOSING HANDLER SPI_CH2: %d\n", SPI_CH2_Info.SerialHandle);
#endif
					spiClose(SPI_CH2_Info.SerialHandle);
					SPI_CH2_Info.SerialHandle = -1;
				}
			}
		}
	}
	
	/*************************** Disconnecting the UDP connection *********************/
	UDP_ServerDisconnect(&sockfd);

	return 0;
}

/**
 *  @name  gpio_Init
 *  @brief This function shall initialize RPi GPIO.
 *  
 *  @return State of initialization.
 *  	Options:
 *  		PIGPIO_INIT_SUCCESSFUL		: Initialization sucessful.	
 *          ERROR_PIGPIO_INIT			: Library Initialization failure.
 */
static int gpio_Init(void)
{
	/************************************ Initializations ************************************/
	/* pigpio Library Initialization */
	if (gpioInitialise() < 0)
	{
		fprintf(stderr, "pigpio initialisation failed\n");
		return ERROR_PIGPIO_INIT;
	}

	/* Setting Pin Modes */
	gpioSetMode(DIO_OUT1, PI_OUTPUT);
	gpioSetMode(DIO_OUT2, PI_OUTPUT);
	gpioSetMode(DIO_OUT3, PI_OUTPUT);
	gpioSetMode(DIO_OUT4, PI_OUTPUT);
	
	gpioSetMode(PWM0_OUT, PI_OUTPUT);
	gpioSetMode(PWM1_OUT, PI_OUTPUT);

	gpioSetMode(DIO_INPUT1, PI_INPUT);
	gpioSetMode(DIO_INPUT2, PI_INPUT);
	gpioSetMode(DIO_INPUT3, PI_INPUT);
	gpioSetMode(DIO_INPUT4, PI_INPUT);

	gpioSetMode(PWM0_INPUT, PI_INPUT);
	gpioSetMode(PWM1_INPUT, PI_INPUT);
	
	/* Set up callbacks for PWM input */
	gpioSetAlertFunc(PWM0_INPUT, PWM0_CallbackFn);
	gpioSetAlertFunc(PWM1_INPUT, PWM1_CallbackFn);

	return PIGPIO_INIT_SUCCESSFUL;
}

/**
 *  @name  gpio_DeInit
 *  @brief This function shall de-initialize RPi GPIO.
 *
 *  @return void.
 */
static void gpio_DeInit(void)
{
	/* Re-setting the program counter */
	ProgramCounter = 0;
	//gpioTerminate();
}

/**
 *  @name  PWM0_CallbackFn
 *  @brief This function shall set the call back form PWM0 input.
 *  
 *  @param [in] user_gpio	: PWM0 Input Pin.
 *  @param [in] level		: PWM0 Pin Level at interrupt.
 *  @param [in] tick		: Tick Value at interrupt.
 *  
 *  @Note:	Tick value will wrap-around every 72 min.
 *  @return void.
 */
static void PWM0_CallbackFn(int user_gpio, int level, uint32_t tick)
 {
    if (level == 1) /* Rising edge */
	{  
        PWM0.RiseTick = tick;
		PWM0.OffTime = tick - PWM0.FallingTick;
    }
    else if (level == 0) /* Falling edge */
	{  
        PWM0.OnTime = tick - PWM0.RiseTick;
		PWM0.FallingTick = tick;
    }
}

/**
 *  @name  PWM1_CallbackFn
 *  @brief This function shall set the call back form PWM1 input.
 *  
 *  @param [in] user_gpio	: PWM1 Input Pin.
 *  @param [in] level		: PWM1 Pin Level at interrupt.
 *  @param [in] tick		: Tick Value at interrupt.
 *  
 *  @Note:	Tick value will wrap-around every 72 min.
 *  @return void.
 */
static void PWM1_CallbackFn(int user_gpio, int level, uint32_t tick)
 {
    if (level == 1) /* Rising edge */
	{  
        PWM1.RiseTick = tick;
		PWM1.OffTime = tick - PWM1.FallingTick;
    }
    else if (level == 0) /* Falling edge */
	{  
        PWM1.OnTime = tick - PWM1.RiseTick;
		PWM1.FallingTick = tick;
    }
}

/**
 *  @name  RPi_ReadInputs
 *  @brief This function shall read DIO and PWM readings and store them to the Readings frame.
 *  
 *  @return void.
 */
static void RPi_ReadInputs(void)
{
#if TRACE_PRINT_ENABLE == 1	
	printf("ON_TIME1: %d\t OFF_TIME1: %d\n", PWM0.OnTime, PWM0.OffTime);
#endif
	if((PWM0.OnTime == 0) && (PWM0.OffTime == 0))
	{
		PWM0.DutyCycleReading = 0;
		PWM0.FrequencyReading = 0;
	}
	else
	{
		PWM0.DutyCycleReading = ((PWM0.OnTime * 100) / (PWM0.OnTime+PWM0.OffTime));
		PWM0.FrequencyReading = (1000000 / (PWM0.OnTime+PWM0.OffTime)) ;
	}
#if TRACE_PRINT_ENABLE == 1	
	printf("PWM0.DutyCycleReading: %d\tPWM0.FrequencyReading: %d\n", PWM0.DutyCycleReading, PWM0.FrequencyReading);
	printf("ON_TIME2: %d\t OFF_TIME2: %d\n", PWM1.OnTime, PWM1.OffTime);
#endif
	if((PWM1.OnTime == 0) && (PWM1.OffTime == 0))
	{
		PWM1.DutyCycleReading = 0;
		PWM1.FrequencyReading = 0;
	}
	else
	{
		PWM1.DutyCycleReading = ((PWM1.OnTime * 100)/ (PWM1.OnTime+PWM1.OffTime)) ;
		PWM1.FrequencyReading = ((1000000 / (PWM1.OnTime+PWM1.OffTime))) ;
	}
#if TRACE_PRINT_ENABLE == 1	
	printf("PWM1.DutyCycleReading: %d\tPWM1.FrequencyReading: %d\n", PWM1.DutyCycleReading, PWM1.FrequencyReading);
#endif
	/* Clearing the Readings Frame before re-assigning the readings */
	memset(ReadingsFrame, 0, TOTAL_READINGS_DATA_SIZE);
	
	/* Assigning the readings (aligned to 4 bytes) */
	ReadingsFrame[0] = DIO_ReadingsFrameData.PeripheralID;
	ReadingsFrame[1] = DIO_ReadingsFrameData.DataSize;
	ReadingsFrame[2] = gpioRead(DIO_INPUT1);
	ReadingsFrame[3] = gpioRead(DIO_INPUT2);
	ReadingsFrame[4] = gpioRead(DIO_INPUT3);
	ReadingsFrame[5] = gpioRead(DIO_INPUT4);
	ReadingsFrame[6] = PWM_ReadingsFrameData.PeripheralID;
	ReadingsFrame[7] = PWM_ReadingsFrameData.DataSize;
	ReadingsFrame[8] = PWM0.DutyCycleReading;
	ReadingsFrame[9] = PWM0.FrequencyReading;
	ReadingsFrame[10] = PWM1.DutyCycleReading;
	ReadingsFrame[11] = PWM1.FrequencyReading;
}

/**
 *  @name  RPi_WriteOutputs
 *  @brief This function shall Set DIO and PWM values and apply serial communications configurations.
 *  
 *  @return void.
 */
static void RPi_WriteOutputs(void)
{
	uint32_t Frequency1 = 0;
	uint32_t DutyCycle1 = 0;
	uint32_t Frequency2 = 0;
	uint32_t DutyCycle2 = 0;
	
	/********************* DIO CHANNELS *********************/
	/* Updating DIO Outputs */
	gpioWrite(DIO_OUT1, FrameDataBuffer[8]);
	gpioWrite(DIO_OUT2, FrameDataBuffer[9]);
	gpioWrite(DIO_OUT3, FrameDataBuffer[10]);
	gpioWrite(DIO_OUT4, FrameDataBuffer[11]);
	
	/********************* PWM CHANNELS *********************/
	Frequency1 = *((uint32_t *)(FrameDataBuffer+20));
	DutyCycle1 = *((uint32_t *)(FrameDataBuffer+24));
	
	Frequency2 = *((uint32_t *)(FrameDataBuffer+28));
	DutyCycle2 = *((uint32_t *)(FrameDataBuffer+32));
#if TRACE_PRINT_ENABLE == 1
	printf("PWM Info read\n");
	printf("Frequency1: %d\tDutyCycle1: %d\n", Frequency1, DutyCycle1);
	printf("Frequency2: %d\tDutyCycle2: %d\n", Frequency2, DutyCycle2);
#endif
	/* Updating PWM Outputs */
	gpioHardwarePWM(PWM0_OUT, Frequency1, DutyCycle1);
	gpioHardwarePWM(PWM1_OUT, Frequency2, DutyCycle2);

	/********************* UART CHANNEL *********************/
	/* Updating UART Configurations */
	UART_Info.SerialStatus = *((uint32_t *)(FrameDataBuffer+44));
	UART_Info.SerialBaudrate = *((uint32_t *)(FrameDataBuffer+48));
	UART_Info.SerialDataSize = *((uint32_t *)(FrameDataBuffer+52));
#if TRACE_PRINT_ENABLE == 1
	printf("*********** UART Info ***********\n");
	printf("UART_SerialStatus: %d\n", UART_Info.SerialStatus);
	printf("UART_SerialBaudrate: %d\n", UART_Info.SerialBaudrate);	
	printf("UART_SerialDataSize: %d\n", UART_Info.SerialDataSize);
#endif

	/********************* SPI CHANNELS *********************/
	/* Updating SPI_CH1 Configurations */
	SPI_CH1_Info.SerialStatus = *((uint32_t *)(FrameDataBuffer+64));
	SPI_CH1_Info.SerialBaudrate = *((uint32_t *)(FrameDataBuffer+68));
	SPI_CH1_Info.SerialDataSize = *((uint32_t *)(FrameDataBuffer+72));
#if TRACE_PRINT_ENABLE == 1
	printf("*********** SPI_CH1 Info ***********\n");
	printf("SPI_CH1_SerialStatus: %d\n", SPI_CH1_Info.SerialStatus);
	printf("SPI_CH1_SerialBaudrate: %d\n", SPI_CH1_Info.SerialBaudrate);	
	printf("SPI_CH1_SerialDataSize: %d\n", SPI_CH1_Info.SerialDataSize);	
#endif
	/* Updating SPI_CH2 Configurations */
	SPI_CH2_Info.SerialStatus = *((uint32_t *)(FrameDataBuffer+84));
	SPI_CH2_Info.SerialBaudrate = *((uint32_t *)(FrameDataBuffer+88));
	SPI_CH2_Info.SerialDataSize = *((uint32_t *)(FrameDataBuffer+92));
#if TRACE_PRINT_ENABLE == 1
	printf("*********** SPI_CH2 Info ***********\n");
	printf("SPI_CH2_SerialStatus: %d\n", SPI_CH2_Info.SerialStatus);
	printf("SPI_CH2_SerialBaudrate: %d\n", SPI_CH2_Info.SerialBaudrate);	
	printf("SPI_CH2_SerialDataSize: %d\n", SPI_CH2_Info.SerialDataSize);					
#endif
}

