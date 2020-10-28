#ifndef FRAME_H
#define FRAME_H

/******************** EXAMPLE ********************/
#define DIO_PERIPHERAL_ID		0x01
#define DIO_DATA_SIZE			5

#define UZART_PERIPHERAL_ID		0x04
#define UZART_DATA_SIZE			3

#define SIGNATURE				0x07775000
#define NUM_OF_CMD				2
#define PERIPH_HEADER_SIZE		(8)
#define TOTAL_SIZE				(UZART_DATA_SIZE + DIO_DATA_SIZE + (NUM_OF_CMD * PERIPH_HEADER_SIZE))
/*************************************************/

typedef struct
{
	uint32_t Signature;
	uint16_t NumOfCommands;
	uint16_t TotalDataSize;
}FrameHeader_t;


typedef struct
{
	uint32_t  PeripheralID;
	uint32_t  DataSize;
	uint8_t*  PeripheralData;
}FrameData_t;

void FRAME_Generate(uint8_t* DIO_Data, uint32_t DIO_DataSize , uint8_t* UART_Data, uint32_t UART_DataSize);
void FRAME_Print(void);


#endif /* FRAME_H */