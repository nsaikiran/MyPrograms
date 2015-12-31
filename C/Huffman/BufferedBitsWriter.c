# include <stdio.h>
# include <string.h>
# include <stdlib.h>

# define DONOT	0
# define DO		1

# define ECALLSEQUENCE	1
# define EINPUTPARAM	2

static unsigned maxsize	= BUFSIZ;
static unsigned char* string	= NULL;
static char flush	= DONOT;

static unsigned short index= 0U;
static unsigned byte	= 0U;
static FILE* outfile	= NULL;
static unsigned writes	= 0;

void showError(short error){
	switch(error){
		default:
			fputs("\nUnknown Error\n",stderr);break;
		case 1:
			fputs("\nInvalid Call Sequence\n",stderr);break;
		case 2:
			fputs("\nInvalid Input Parameters\n",stderr);break;
		}
	}

void writeBufferedBits( unsigned char*const bitstring ) {
	if ( !string ){
		showError(ECALLSEQUENCE);
		return;
		}
	if (  flush	== DO ) { // no more data. flush
		if ( index%8 )
			string[byte+1]='\0';// or 0 will do.
		else{
			if ( writes > 0 ) --index;
			string[byte]='\0';
			}
		fprintf(outfile,"%s %d\n",string,index%8);
				
		printf("\nflush1\n");
		for ( int var =0;var<=byte;++var)
			printf("%d ",string[var]);
		printf("\nflush1\n");
		printf("No.of writes %d\n",writes);
		//clear the string
		for ( int flag = 0; flag < maxsize;++flag) string[flag]^=string[flag];
		index	= 0;
		byte	= 0;
		}
	if ( !bitstring ) return;
	unsigned temp;
	for ( int var	= 0; var < strlen(bitstring) ; ++var ) {
		if ( bitstring[var] == '1') {
			temp ^= temp;
			temp |= 1U;
			temp <<= (7U - ( index % 8U ) );
			string[byte] = string[byte] | temp ;
			}
		index++;
		if ( !(index % 8) ) {
			if (byte < maxsize - 2) byte++;
			else {
				string[maxsize - 1] = '\0'; //or 0 will do.
				//write to file here.
				fputs(string,outfile);
				writes++;
						
				printf("\nflush\n");
				for ( int var =0;var<byte;++var)
					printf("%d ",string[var]);
				printf("\nflush\n");
				
				//clear the string
				for ( int flag = 0; flag < maxsize;++flag) string[flag]^=string[flag];
				index	= 0;
				byte	= 0;

				writeBufferedBits( bitstring+var+1 );
				break;
				}
			}
		}
	}

void setBuffer(unsigned size,FILE* ofile){
	if ( !string ) {
		if (size) maxsize	= size;
		if (ofile)outfile	= ofile;
		}
	else showError(ECALLSEQUENCE);
	}

void startBufferedBitsWriter(void){
	if ( !string && outfile ) {
		string	= (unsigned char*)calloc(maxsize,sizeof(unsigned char));
		index	= byte	= 0U;
		flush	= DONOT;
		writes	= 0;
		}
	else showError(EINPUTPARAM);
	}

void stopBufferedBitsWriter(void){
	if ( string ) {
		free(string);
		string	= NULL;	//whenever we free something, point that to NULL
		}
	}

void flushBufferedBits(void) {
	if ( string ) {
		flush	= DO;
		writeBufferedBits(NULL);
		flush	= DONOT;
		}
	}
