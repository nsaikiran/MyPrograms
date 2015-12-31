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

void writeBufferedBits( unsigned char*const bitString , int INIT,int FINISH) {
	static unsigned short index= 0U;
	static int byte	= 0U;
	static unsigned char* string	= NULL;
	if ( /*FLAGS &*/ INIT )
		string	= (unsigned char*)calloc(/*BUFSIZ*/2,sizeof(unsigned char));
	if ( /*FLAGS &*/ FINISH ) { // no more data. flush
		// code for ending
		string[byte+1]='\0';// or 0 will do.
		printf("written2 %s %u\n",string,index);
		for ( int flag = 0; flag<strlen(string);++flag)
			printf("%d ",string[flag]);
		printf("written\n");
		}
	if ( !bitString ) return;
	unsigned temp;
	for ( int var	= 0; var < strlen(bitString) ; ++var ) {
		if ( bitString[var] == '1') {
			//printf("1");
			temp ^= temp;
			temp |= 1U;
			temp <<= (7U - ( index % 8U ) );
			//printf("shifted temp : %u ,",temp);
			string[byte] = string[byte] | temp ;
			printf(" %d %d \n",index,byte);
			}
		index++;
		if ( !(index % 8) ) {
			if (byte < /*BUFSIZ*/2 - 2) byte++;
			else {
				printf("written1 %d\n",var);
				string[/*BUFSIZ*/2 - 1] = '\0'; //or 0 will do.
				for ( int flag = 0; flag<strlen(string);++flag)
					printf("%d ",string[flag]);
				printf("written1\n");

				//clear the string
				for ( int flag = 0; flag < /*BUFSIZ*/2;++flag) string[flag]^=string[flag];
				index	= 0;
				byte	= 0;
				//printf("written1 %s %u\n",string,index);
				writeBufferedBits( bitString+var+1, 0,0 );
				break;
				}
			}

		}

	}
# define LIMIT 10

void writeBufferedString( unsigned char*const bitString , int INIT,int FINISH) {
	static unsigned index	= 0U;
	static char* string	= NULL;
	if ( /*FLAGS &*/ INIT )
		string	= (char*)calloc(LIMIT,sizeof(char));
	if ( /*FLAGS &*/ FINISH ) { // no more data. flush
		string[ index ] = 0;
		printf("final %s \n",string);
		index	= 0;
		free(string);
		string	= NULL;
		}
	if ( !bitString ) return;
	printf("Got %s %d \n",bitString,index);
	if ( index + strlen( bitString ) <= LIMIT - 1 ) { // < 9 
		strcpy (string+index,bitString);
		index += strlen(bitString);
		if ( index == LIMIT - 1 ){
			printf("final %s \n",string);//flush
			index	= 0;
			}
		}
	else {
		printf("here\n");
		int n	= (LIMIT - 1) - index;
		printf("n = %d\n",n);
		strncpy( string+index,bitString,n);
		string[LIMIT - 1] = 0;
		printf("final %s \n",string);
		index	= 0;
		printf("here0\n");
		writeBufferedString( bitString + n ,0,0);
		}
	}
# undef LIMIT
