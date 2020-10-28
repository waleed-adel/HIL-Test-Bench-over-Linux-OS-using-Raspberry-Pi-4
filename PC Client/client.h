/**
 *  @file client.h
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief PC Client Header File
 */

#ifndef CLIENT_H
#define CLIENT_H

/* File includes */
/* Winsock Library */
#include <winsock2.h>
#pragma comment(lib,"ws2_32") 	


/*****************************************************************************/
/********************************* CLIENT MACROS *****************************/
/*****************************************************************************/

/* Enabling client buffers tracing */
#define TRACE_PRINT_ENABLE				0

/* Client connection status macros */
#define CONNECTION_KEY					0x12487
#define CONNECTION_TIMEOUT_COUNT		5
#define CONNECTION_OK					0
#define CONNECTION_WINSOCK_INIT_ERROR	1
#define CONNECTION_SOCKET_ERROR			2
#define CONENCTION_REQUEST_TIMEOUT		3

/* Client Messages macros */
#define STATUS_SIZE						1
#define ACK								0x05
#define NACK							0x08
#define HEADER_VALID					0
#define HEADER_INVALID					1
#define	MESSAGE_ACK						0
#define MESSAGE_NACK					1
#define MESSAGE_HEADER_FRAME			2
#define MESSAGE_DATA_FRAME				3
#define MESSAGE_CONNECTION_KEY			4
#define MESSAGE_UART					5
#define MESSAGE_SPI_CH1					6
#define MESSAGE_SPI_CH2					7
#define MESSAGE_SERIAL_SIZE				8

/* Frame Indexes to free allocated Data */
#define DATA_FRAME						0
#define SERIAL_FRAME					1
#define SERIAL_RETURN_FRAME				2
#define READINGS_FRAME					3



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
uint8_t UDP_ClientConnect(uint8_t* ServerIP, uint16_t ServerPort);

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
void UDP_ClientSend(uint8_t MessageType);

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
uint8_t UDP_ClientReceive(uint8_t MessageType);

/**
 *  @name  UDP_ClientDisconnect
 *  @brief This API shall disconnect the client from server.
 *  
 *  @return void.
 */
void UDP_ClientDisconnect(void);


#endif /* CLIENT_H */