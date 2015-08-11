# include <stdio.h>
# include <stdlib.h>

int main (void) {
	setbuf(stdin,NULL);
	int a;
	char b;
	char c[10];
	scanf("%d%c%s",&a,&b,c);
	printf("%d and %c and %s\n",a,b,c);
	fputc('c',stdin);
	return 0;
	}
