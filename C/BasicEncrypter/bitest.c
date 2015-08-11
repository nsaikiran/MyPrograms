# include <stdio.h>


int main(void) {
	FILE* fp = fopen("t.txt","r");
	char p[3];
	int nread=fread(p,1,2,fp);
	printf("%d\n",nread);
	nread = fread(p,1,2,fp);
	printf("%d\n",nread);
	//fread (	
	int a;
	a^=a;
	printf("%d\n",a);
	return 0;
	}
