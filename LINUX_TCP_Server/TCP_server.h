/*********************************************************
 * @defgroup   TCP_CLIENT TCP Server					  
 *														
 * @brief      This file implements TCP Server.
 *
 * @author     BENCH,PLEASE! TEAM
 * @date       June 1st,2020
 *********************************************************/

/*<------------------------ HEARDER GUARD ---------------------->*/
#ifndef TCP_SERVER_H
#define TCP_SERVER_H

/*<---------------------- FILE INCLUDES ------------------------>*/
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 

/*<----------------------MACRO DEFINITIONS  ---------------------->*/
#define SERVER 				"127.0.0.1"   	//ip address of udp server
#define BUFLEN 				512				//Max length of buffer
#define PORT 				8880			//The port on which to listen for incoming data
#define ACK					0x05
#define NACK				0x08
#define STATUS_SIZE			1
#define NUM_OF_FRAMES		3

#define CONNECTION_OK					0
#define CONNECTION_WINSOCK_INIT_ERROR	1
#define CONNECTION_SOCKET_ERROR			2
#define CONNECTION_BIND_ERROR			3
#define CONNECTION_CONNECT_ERROR		4


/************* MESSAGE TYPES MACROS ************/
#define	MESSAGE_ACK				0
#define MESSAGE_NACK			1
#define MESSAGE_HEADER_FRAME	2
#define MESSAGE_DATA_FRAME		3

/********** PC CLIENT INTERFACES ***********/

uint8_t TCP_ServerConnect(void);

void TCP_ServerSend(uint8_t MessageType);

uint8_t TCP_ServerReceive(uint8_t MessageType);

void TCP_ServerDisconnect(void);


#endif /* TCP_SERVER_H */
