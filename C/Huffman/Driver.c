# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "Compress.h"

unsigned long int frequencies[128];

void findFrequencies( unsigned char *const buffer ) {
	for ( register int index = 0; index < strlen(buffer); ++index )
		frequencies[buffer[index]]++;
	}

int main( int nargs, const char * const * const args ) {
	if ( nargs < 2 ) exit(EXIT_FAILURE);
	FILE* infile = fopen(args[1],"r");
	if ( !infile ) exit(EXIT_FAILURE);
	
	unsigned char buffer[BUFSIZ];
	for ( register int index  = 0;	index < 128; ++index )	frequencies[index]^=frequencies[index];
	
	while ( !feof(infile) ) {
		if ( !fgets( buffer, BUFSIZ, infile)) continue;
		
		//for ( int t=0;t<strlen(buffer);++t) printf("%c %d \n",buffer[t],buffer[t]); printf("doone");

		findFrequencies( buffer );
		}

	for ( register int index = 0;	index < 128; ++index )	
		if (frequencies[index]) 
			printf("'%c' %10lu\n",index,frequencies[index]);
	
	printf("trur or false : %d\n",'\n'==10);
	buildTree();
	return EXIT_SUCCESS;
	}
