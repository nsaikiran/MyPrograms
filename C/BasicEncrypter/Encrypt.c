/*
Aim:	To write a basic encryption program using bitwise XOR (^) operator to encrypt & decrypt the data.				|
	Encryption:															|
		X^KEY = Z .	Here Z is considered as encrypted character.								|
	Decryption:															|
		Z^KEY = X .														|
*/

# include <stdio.h>
# include <stdlib.h>
# include <string.h>

//Error and Notification codes														|
# define ERR_USAGE 	1u
# define ERR_INFILE 	2u
# define ERR_KEY 	4u
# define ERR_DFOUT 	8u
# define ERR_OUT 	16u
# define NOTI_DFOUT 	32u
# define NOTI_OUT 	64u
# define SUCCESS	128u

// pointer to arguments of main														|
static char *const *margs=NULL;

//Error and Notification status														|
static unsigned status=0;

//Main part of the program.														|
static int crypt(FILE *const infile,FILE *const outfile,char *const key) {
	unsigned len  = strlen (key),var=0;
	unsigned char ptr[len+1];
	while ( fgets(ptr,len+1,infile) ){
		for (var=0;var< strlen(ptr); ++var)
			ptr[var] ^= key[var];
		fputs(ptr,outfile);
		}
	}

//Check for errors & notifications and print appropriate messages.									|
static void notify(void){
	if ( (status & ERR_USAGE)  == ERR_USAGE) 	fprintf(stderr,"Usage:\n\t%s inputfile key [outputfile].\n",margs[0]);
	if ( (status & ERR_INFILE) == ERR_INFILE ) 	fprintf(stderr,"\nERROR:	file '%s' doesn't exist.\n",margs[1]);
	if ( (status & ERR_KEY )   == ERR_KEY ) 	fprintf(stderr,"\nERROR:	Invalid key.\n");
	if ( (status & ERR_DFOUT ) == ERR_DFOUT) 	fprintf(stderr,"\nERROR:	Unable to create default file.\n");
	if ( (status & ERR_OUT )   == ERR_OUT)		fprintf(stderr,"\nERROR:	file '%s' already exist.\n",margs[3]);
	if ( (status & NOTI_DFOUT) == NOTI_DFOUT)	fprintf(stdout,"\nNOTIFICATION:	output written to '%s.crypt'.\n",margs[1]);
	if ( (status & NOTI_OUT)   == NOTI_OUT)		fprintf(stdout,"\nNOTIFICATION:	output written to '%s'.\n",margs[3]);
	if ( (status & SUCCESS )   == SUCCESS)		fprintf(stdout,"\nNOTIFICATION:	Successful termination.\n");
	return;
	}

int main (int nargs,char *const*const args) {
	margs=args;
	atexit(notify);// register notify function to be called before normal termination						|

	if ( nargs < 3 && (status |= ERR_USAGE) ) exit(EXIT_FAILURE);

	FILE *infile = NULL,*outfile = NULL;

	if ((infile=fopen(args[1],"r")) == NULL && (status |= ERR_INFILE) ) 
		exit(EXIT_FAILURE);

	if ( !strlen(args[2]) &&  (status |= ERR_KEY) ) 
		exit(EXIT_FAILURE);

	unsigned char out[strlen(args[1]) + 6];

	if ( nargs == 3) { 	//no output file name specified. Assume inputfile.crypt as outputfile name.				|
		strcpy(out,args[1]);
		strcat(out,".crypt");
		if ( ( outfile=fopen(out,"r") ) != NULL && (status |= ERR_DFOUT) )
			exit(EXIT_FAILURE);
		else {
			outfile = fopen(out,"w");
			status |= NOTI_DFOUT;
			}
		}
	else {			//output filename specified										|
		if ( (outfile = fopen(args[3],"r")) != NULL && (status |= ERR_OUT) )	//Check whether it exists or not. 
			exit(EXIT_FAILURE);
		else {
			outfile = fopen(args[3],"w");
			status |= NOTI_OUT;
			}

		}
		
	crypt(infile,outfile,args[2]);
	status |= SUCCESS;	//Successful termination										|
	return EXIT_SUCCESS;
	}
