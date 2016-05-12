// 5.read contents from two files and append to a single file
#include<stdio.h>
#include<fcntl.h>

int main(int nargs,char* argv[])
	{
	if (nargs!=4)
		return 1;
	char *rfname=argv[1],*rfname1=argv[2],*wfname=argv[3],Buffer[100];
	int rfd=open(rfname,O_RDONLY),rfd1=open(rfname1,O_RDONLY),wfd=creat(wfname,0777),bytes;
	if (rfd==-1 || wfd==-1 ||rfd1==-1)
		{
		printf("Can not open %s , %s and %s successfully\n",argv[1],argv[2],argv[3]);
		return 1;
		}
	printf("Successfully opened %s , %s and %s .\n",argv[1],argv[2],argv[3]);
	while ( bytes=read(rfd,Buffer,sizeof(Buffer)) )//bytes is the no . of bytes read from input.. it will be zero if EOF occurs
		write(wfd,Buffer,bytes);
		
	while ( bytes=read(rfd1,Buffer,sizeof(Buffer)) )
		write(wfd,Buffer,bytes);

	close(rfd1);
	close(rfd);
	close(wfd);
	return 0;
	}
//Ctrl + D EOF
