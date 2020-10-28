/*********************************************************
 * @defgroup   TCP_CLIENT TCP Server					  
 *														
 * @brief      This file implements TCP Server.
 *
 * @author     BENCH,PLEASE! TEAM
 * @date       June 1st,2020
 *********************************************************/
#include "TCP_server.h"
#include "Frame.h"

/*<--------------- SERVER INITIALIZATION GLOBAL VARIABLES----------->*/

uint32_t ServerSocket, ClientSocket;
struct sockaddr_in servaddr, cliaddr;
uint32_t len =sizeof(cliaddr);
/**------------------------------------------------------------------**/

/*<------------- GLOBAL SEND AND RECEIVE BUFFERS & VARIABLES--------->*/

uint8_t recvBuf[STATUS_SIZE];
uint8_t RxFrameHeaderBuffer[100];
uint8_t RxFrameDataBuffer[100];
uint8_t Status = NACK;
uint8_t ConnectionStatus = CONNECTION_OK;

/**------------------------------------------------------------------**/


/*<----------------- FRAME RELATED GLOBALE VARIABLES------------------>*/

uint8_t DIO_Data[DIO_DATA_SIZE] = {45, 120, 78, 42, 11};
uint8_t UZART_Data[UZART_DATA_SIZE] = {23, 10, 117};
uint8_t *Frame = NULL;
FrameHeader_t FrameHeader = 
{
	.Signature 		= 	SIGNATURE,	
	.NumOfCommands	= 	NUM_OF_CMD,
	.TotalDataSize	= 	0
};

/**-------------------------------------------------------------------**/

/**--------------------------MAIN FUNCTION----------------------------*/
void main(void)
{
	
	TCP_ServerConnect();
	printf("connected socket: %d\n",ClientSocket);
	TCP_ServerReceive(MESSAGE_ACK);
	TCP_ServerSend(MESSAGE_ACK);
	TCP_ServerDisconnect();

}
/**------------------------------------------------------------------**/

/*<------------------------FUNCTION DEFINITIONS---------------------->*/
uint8_t TCP_ServerConnect(void){

	//create socket
	if ((ServerSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
	{
		perror("socket() Failed \n");
		return CONNECTION_SOCKET_ERROR;
	}
		
	//setup address structure
	memset((char *) &servaddr, 0, sizeof(struct sockaddr_in ));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(PORT);
	servaddr.sin_addr.s_addr = inet_addr(SERVER); 
	
	if (bind(ServerSocket, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) 
    { 
		perror("bind() Failed ");
		return CONNECTION_BIND_ERROR;
    } 
    printf("Bind done\n");  

	if(listen(ServerSocket,5) < 0)
	{
		perror("Listen() Failed ");
		return CONNECTION_SOCKET_ERROR;
	}
	else
	{
		printf("WAITING... \n ");

	}
	if((ClientSocket = accept(ServerSocket, (struct sockaddr*)&cliaddr, &len)) < 0)
	{
		perror("accept() Failed ");
		return CONNECTION_SOCKET_ERROR;
	}
	else
	{
		printf("connected socket: %d\n",ClientSocket);
		printf("CONNECTION ACCEPTED... \n Let the communications begin \n");
	}

	return CONNECTION_OK;
}

void TCP_ServerSend(uint8_t MessageType)
{
	switch(MessageType)
	{
		case MESSAGE_ACK:
			Status = ACK;
			if (send(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0) < 0)
			{
				perror("send() Failed ");
			}
			break;

		case MESSAGE_NACK:
			Status = NACK;
			if (send(ClientSocket, (uint8_t *)&Status, STATUS_SIZE, 0) < 0)
			{
				perror("send() Failed ");
				//exit(EXIT_FAILURE);
			}
			break;
		case MESSAGE_HEADER_FRAME:
			if (send(ClientSocket, (uint8_t *)&FrameHeader, sizeof(FrameHeader_t), 0) < 0)
			{
				perror("send() Failed ");
			}
			break;
		case MESSAGE_DATA_FRAME:	
			if (send(ClientSocket, (uint8_t *)Frame, FrameHeader.TotalDataSize, 0) < 0)
			{
				perror("send() Failed ");
			}
			break;
			
		default:
			printf("MESSAGE_TYPE_ERROR");
			break;
	}
}

uint8_t TCP_ServerReceive(uint8_t MessageType)
{
	uint8_t returnType = 0;
	//clear the buffer by filling null, it might have previously received data	
	switch(MessageType)
	{
		case MESSAGE_ACK:
		//try to receive some data, this is a blocking call
		printf("connected socket: %d\n",ClientSocket);

		if (recv(ClientSocket, (uint8_t *)recvBuf, STATUS_SIZE, 0) < 0 )
		{
			printf("recv() failed");
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
				printf("recv() failed");
			}
			
			returnType = MESSAGE_HEADER_FRAME;
			break;
			
		case MESSAGE_DATA_FRAME:
		
			printf("FML2\n");
			if (recv(ClientSocket, recvBuf, FrameHeader.TotalDataSize, 0) < 0)
			{
				printf("recv() failed");
			}
			
			returnType = MESSAGE_DATA_FRAME;
			break;
			
		default:
			printf("MESSAGE_TYPE_ERROR\n");
			break;
	}
	
	return returnType;
}

void TCP_ServerDisconnect(void)
{
	close(ServerSocket);
}
