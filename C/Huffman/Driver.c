# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "Compress.h"

info characters[128];

void findFrequencies( unsigned char *const buffer ) {
	for ( register int index = 0; index < strlen(buffer); ++index )
		characters[buffer[index]].count++;
	}

int main( int nargs, const char * const * const args ) {
	if ( nargs < 2 ) exit(EXIT_FAILURE);
	FILE* infile = fopen(args[1],"r");
	if ( !infile ) exit(EXIT_FAILURE);
	
	unsigned char buffer[BUFSIZ];
	for ( register int index  = 0;	index < 128; ++index )	characters[index].count^=characters[index].count;
	
	while ( !feof(infile) ) {
		if ( !fgets( buffer, BUFSIZ, infile)) continue;
		
		findFrequencies( buffer );
		}

	for ( register int index = 0;	index < 128; ++index )	
		if (characters[index].count) 
			printf("'%c' %10lu\n",index,characters[index].count);
	
	printf("trur or false : %d\n",'\n'==10);
	buildTree();
	return EXIT_SUCCESS;
	}
