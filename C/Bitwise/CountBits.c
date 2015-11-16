# include <stdio.h>

int main(void) {
	unsigned long a,count = 0;
	scanf("%lu",&a);
	while (a) {
		if ( a & 1u ) count++;
		a >>= 1;
		}
	printf("%lu",count);
	return 0;
	}
