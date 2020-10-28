 /**
 *  @file server.c
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief Linux Server Source File
 */

/* File includes */
#include "server.h"

/*****************************************************************************/
/************************** SERVER GLOBAL VARIABLES **************************/
/*****************************************************************************/

/* Client availability status */
uint8_t ClientAvailable = 0;

/*****************************************************************************/
/****************************** SERVER INTERFACES ****************************/
/*****************************************************************************/

/**
 *  @name  UDP_ServerInit
 *  @brief This API shall initialize the Linux UDP link.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  @param [in] servaddr	: Server Socket Address.
 *  @param [in] cliaddr		: Client Socket Address.
 *  
 *  @return void.
 */
void UDP_ServerInit(uint32_t *ServerSocket, struct sockaddr_in *servaddr, struct sockaddr_in *cliaddr)
{	
	struct timeval tv;
	tv.tv_sec 	= TIMEOUT_DURATION_SEC;
	tv.tv_usec 	= 0;

	/* Creating socket file descriptor */
    if ( (*ServerSocket = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) 
	{ 
        perror("socket creation failed"); 
        exit(EXIT_FAILURE); 
    } 
	
    printf("Socket created.\n");
    memset(servaddr, 0, sizeof(struct sockaddr_in)); 
    memset(cliaddr, 0, sizeof(struct sockaddr_in)); 
    
    /* Filling server information */
    servaddr->sin_family    	= AF_INET; // IPv4 
    servaddr->sin_addr.s_addr 	= inet_addr(SERVER); 
    servaddr->sin_port 			= htons(PORT); 
    
    setsockopt(*ServerSocket, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(struct timeval));
    
    /* Bind the socket with the server address */
    if ( bind(*ServerSocket, (const struct sockaddr *)servaddr, sizeof(struct sockaddr_in)) < 0 ) 
    { 
        perror("bind failed\n"); 
        exit(EXIT_FAILURE); 
    } 
    printf("Bind done\n"); 	
}

/**
 *  @name  UDP_ServerSend
 *  @brief This API shall send a message to the client.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  @param [in] Buffer		: Data buffer to be sent to the client.
 *  @param [in] cliaddr		: Client Socket Address.
 *  @param [in] SocketSize	: Size of socket structure.
 *  @param [in] FrameSize	: Size of the data buffer being sent.
 *  
 *  @return void.
 */
void UDP_ServerSend(uint32_t *ServerSocket, uint8_t* Buffer, struct sockaddr_in * cliaddr, uint32_t SocketSize, uint16_t FrameSize)
{
	sendto(*ServerSocket, Buffer, FrameSize, MSG_CONFIRM, (const struct sockaddr *)cliaddr, SocketSize); 
}

/**
 *  @name  UDP_ServerReceive
 *  @brief This API shall recieve a a message from the client.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  @param [in] frame		: Data buffer to hold the received data from the client.
 *  @param [in] cliaddr		: Client Socket Address.
 *  @param [in] SocketSize	: Size of socket structure.
 *  @param [in] FrameSize	: Size of the data to be received.
 *  
 *  @return void.
 */
void UDP_ServerReceive(uint32_t *ServerSocket, uint8_t* frame, struct sockaddr_in*  cliaddr, uint32_t* SocketSize, uint16_t FrameSize)
{	
	if((recvfrom(*ServerSocket, (uint8_t*)frame, FrameSize,  MSG_WAITALL, (struct sockaddr *)cliaddr, SocketSize) < 0))
	{
		printf("Receive from failed\n");
		if(errno == TIMEOUT_ERROR)
		{
			printf("Session Timeout, client has been disconnected\n");
			if(ClientAvailable == 1)
			{
				ClientAvailable = 0;
			}
		}
	}
}

/**
 *  @name  UDP_ServerDisconnect
 *  @brief This API shall terminate the Linux Socket UDP connection.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  
 *  @return void.
 */
void UDP_ServerDisconnect(uint32_t *ServerSocket)
{
	close(*ServerSocket);
}

/**
 *  @name  UDP_ValidateKey
 *  @brief This API shall validate the connection key from the client.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  @param [in] servaddr	: Server Socket Address.
 *  @param [in] cliaddr		: Client Socket Address.
 *  
 *  @return Return description
 */
uint8_t UDP_ValidateKey(uint32_t *ServerSocket, struct sockaddr_in *servaddr, struct sockaddr_in *cliaddr)
{
	uint8_t validation 			= 0;
	uint8_t ConnectionStatus 	= 0;
	uint32_t keyFrame 			= 0;
	uint32_t SocketSize 		= sizeof(struct sockaddr_in);
	
	printf("Waiting for Initialization key....\n");

	/* Wait on the connection key to be received to be validated */
	UDP_ServerReceive(ServerSocket, (uint8_t*)&keyFrame, cliaddr, &SocketSize, sizeof(uint32_t));

	/* Checking whether the connection key is valid or not */
	if(keyFrame == CONNECTION_KEY)
	{
		printf("CONNECTION KEY SUCCESS....\n");
		ClientAvailable = 1;
		validation = 1;
		ConnectionStatus = ACK;
		/* Send an ACK to the client */
		UDP_ServerSend(ServerSocket, (uint8_t*)&ConnectionStatus, cliaddr, SocketSize, sizeof(uint8_t));
	}
	else
	{
		printf("CONNECTION KEY FAILURE....\n");
		validation = 0;
		ConnectionStatus = NACK;
		/* Send an NACK to the client */
		UDP_ServerSend(ServerSocket, (uint8_t*)&ConnectionStatus, cliaddr, SocketSize, sizeof(uint8_t));
	}
	
	return validation;
}

