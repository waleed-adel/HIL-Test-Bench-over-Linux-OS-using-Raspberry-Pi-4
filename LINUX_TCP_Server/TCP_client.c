/*********************************************************
 * @defgroup   TCP_CLIENT TCP client					  
 *														
 * @brief      This file implements TCP client.
 *
 * @author     BENCH,PLEASE! TEAM
 * @date       June 1st,2020
 *********************************************************/
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "TCP_client.h"
#include "Frame.h"



/*<--------------- SERVER INITIALIZATION GLOBAL VARIABLES----------->*/
uint32_t ClientSocket;
struct sockaddr_in servaddr;
uint32_t slen = sizeof(servaddr);
/**------------------------------------------------------------------**/

/*<------------- GLOBAL SEND AND RECEIVE BUFFERS & VARIABLES--------->*/

uint8_t recvBuf[STATUS_SIZE];
uint8_t RxFrameHeaderBuffer[100];
uint8_t RxFrameDataBuffer[100];
uint16_t Iterator = 0;
uint8_t Status = NACK;
uint8_t ConnectionStatus = CONNECTION_OK;
/**------------------------------------------------------------------**/

/*<----------------- FRAME RELATED GLOBALE VARIABLES------------------>*/
uint8_t DIO_Data[DIO_DATA_SIZE] = {45, 120, 78, 42, 11};
uint8_t UZART_Data[UZART_DATA_SIZE] = {23, 10, 117};
uint8_t *Frame = NULL;
uint32_t FrameTotalSize = 0;

typedef struct
{
	uint8_t MessageType;
	uint8_t MessageSize;
}MessageInfo;

FrameHeader_t FrameHeader = 
{
	.Signature 		= 	SIGNATURE,	
	.NumOfCommands	= 	NUM_OF_CMD,
	.TotalDataSize	= 	0
};
/**------------------------------------------------------------------**/

/**--------------------------MAIN FUNCTION----------------------------*/

void main (void)
{
	TCP_ClientConnect();
	TCP_ClientSend(MESSAGE_ACK);
	TCP_ClientReceive(MESSAGE_ACK);
	TCP_ClientDisconnect();
}
/**------------------------------------------------------------------**/

uint8_t TCP_ClientConnect(void)
{
	
	//create socket
	if ((ClientSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
	{
		perror("socket() Failed");
		return CONNECTION_SOCKET_ERROR;
	}
		
	//setup address structure
	memset((char *) &servaddr, 0, sizeof(struct sockaddr_in ));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(PORT);
	servaddr.sin_addr.s_addr = inet_addr(SERVER); 
	
	if (connect(ClientSocket, (struct sockaddr *) &servaddr, sizeof(servaddr)) < 0 )
	{
		perror("connect() failed");
		return CONNECTION_SOCKET_ERROR;
	}
	else
	{
		printf("connect() OK! \nLet the communications begin \n ");
	}

	return CONNECTION_OK;
}


void TCP_ClientSend(uint8_t MessageType)
{
	switch(MessageType)
	{
		case MESSAGE_ACK:
			Status = ACK;
			if (send(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0) < 0)
			{
				perror("send() failed ");
				//exit(EXIT_FAILURE);
			}
			else
			{
				printf("Sent Hopefully\n");
			}
			break;

		case MESSAGE_NACK:
			Status = NACK;
			if (send(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0) < 0)
			{
				perror("send() failed");
			}
			else
			{
				printf("Sent Hopefully\n");
			}
			
			break;
		case MESSAGE_HEADER_FRAME:
			if (send(ClientSocket, (uint8_t *)&FrameHeader, sizeof(FrameHeader_t), 0) < 0 )
			{
				perror("send() failed");
			}
			else
			{
				printf("Sent Hopefully\n");
			}
			break;
		case MESSAGE_DATA_FRAME:	
			if (send(ClientSocket, (uint8_t *)Frame, FrameHeader.TotalDataSize, 0) < 0)
			{
				perror("send() failed");
			}
			else
			{
				printf("Sent Hopefully\n");
			}
			break;
			
		default:
			printf("MESSAGE_TYPE_ERROR\n");
			break;
	}
}

uint8_t TCP_ClientReceive(uint8_t MessageType)
{
	uint8_t returnType = 0;
	
	switch(MessageType)
	{
		case MESSAGE_ACK:
		//try to receive some data, this is a blocking call
		if (recv(ClientSocket, (uint8_t *)recvBuf, STATUS_SIZE, 0) < 0)
		{
			perror("recv() failed");
		}
		printf("%X\n", recvBuf[0]);
		if( recvBuf[0] == ACK)
		{
			returnType = MESSAGE_ACK;	
		}
		else
		{
			returnType = MESSAGE_NACK;
		}
		break;

		case MESSAGE_HEADER_FRAME:
			if (recv(ClientSocket, recvBuf, sizeof(FrameHeader_t), 0) < 0)
			{
				perror("recv() failed");
			}
			
			returnType = MESSAGE_HEADER_FRAME;
			break;
			
		case MESSAGE_DATA_FRAME:
			if (recv(ClientSocket, recvBuf, FrameHeader.TotalDataSize, 0) < 0)
			{
				perror("recv() failed");
			}
			
			returnType = MESSAGE_DATA_FRAME;
			break;
			
		default:
			printf("MESSAGE_TYPE_ERROR\n");
			break;
	}
	
	return returnType;
}

void TCP_ClientDisconnect(void)
{
	close(ClientSocket);
}

////////////////////////////////////////////FRAME APIS////////////////////////////////////////
void FRAME_Generate(uint8_t* DIO_Data, uint32_t DIO_DataSize , uint8_t* UART_Data, uint32_t UART_DataSize)
{
	uint16_t CMDIndex = 0;
	uint16_t DataIndex = 0;
	uint16_t FrameIndex = 0;
	
	FrameData_t FrameData[NUM_OF_CMD] = 
	{
		{
			.PeripheralID	= 	DIO_PERIPHERAL_ID,	
			.DataSize		= 	DIO_DataSize,		
			.PeripheralData	= 	DIO_Data
		},

		{
			.PeripheralID	= 	UZART_PERIPHERAL_ID,	
			.DataSize		= 	UART_DataSize,		
			.PeripheralData	= 	UART_Data
		}
	};
	
	FrameTotalSize = DIO_DataSize + UART_DataSize + (NUM_OF_CMD * PERIPH_HEADER_SIZE);
	FrameHeader.TotalDataSize = FrameTotalSize;
	Frame = (uint8_t *) calloc(FrameTotalSize, sizeof(uint8_t));
	
	for(CMDIndex = 0; CMDIndex < NUM_OF_CMD; CMDIndex++)
	{
		Frame[FrameIndex] = FrameData[CMDIndex].PeripheralID; //2 bytes
		FrameIndex += 2;
		Frame[FrameIndex] = FrameData[CMDIndex].DataSize; //2 bytes
		FrameIndex += 2;
		
		for(DataIndex = 0; DataIndex < FrameData[CMDIndex].DataSize; DataIndex++)
		{
			Frame[FrameIndex] = FrameData[CMDIndex].PeripheralData[DataIndex];
			FrameIndex++;
		}
	}
}

void FRAME_Print(void)
{
	uint16_t Iterator = 0;
	for(Iterator = 0; Iterator < FrameTotalSize; Iterator++)
	{
		printf("Frame-Byte[%d]: %d\n", Iterator, Frame[Iterator]);
	}
}


//////////////////////////////////////////////////////////////////////////


