#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
/*
This is just an example of understanding buffering. It is most of the time not possible to 
identify it in stdout as stdout and stdin are works with screen.
*/

int main(void) {
	int c;
	int limit = 10;
	if (setvbuf(stdout,NULL,_IOFBF,limit)) {
		strerror(errno);
		exit(EXIT_FAILURE);
		}
	//while (( c = fgetc(stdin) )!= EOF ) fwrite(&c,sizeof(1),1,stdout);
	printf("Hello");
	scanf("%d",&c);//Hello won't be printed until you enter some char.
	printf("world!");scanf("%d",&c);
	return 0;
	}
