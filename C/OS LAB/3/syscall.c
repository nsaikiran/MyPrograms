#include<stdio.h>
#include<fcntl.h>
#define MSIZ 50

int main(int nargs, char* args[]){
	int rfd=open(args[1],O_RDONLY),wfd=open(args[2],O_WRONLY),var=1,index;
	
	off_t start=lseek(rfd,0,SEEK_SET);
	off_t end=lseek(rfd,-1,SEEK_END);
	char Buffer[MSIZ],c;
	Buffer[MSIZ-1]=0;
	index=MSIZ-2;
	while (start <= end){
		read(rfd,&c,1);
		var++;
		Buffer[index--]=c;
		//printf("%d '%c'\n",index,c);
		if (c==' '||c=='\t'){
			//printf("hit \t %d\n",index);
			printf("%s ",Buffer+index+2);
			index=MSIZ-2;
			}
		if (c=='\n'){
			printf("%s ",Buffer+index+1);
			index=MSIZ-2;
			}
		end=lseek(rfd,-var,SEEK_END);
		}
	if (c!=' '){
		printf("%s",Buffer+index+1);
		} 
	close(rfd);
	close(wfd);
	}