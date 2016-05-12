// 3.write a program that reading data from file and display on monitor
#include<stdio.h>
#include<fcntl.h>
int main(int nargs,char* argv[])
	{
	if (nargs!=2)
		return 1;
	char *fname=argv[1],Buffer[100];
	int fd=open(fname,O_RDONLY),bytes;
	if (fd==-1)
		{
		printf("File %s not opened successfully\n",argv[1]);
		return 1;
		}
	printf("File %s opened successfully\n",argv[1]);
	while ( bytes=read(fd,Buffer,sizeof(Buffer)) )//bytes is the no . of bytes read from input.. it will be zero if EOF occurs
		write(1,Buffer,bytes);
	close(fd);
	return 0;
	}
//Ctrl + D EOF
