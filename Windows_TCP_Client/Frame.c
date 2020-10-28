#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include "Frame.h"

uint8_t DIO_Data[DIO_DATA_SIZE] = {45, 120, 78, 42, 11};
uint8_t UZART_Data[UZART_DATA_SIZE] = {23, 10, 117};

FrameHeader_t FrameHeader = 
{
	.Signature 		= 	SIGNATURE,	
	.NumOfCommands	= 	NUM_OF_CMD,
	.TotalDataSize	= 	TOTAL_SIZE
};

FrameData_t FrameData [NUM_OF_CMD] = 
{
	{
		.PeripheralID	= 	DIO_PERIPHERAL_ID,	
		.DataSize		= 	DIO_DATA_SIZE,		
		.PeripheralData	= 	DIO_Data
	},

	{
		.PeripheralID	= 	UZART_PERIPHERAL_ID,	
		.DataSize		= 	UZART_DATA_SIZE,		
		.PeripheralData	= 	UZART_Data
	}
};

///************************** GLOBAL VARIABLES **************************/

uint8_t* FRAME_Generate(void)
{
	uint16_t CMDIndex = 0;
	uint16_t DataIndex = 0;
	uint16_t FrameIndex = 0;
	
	uint8_t *Frame = (uint8_t *) calloc(TOTAL_SIZE, sizeof(uint8_t));
	
	for(CMDIndex = 0; CMDIndex < NUM_OF_CMD; CMDIndex++)
	{
		Frame[FrameIndex] = FrameData[CMDIndex].PeripheralID; // 2 bytes
		FrameIndex += 2;
		Frame[FrameIndex] = FrameData[CMDIndex].DataSize; //2 bytes
		FrameIndex += 2;
		
		for(DataIndex = 0; DataIndex < FrameData[CMDIndex].DataSize; DataIndex++)
		{
			Frame[FrameIndex] = FrameData[CMDIndex].PeripheralData[DataIndex];
			FrameIndex++;
		}
	}
	return Frame;
}

void FRAME_Print(uint8_t* Frame)
{
	uint16_t Iterator = 0;
	for(Iterator = 0; Iterator < TOTAL_SIZE; Iterator++)
	{
		printf("Frame-Byte[%d]: %d\n", Iterator, Frame[Iterator]);
	}
}


