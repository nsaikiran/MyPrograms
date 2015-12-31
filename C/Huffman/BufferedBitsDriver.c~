#include <stdio.h>
# include "BufferedBitsWriter.h"
int main(void) {
	FILE* fp	= fopen("testbuff","w");
	setBuffer(2,fp);
	startBufferedBitsWriter();
	writeBufferedBits("1111000");
	writeBufferedBits("00010");
	writeBufferedBits("1101");
	writeBufferedBits("00101000110");
	flushBufferedBits();
	stopBufferedBitsWriter();
	}
