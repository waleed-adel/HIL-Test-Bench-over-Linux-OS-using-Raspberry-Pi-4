 /**
 *  @file Frame.h
 *  @authors (May Alaa - Hazem Mekawy - Ahmed Zoher - Ahmed Refaat - Waleed Adel)
 *  @brief Linux Server Frame Header File
 */
 
#ifndef FRAME_H
#define FRAME_H

/*****************************************************************************/
/********************************* FRAME MACROS ******************************/
/*****************************************************************************/

/* RaspberryPi Configurations macros */
/* Serial channels Receiving buffer length */
#define RX_BUFF_LEN				512
/* Messages Receiving buffer length */
#define FRAME_DATA_LEN			512

/* Peripherals Info macros */
#define DIO_PERIPHERAL_ID			0x01
#define DIO_DATA_SIZE				16
#define PWM_PERIPHERAL_ID			0x04
#define PWM_DATA_SIZE				16

#define SIGNATURE					0x07775000
#define NUM_READINGS_PERIPH			2
#define PERIPH_HEADER_SIZE			8
#define PERIPH_ID_SIZE				(sizeof(uint32_t))
#define TOTAL_READINGS_DATA_SIZE	((DIO_DATA_SIZE + PWM_DATA_SIZE) + (NUM_READINGS_PERIPH * PERIPH_HEADER_SIZE))


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


#endif /* FRAME_H */


