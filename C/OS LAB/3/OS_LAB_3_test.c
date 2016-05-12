#include<stdio.h>
#include<fcntl.h>
#include<string.h>
int main()
	{
	char Buffer[]="how  you doing ?\0";
	int fd=open("1.c",O_WRONLY);
	write(fd,Buffer,strlen(Buffer));
	return 0;
	}
