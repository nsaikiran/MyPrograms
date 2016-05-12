// 4.reading data from one file and writing in to another file
#include<stdio.h>
#include<fcntl.h>

int main(int nargs,char* argv[])
	{
	if (nargs!=3)
		return 1;
	char *rfname=argv[1],*wfname=argv[2],Buffer[100];
	int rfd=open(rfname,O_RDONLY),wfd=creat(wfname,0777),bytes;
	printf("%d %d \n",rfd,wfd);
	if (rfd==-1 || wfd==-1)
		{
		printf("Can not open %s and %s successfully\n",argv[1],argv[2]);
		return 1;
		}
	printf("Successfully opened %s and %s successfully\n",argv[1],argv[2]);
	while ( bytes=read(rfd,Buffer,sizeof(Buffer)) )//bytes is the no . of bytes read from input.. it will be zero if EOF occurs
		write(wfd,Buffer,bytes);
	close(rfd);
	close(wfd);
	return 0;
	}
//Ctrl + D EOF
