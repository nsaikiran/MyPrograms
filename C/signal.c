/*
This program demostrates usage of signals in C programming. Before using this program's		|
executable. Keep in mind that stdin and stdout are 'line buffered': data will be written into 	|
stdin/stdout when you press enter/it gets newline. So, to get understand clearly press some	|
character and EOF(Ctrl+D in UNIX and Ctrl+Z in Windows) when it asked you to do	if you didn't	|
redirect stdin else it won't be a problem.							|
*/


# include <stdio.h>
# include <signal.h>
# include <stdlib.h>

# define CHECKERR( ERR, CHECK) (ERR & CHECK) == CHECK		//Mind operator precedence	|

static const char *progname=NULL;
static const char * const author = "SAI KIRAN N";
static unsigned count=0;
static const char* const text = "Hello\n";
static unsigned short error=0;

enum { NOERROR,USAGERROR,INVALIDARG };

void (*handler_ptr)(int) = NULL;

void handler(int sig) {
	printf("\nReceived interrupt\n Press something to continue:");
	if ( signal( sig , handler) == SIG_ERR) exit(EXIT_FAILURE);
	char c;
	scanf("%c",&c);
	count++;
	}

void cleaner(void) {
	//There are no variables to clean or free.						|
	if (!error) {
		fprintf(stderr,"Program Terminated Normally\n");
		return;
		}
	if (CHECKERR(error,USAGERROR))
		fprintf(stderr,"Usage:\n%s number\n",progname);
	if (CHECKERR(error,INVALIDARG))
		fprintf(stderr,"Argument must be positive\n");
	}

int main ( int nargs, char * const * const args) {
	progname = args[0];
	atexit( cleaner );		//The function will be called at the end of the program	|
	if ( nargs < 2 && (error|=USAGERROR) ) exit(EXIT_FAILURE);
	int csigint = atoi(args[1]);
	if ( csigint < 0 && (error|=INVALIDARG)) exit(EXIT_FAILURE);
	handler_ptr = handler;		// Here we didn't use it.				|
	if ( signal( SIGINT ,handler )== SIG_ERR ) exit(EXIT_FAILURE);
	while (count < csigint)
		puts(text);
	printf("Author: %s \n",author);
	return EXIT_SUCCESS;
	}
