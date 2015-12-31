void setBuffer(unsigned size,FILE* ofile);
void startBufferedBitsWriter(void);
void stopBufferedBitsWriter(void);
void flushBufferedBits(void) ;
void writeBufferedBits( unsigned char*const bitstring );
