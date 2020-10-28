/**
 *  @file Frame.h
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief PC Client Frame Header File
 */
 
#ifndef FRAME_H
#define FRAME_H

/*****************************************************************************/
/********************************* FRAME MACROS ******************************/
/*****************************************************************************/

/* Peripherals Info macros */
#define DIO_PERIPHERAL_ID		0x01
#define PWM_PERIPHERAL_ID		0x04
#define PWM_CONFIG_SIZE			16
#define UART_PERIPHERAL_ID		0x07
#define UART_CONFIG_SIZE		12
#define SPI_CH1_PERIPHERAL_ID	0x08
#define SPI_CH1_CONFIG_SIZE		12
#define SPI_CH2_PERIPHERAL_ID	0x09
#define SPI_CH2_CONFIG_SIZE		12

#define SIGNATURE				0x07775000
#define DIO_OUTPUT_PINS			4
#define NUM_OF_PERIPH			5
#define NUM_RX_PERIPH			2
#define PERIPH_HEADER_SIZE		8
#define PERIPH_ID_SIZE			(sizeof(uint32_t))
#define PERIPH_INFO_SIZE		(PERIPH_HEADER_SIZE * NUM_OF_PERIPH)

/* Serial Channels macros */
#define SERIAL_UART				0
#define SERIAL_SPI_CH1			1
#define SERIAL_SPI_CH2			2


/*****************************************************************************/
/*************************** FRAME TYPE DEFINITIONS **************************/
/*****************************************************************************/

typedef struct
{
	/* Signature of client */
	uint32_t Signature;
	
	/* Number of Peripherals supported by the frame */
	uint16_t NumOfPeripherals;
	
	/* Total size of data frame */
	uint16_t TotalDataSize;
}FrameHeader_t;

typedef struct
{
	/* ID of peripheral */
	uint32_t  PeripheralID;
	
	/* Size of Data/Config of a peripheral */
	uint32_t  DataSize;
	
	/* Data/Config of a peripheral */
	uint8_t   PeripheralData;
}FrameData_t;

/*****************************************************************************/
/***************************** FRAME INTERFACES ******************************/
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
void FRAME_GenerateDataFrame(uint8_t* DIO_Data, uint8_t* PWM_Config, uint8_t* UART_Config, uint8_t* SPI_CH1_Config, uint8_t* SPI_CH2_Config);

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
void FRAME_GenerateSerialFrame(uint8_t *Serial_Data, uint32_t Serial_DataSize, uint8_t SerialIndex);

/**
 *  @name  FRAME_SerialReturnFrame
 *  @brief This API shall send the received serial data from server to GUI.
 *  
 *  @return Buffer of serial data received.
 */
uint8_t *FRAME_SerialReturnFrame(void);

/**
 *  @name  FRAME_ReadingsFrame
 *  @brief This API shall return the (DIO - PWM) Readings from the server to GUI.
 *  
 *  @return Buffer holding the readings.
 */
uint32_t *FRAME_ReadingsFrame(void);

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
void FRAME_FreeBuffer(uint8_t Buffer);

/**
 *  @name  FRAME_Print
 *  @brief This API shall print the data frame sent to the server.
 *  
 *  @return void.
 */
void FRAME_Print(void);

#endif /* FRAME_H */

