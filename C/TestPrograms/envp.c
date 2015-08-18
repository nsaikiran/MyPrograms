# include <stdio.h>

int main ( int nargs, char * args[],char * envp[]){
	int i=0;
	for (;i<20;i++)	
	puts(envp[i]);
	return 0;
	}
