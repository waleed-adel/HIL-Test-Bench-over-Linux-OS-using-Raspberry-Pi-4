/**
 *  @file client.c
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief PC Client Source File
 */

/* File includes */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "client.h"
#include "Frame.h"

/*****************************************************************************/
/************************** CLIENT GLOBAL VARIABLES **************************/
/*****************************************************************************/
/* Server socket structure */
struct sockaddr_in servaddr;

/* Server Socket Size */
uint32_t socketSize = sizeof(servaddr);

/* Client Socket Handler*/
uint32_t ClientSocket = 0;

/* Client Connection key to be verified by the server upon connection*/
uint32_t ConnectionKey = CONNECTION_KEY;

/* General Index Iterator */
uint16_t Iterator = 0;

/* Server Connection Status */
uint8_t Status = NACK;


/*****************************************************************************/
/************************** FRAME GLOBAL VARIABLES ***************************/
/*****************************************************************************/
/* Tx Data Frame */
uint8_t *Frame = NULL;
uint32_t FrameTotalSize = 0;

/* Serial Communication Frames */
/* General Frame holding data to be sent to server */
uint8_t *SerialFrame = NULL;
uint32_t SerialSize = 0;
uint8_t *UART_Frame = NULL;
uint32_t UART_FrameSize = 0;
uint8_t *SPI_CH1_Frame = NULL;
uint32_t SPI_CH1_FrameSize = 0;
uint8_t *SPI_CH2_Frame = NULL;
uint32_t SPI_CH2_FrameSize = 0;

/* General Frame holding data received from server */
uint8_t* SerialReturnBuffer = NULL;

/* A buffer holding the Readings to be passed to the GUI */
uint32_t *Rx_ReadingsFrame = NULL;

/* Frame holding data received from server */
uint8_t RxFrameDataBuffer[512];

/* Pointer used to deal with the Buffer of received data as a FrameData_t struct */
FrameData_t *RxFrameData = (FrameData_t *)RxFrameDataBuffer;

/* Frame Header sent to the server */
FrameHeader_t TxFrameHeader = 
{
	.Signature 			= 	SIGNATURE,	
	.NumOfPeripherals	= 	NUM_OF_PERIPH,
	.TotalDataSize		= 	0
};

/* Frame Header received from the server */
FrameHeader_t RxFrameHeader;


/*****************************************************************************/
/****************************** CLIENT INTERFACES ****************************/
/*****************************************************************************/

/**
 *  @name  UDP_ClientConnect
 *  @brief This API shall connect the client to server(RPi)
 *  
 *  @param [in] ServerIP:   Holds server's IP Address
 *  @param [in] ServerPort: Holds server's Port Address
 *  @return Connection Status 
 *  	Options: 
 *  		CONNECTION_WINSOCK_INIT_ERROR 	: Initialization of winsocket failed.
 *  		CONNECTION_SOCKET_ERROR 		: Error in Client's socket.
 *  		CONNECTION_OK					: Client connection successful.
 *  		CONENCTION_REQUEST_TIMEOUT		: Connection to server timeout.
 */
