# include <stdio.h>
# include <string.h>
# include <stdlib.h>

void writeBits( unsigned char* bitString ) {
	unsigned char* array	= (unsigned char*)calloc(BUFSIZ,sizeof(unsigned char));
	int byte		= -1;
	unsigned int index	= 0U;
	unsigned char temp	= 0U;

	printf("\n\n");

	for (; index	< strlen(bitString) & byte < BUFSIZ-1 ; ++index ) {
		if ( !(index % 8) ){
			if ( byte < BUFSIZ - 2 )
				++byte;
			printf("\nbit changed %d \n",byte);
			}
		if ( bitString[index] == '1') {
			printf("1");
			temp ^= temp;
			temp |= 1U;
			temp <<= (7U - ( index % 8U ) );
			printf("shifted temp : %u ,",temp);
			array[byte] = array[byte] | temp ;
			}
		}
	printf( "\n ..  %d %d \n",index % 8,byte );
	array[byte+1]	= 0;// or '\0'

	for ( index =0 ;index <= byte ;++ index ) 
		printf("\n.. Encoded %u\n",array[index] );
	free( array );
	}
