 /**
 *  @file server.h
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief Linux Server Header File
 */
 
#ifndef SERVER_H
#define SERVER_H

/* Libraries includes */
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 
#include <errno.h>

/*****************************************************************************/
/******************************* SERVER MACROS *******************************/
/*****************************************************************************/

/* Server connection status macros */
#define TRACE_PRINT_ENABLE		0
#define PORT     				8080 
#define SERVER 					"192.168.5.10"
#define TIMEOUT_DURATION_SEC	10
#define TIMEOUT_ERROR			11
#define CONNECTION_KEY			0x12487
#define ACK 					0x05
#define NACK					0x08
#define STATUS_SIZE				1


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
void UDP_ServerInit(uint32_t *ServerSocket, struct sockaddr_in *servaddr, struct sockaddr_in *cliaddr);

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
void UDP_ServerSend(uint32_t *ServerSocket, uint8_t* Buffer, struct sockaddr_in * cliaddr, uint32_t SocketSize, uint16_t FrameSize);

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
void UDP_ServerReceive(uint32_t *ServerSocket, uint8_t* frame, struct sockaddr_in*  cliaddr, uint32_t* SocketSize, uint16_t FrameSize);

/**
 *  @name  UDP_ServerDisconnect
 *  @brief This API shall terminate the Linux Socket UDP connection.
 *  
 *  @param [in] ServerSocket: Server Socket Number.
 *  
 *  @return void.
 */
void UDP_ServerDisconnect(uint32_t *ServerSocket);

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
uint8_t UDP_ValidateKey(uint32_t *ServerSocket, struct sockaddr_in *servaddr, struct sockaddr_in *cliaddr);

#endif /* SERVER_H */