uint8_t UDP_ClientConnect(uint8_t* ServerIP, uint16_t ServerPort)
{
	/* Counter for number of timed out tries */
	uint8_t TimeoutCounter = 0;
	WSADATA wsa;
	
	/* Initialise winsock */
	printf("\nInitialising Winsock...\n");
	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
	{
		printf("Initialization Failed. Error Code : %d\n",WSAGetLastError());
		return CONNECTION_WINSOCK_INIT_ERROR;
	}
	printf("Initialised.\n");
	
	/* Creating socket */
	if ((ClientSocket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == SOCKET_ERROR)
	{
		printf("socket() Failed. Error Code : %d\n" , WSAGetLastError());
		return CONNECTION_SOCKET_ERROR;
	}

	/* Setup address structure */
	memset((char *) &servaddr, 0, sizeof(struct sockaddr_in ));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(ServerPort);
	servaddr.sin_addr.S_un.S_addr = inet_addr(ServerIP); 
	
	
	/* Send the connection key to server */
	UDP_ClientSend(MESSAGE_CONNECTION_KEY);
	
	while(TimeoutCounter < CONNECTION_TIMEOUT_COUNT)
	{
		printf("Trial: %d\n", TimeoutCounter);
		if(UDP_ClientReceive(MESSAGE_ACK) == MESSAGE_ACK)
		{
			printf("CONNECTION KEY ACCEPTED\n");
			TimeoutCounter = 0;
			return CONNECTION_OK;
		}
		else
		{
			printf("Connection Trial[%d] failed, Retrying......\n", TimeoutCounter);
			TimeoutCounter++;
			
			/* Re-send the connection key after failing */
			UDP_ClientSend(MESSAGE_CONNECTION_KEY);
		}
	}
	return CONENCTION_REQUEST_TIMEOUT;
}

/**
 *  @name  UDP_ClientSend
 *  @brief This API shall send a message to server.
 *  	
 *  @param [in] MessageType: Type of message being sent to the server.
 *  	Options:
 *  		MESSAGE_ACK				: Send an ACK message.					
 *          MESSAGE_NACK			: Send a NACK message.	
 *          MESSAGE_HEADER_FRAME	: Send a Frame Header message.	
 *          MESSAGE_DATA_FRAME		: Send a Frame Data message.
 *          MESSAGE_CONNECTION_KEY	: Send a Connection Key message.
 *          MESSAGE_UART			: Send an UART Data message.
 *          MESSAGE_SPI_CH1			: Send an SPI_CH1 Data message.
 *          MESSAGE_SPI_CH2			: Send an SPI_CH2 Data message.
 *          MESSAGE_SERIAL_SIZE		: Send a Serial Size message.
 *  
 *  @return void.
 */
void UDP_ClientSend(uint8_t MessageType)
{	
	switch(MessageType)
	{
		case MESSAGE_ACK:
			Status = ACK;
			if (sendto(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;

		case MESSAGE_NACK:
			Status = NACK;
			if (sendto(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		case MESSAGE_HEADER_FRAME:
			if (sendto(ClientSocket, (uint8_t *)&TxFrameHeader, sizeof(FrameHeader_t), 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		case MESSAGE_DATA_FRAME:	
			if (sendto(ClientSocket, (uint8_t *)Frame, TxFrameHeader.TotalDataSize, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		case MESSAGE_CONNECTION_KEY:	
			if (sendto(ClientSocket, (uint8_t *)&ConnectionKey, sizeof(uint32_t), 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		case MESSAGE_UART:
			if(UART_FrameSize > 0)
			{
				if (sendto(ClientSocket, (uint8_t *)UART_Frame, UART_FrameSize, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
				{
					printf("sendto() failed with error code : %d" , WSAGetLastError());
					exit(EXIT_FAILURE);
				}
			}
			break;
			
		case MESSAGE_SPI_CH1:	
			if (sendto(ClientSocket, (uint8_t *)SPI_CH1_Frame, SPI_CH1_FrameSize, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		case MESSAGE_SPI_CH2:	
			if (sendto(ClientSocket, (uint8_t *)SPI_CH2_Frame, SPI_CH2_FrameSize, 0, (struct sockaddr *)&servaddr, socketSize) == SOCKET_ERROR)
			{
				printf("sendto() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
			break;
			
		default:
			break;
	}
}

/**
 *  @name  UDP_ClientReceive
 *  @brief This API shall receive a message from server.
 *  
 *  @param [in] MessageType: Type of message received from server.
 *  	Options:
 *  		MESSAGE_ACK				: Receive an ACK message.					
 *          MESSAGE_NACK			: Receive a NACK message.	
 *          MESSAGE_HEADER_FRAME	: Receive a Frame Header message.	
 *          MESSAGE_DATA_FRAME		: Receive a Frame Data message.
 *          MESSAGE_CONNECTION_KEY	: Receive a Connection Key message.
 *          MESSAGE_UART			: Receive an UART Data message.
 *          MESSAGE_SPI_CH1			: Receive an SPI_CH1 Data message.
 *          MESSAGE_SPI_CH2			: Receive an SPI_CH2 Data message.
 *          MESSAGE_SERIAL_SIZE		: Receive a Serial Size message.
 *  
 *  @return Status of received message.
 *  	Options:
 *  		MESSAGE_ACK				: Received an ACK
 *  		MESSAGE_NACK            : Received an NACK
 *  		HEADER_VALID            : Received a valid Header Frame.
 *  		HEADER_INVALID          : Received an invalid Header Frame.
 *  		MESSAGE_DATA_FRAME      : Received an Data Frame.
 *  		MESSAGE_SERIAL_SIZE     : Received a Serial Size.
 *  		MESSAGE_UART			: Received an UART Frame.
 *			MESSAGE_SPI_CH1         : Received an SPI_CH1 Frame.
 *			MESSAGE_SPI_CH2         : Received an SPI_CH2 Frame.
 */
uint8_t UDP_ClientReceive(uint8_t MessageType)
{
	uint8_t returnType = 0;
	
	switch(MessageType)
	{
		case MESSAGE_ACK:
			memset(RxFrameDataBuffer, 0, STATUS_SIZE);
			if (recvfrom(ClientSocket, (uint8_t *)RxFrameDataBuffer, STATUS_SIZE, 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
			{
				printf("recvfrom() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}	
#if	(TRACE_PRINT_ENABLE == 1)			
			printf("ACKNOWLEDGMENT_STATUS: %d\n", RxFrameDataBuffer[0]);
#endif
			if(RxFrameDataBuffer[0] == ACK)
			{
				returnType = MESSAGE_ACK;	
			}
			else
			{
				returnType = MESSAGE_NACK;
			}
		break;

		case MESSAGE_HEADER_FRAME:
			memset(&RxFrameHeader, 0, sizeof(FrameHeader_t));
			if (recvfrom(ClientSocket, (uint8_t*)&RxFrameHeader, sizeof(FrameHeader_t), 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
			{
				printf("recvfrom() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}			
			if(RxFrameHeader.Signature == SIGNATURE)
			{
				returnType = HEADER_VALID;
			}
			else
			{
				returnType = HEADER_INVALID;
			}
#if	(TRACE_PRINT_ENABLE == 1)	
			for(Iterator = 0; Iterator < sizeof(FrameHeader_t); Iterator++)
			{
				printf("RX_HEADER_FRAME_BYTE[%d]: %d\n", Iterator, ((uint8_t*)&RxFrameHeader)[Iterator]);
			}
			printf("\n");
#endif
			break;
	
		case MESSAGE_DATA_FRAME:
			memset(RxFrameDataBuffer, 0, RxFrameHeader.TotalDataSize);
			if (recvfrom(ClientSocket, RxFrameDataBuffer, RxFrameHeader.TotalDataSize, 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
			{
				printf("recvfrom() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
#if	(TRACE_PRINT_ENABLE == 1)
			for(Iterator = 0; Iterator < RxFrameHeader.TotalDataSize; Iterator++)
			{
				printf("RX_DATA_FRAME_BYTE[%d]: %d\n", Iterator, RxFrameDataBuffer[Iterator]);
			}
			printf("\n");
#endif
			returnType = MESSAGE_DATA_FRAME;
			break;
		
		case MESSAGE_SERIAL_SIZE:
			if (recvfrom(ClientSocket, (uint8_t *)&SerialSize, sizeof(uint32_t), 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
			{
				printf("recvfrom() failed with error code : %d" , WSAGetLastError());
				exit(EXIT_FAILURE);
			}
#if	(TRACE_PRINT_ENABLE == 1)
			if(SerialSize > 0)
				printf("SerialSize: %d\n", SerialSize);
#endif			
			if(SerialSize != 0)
			{
				returnType = MESSAGE_SERIAL_SIZE;
			}
			else
			{
				returnType = MESSAGE_NACK;
			}
			break;
		
		case MESSAGE_UART:
			if(SerialSize > 0)
			{
				memset(RxFrameDataBuffer, 0, SerialSize);
				if (recvfrom(ClientSocket, RxFrameDataBuffer, SerialSize, 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
				{
					printf("recvfrom() failed with error code : %d" , WSAGetLastError());
					exit(EXIT_FAILURE);
				}
#if	(TRACE_PRINT_ENABLE == 1)
				for(Iterator = 0; Iterator < SerialSize; Iterator++)
				{
					printf("RX_UART_MESSAGE_BYTE[%d]: %d\n", Iterator, RxFrameDataBuffer[Iterator]);
				}
#endif
			}
			returnType = MESSAGE_UART;
			break;
			
		case MESSAGE_SPI_CH1:
			if(SerialSize > 0)
			{
				memset(RxFrameDataBuffer, 0, SerialSize);
				if (recvfrom(ClientSocket, RxFrameDataBuffer, SerialSize, 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
				{
					printf("recvfrom() failed with error code : %d" , WSAGetLastError());
					exit(EXIT_FAILURE);
				}
#if	(TRACE_PRINT_ENABLE == 1)				
				for(Iterator = 0; Iterator < SerialSize; Iterator++)
				{
					printf("RX_SPI_CH1_MESSAGE_BYTE[%d]: %d\n", Iterator, RxFrameDataBuffer[Iterator]);
				}
#endif
			}
			returnType = MESSAGE_SPI_CH1;
			break;
			
		case MESSAGE_SPI_CH2:
			if(SerialSize > 0)
			{
				memset(RxFrameDataBuffer, 0, SerialSize);
				if (recvfrom(ClientSocket, RxFrameDataBuffer, SerialSize, 0, (struct sockaddr *)&servaddr, &socketSize) == SOCKET_ERROR)
				{
					printf("recvfrom() failed with error code : %d" , WSAGetLastError());
					exit(EXIT_FAILURE);
				}
#if	(TRACE_PRINT_ENABLE == 1)				
				for(Iterator = 0; Iterator < SerialSize; Iterator++)
				{
					printf("RX_SPI_CH2_MESSAGE_BYTE[%d]: %d\n", Iterator, RxFrameDataBuffer[Iterator]);
				}
#endif
			}
			returnType = MESSAGE_SPI_CH2;
			break;

		default:
			printf("MESSAGE_TYPE_ERROR\n");
			break;
	}	
	return returnType;
}

/**
 *  @name  UDP_ClientDisconnect
 *  @brief This API shall disconnect the client from server.
 *  
 *  @return void.
 */
void UDP_ClientDisconnect(void)
{
	closesocket(ClientSocket);
	WSACleanup();
}


/*****************************************************************************/
/****************************** FRAME INTERFACES *****************************/
/*****************************************************************************/

/**
 *  @name  FRAME_GenerateDataFrame
 *  @brief This API shall generate the data frame to be sent to server.
 *  
 *  @param [in] DIO_Data		: DIO Data Buffer.
 *  @param [in] PWM_Config		: PWM Configurations Buffer.
 *  @param [in] UART_Config		: UART Configurations Buffer.
 *  @param [in] SPI_CH1_Config	: SPI_CH1 Configurations Buffer.
 *  @param [in] SPI_CH2_Config	: SPI_CH2 Configurations Buffer.
 *  
 *  @return void
 */
void FRAME_GenerateDataFrame(uint8_t* DIO_Data, uint8_t* PWM_Config, uint8_t* UART_Config, uint8_t* SPI_CH1_Config, uint8_t* SPI_CH2_Config)
{
	uint8_t PeripheralIndex = 0;
	
	/* Grouping for easier indexing */
	uint32_t local_PeripheralID[NUM_OF_PERIPH] = {DIO_PERIPHERAL_ID, PWM_PERIPHERAL_ID, UART_PERIPHERAL_ID, SPI_CH1_PERIPHERAL_ID, SPI_CH2_PERIPHERAL_ID};
	uint32_t local_PeripheralDataSize[NUM_OF_PERIPH] = {DIO_OUTPUT_PINS, PWM_CONFIG_SIZE, UART_CONFIG_SIZE, SPI_CH1_CONFIG_SIZE, SPI_CH2_CONFIG_SIZE};
	uint8_t *local_PeripheralData[NUM_OF_PERIPH] = {DIO_Data, PWM_Config, UART_Config, SPI_CH1_Config, SPI_CH2_Config};
	
	/* Alloctating the size of the frame to be sent */
	FrameTotalSize = 0;
	for(PeripheralIndex = 0; PeripheralIndex < NUM_OF_PERIPH; PeripheralIndex++)
		FrameTotalSize += local_PeripheralDataSize[PeripheralIndex];
	
	FrameTotalSize += PERIPH_INFO_SIZE;
	TxFrameHeader.TotalDataSize = FrameTotalSize;
	
	Frame = (uint8_t *) calloc(FrameTotalSize, sizeof(uint8_t));
	/* Pointer to hold the current position while transitioning in the frame */	
	uint8_t *Pointer = (uint8_t *)Frame;
	
	for(PeripheralIndex = 0; PeripheralIndex < NUM_OF_PERIPH; PeripheralIndex++)
	{
		/* Copying the Peripheral ID */
		memcpy(Pointer, &local_PeripheralID[PeripheralIndex], sizeof(uint32_t));
		Pointer += sizeof(uint32_t); /* Moving the pointer by "PeripheralID" size */
		/* Copying the DataSize */
		memcpy(Pointer, &local_PeripheralDataSize[PeripheralIndex], sizeof(uint32_t));
		Pointer += sizeof(uint32_t); /* Moving the pointer by "DataSize" size */
		/* Copying the Data */
		memcpy(Pointer, local_PeripheralData[PeripheralIndex], local_PeripheralDataSize[PeripheralIndex]);
		Pointer += local_PeripheralDataSize[PeripheralIndex]; /* Moving the pointer by to point on the next Peripheral */
	}
}

/**
 *  @name  FRAME_GenerateSerialFrame
 *  @brief This API shall generate the data to be sent over the selected serial channel.
 *  
 *  @param [in] Serial_Data		: Buffer holding serial data being sent.
 *  @param [in] Serial_DataSize	: Size of the serial data being sent
 *  @param [in] SerialIndex		: The Serial channel.
 *  	Options:
 *  		SERIAL_UART			: Generate UART Serial Frame.	
 *          SERIAL_SPI_CH1      : Generate SPI_CH1 Serial Frame.
 *          SERIAL_SPI_CH2      : Generate SPI_CH2 Serial Frame.
 *  
 *  @return void.
 */
void FRAME_GenerateSerialFrame(uint8_t *Serial_Data, uint32_t Serial_DataSize, uint8_t SerialIndex)
{
	uint32_t local_PeripheralID = 0;
	
	SerialFrame = (uint8_t *)calloc((PERIPH_ID_SIZE + Serial_DataSize), sizeof(uint8_t));
	memcpy((SerialFrame + PERIPH_ID_SIZE), Serial_Data, Serial_DataSize);
	
	switch(SerialIndex)
	{
		case SERIAL_UART:
			local_PeripheralID = UART_PERIPHERAL_ID;
			UART_FrameSize = Serial_DataSize;
			memcpy(SerialFrame, &local_PeripheralID, PERIPH_ID_SIZE);
			UART_Frame = SerialFrame;
			break;
		case SERIAL_SPI_CH1:
			local_PeripheralID = SPI_CH1_PERIPHERAL_ID;
			SPI_CH1_FrameSize = Serial_DataSize;
			memcpy(SerialFrame, &local_PeripheralID, PERIPH_ID_SIZE);
			SPI_CH1_Frame = SerialFrame;
			break;		
		case SERIAL_SPI_CH2:
			local_PeripheralID = SPI_CH2_PERIPHERAL_ID; 
			SPI_CH2_FrameSize = Serial_DataSize;
			memcpy(SerialFrame, &local_PeripheralID, PERIPH_ID_SIZE);
			SPI_CH2_Frame = SerialFrame;
			break;
		default:
			break;
	}
#if	(TRACE_PRINT_ENABLE == 1)
	printf("\n");
	for(Iterator = 0; Iterator < Serial_DataSize; Iterator++)
	{
		printf("Serial_Frame[%d]: %02X\n", Iterator, SerialFrame[Iterator]);
	}
#endif
}

/**
 *  @name  FRAME_SerialReturnFrame
 *  @brief This API shall send the received serial data from server to GUI.
 *  
 *  @return Buffer of serial data received.
 */
uint8_t *FRAME_SerialReturnFrame(void)
{
	SerialReturnBuffer = (uint8_t *)calloc(SerialSize + 1, sizeof(uint8_t));

	for (Iterator = 0; Iterator < SerialSize; Iterator++)
	{
#if (TRACE_PRINT_ENABLE == 1)
		printf("RX_FRAME_BUFFER_UART_BYTE[%d]: %02X\n", Iterator, RxFrameDataBuffer[Iterator]);
#endif
		if (RxFrameDataBuffer[Iterator] < 16)
		{
			sprintf(SerialReturnBuffer + Iterator, "%01X", RxFrameDataBuffer[Iterator]);
		}
		else
		{
			sprintf(SerialReturnBuffer + Iterator * 2, "%02X", RxFrameDataBuffer[Iterator]);
		}    
	}
#if (TRACE_PRINT_ENABLE == 1)
	printf("BUFFER: %s\n", SerialReturnBuffer);
#endif

	SerialSize = 0;
	return SerialReturnBuffer;
}

/**
 *  @name  FRAME_ReadingsFrame
 *  @brief This API shall return the (DIO - PWM) Readings from the server to GUI.
 *  
 *  @return Buffer holding the readings.
 */
uint32_t *FRAME_ReadingsFrame(void)
{
	uint32_t Rx_TotalDataSize = 0;
	
	/* A pointer to navigate through the Rx Buffer */
	uint8_t *TransitionPointer = NULL;
	
	/* A pointer to navigate through the Readings Buffer */
	uint8_t *ReadingPointer = NULL;

	TransitionPointer = (uint8_t *)RxFrameDataBuffer;

	/* Scanning for sizes */
	for(Iterator = 0; Iterator < NUM_RX_PERIPH; Iterator++)
	{
		Rx_TotalDataSize += ((FrameData_t *)TransitionPointer)->DataSize;
		TransitionPointer  += (PERIPH_HEADER_SIZE + ((FrameData_t *)TransitionPointer)->DataSize);
	}
	
	Rx_ReadingsFrame = (uint32_t *)calloc((Rx_TotalDataSize/sizeof(uint32_t)), sizeof(uint32_t));
	
	ReadingPointer = (uint8_t *)Rx_ReadingsFrame;
	
	/* Returning the pointer to the initial position of the Rx buffer */
	TransitionPointer = (uint8_t *)RxFrameDataBuffer;
	
	for(Iterator = 0; Iterator < NUM_RX_PERIPH; Iterator++)
	{
		memcpy(ReadingPointer, &(((FrameData_t *)TransitionPointer)->PeripheralData), ((FrameData_t *)TransitionPointer)->DataSize);
		TransitionPointer += (PERIPH_HEADER_SIZE + ((FrameData_t *)TransitionPointer)->DataSize);
		ReadingPointer += ((FrameData_t *)TransitionPointer)->DataSize;
	}

#if (TRACE_PRINT_ENABLE == 1)
	printf("\n\n/*************** PRINTING IN PARSING ***************\n\n");
	for(Iterator = 0; Iterator < 8; Iterator++)
		printf("Reading[%d]: %d\n", Iterator, Rx_ReadingsFrame[Iterator]);
	
	printf("\n\n");
#endif

	return Rx_ReadingsFrame;
}

/**
 *  @name  FRAME_FreeBuffer
 *  @brief This API shall free the dynamically allocated data.
 *  
 *  @param [in] Buffer: Takes the Frame index to be freed.
 *  	Options:
 *  		DATA_FRAME				: Free the Data Frame.	
 *          SERIAL_FRAME            : Free the Serial Frame.
 *          SERIAL_RETURN_FRAME     : Free the Serial Return Frame.
 *          READINGS_FRAME          : Free the Readings Frame.
 *   
 *  @return Return description
 */
void FRAME_FreeBuffer(uint8_t Buffer)
{
	switch(Buffer)
	{
		case DATA_FRAME				:	free(Frame);				break;
		case SERIAL_FRAME			:	free(SerialFrame);			break;
		case SERIAL_RETURN_FRAME	:	free(SerialReturnBuffer);	break;
		case READINGS_FRAME			:	free(Rx_ReadingsFrame);		break;
	}
}

/**
 *  @name  FRAME_Print
 *  @brief This API shall print the data frame sent to the server.
 *  
 *  @return void.
 */
void FRAME_Print(void)
{
#if (TRACE_PRINT_ENABLE == 1)
	for(Iterator = 0; Iterator < FrameTotalSize; Iterator++)
	{
		printf("Frame-Byte[%d]: %d\n", Iterator, Frame[Iterator]);
	}
#endif
}

