// 2.write a program that reading data from keyboard and display on monitor
#include<stdio.h>

int main(void)
	{
	char Buffer[100];
	unsigned bytes;
	while ( bytes=read(0,Buffer,sizeof(Buffer)) )//bytes is the no . of bytes read from input.. it will be zero if EOF occurs
		write(1,Buffer,bytes);
	return 0;
	}
//Ctrl + D EOF
