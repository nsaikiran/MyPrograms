#include<stdio.h>

int main(void){
	
	/* This program demonstrates that we can use type-qualifiers to pointers as we are using to the location
	they are pointing to.
	*/

	int b = 10;
	static int *static const a = &b;
	//a=&b;
	printf("%d\n",b);
	printf("%d\n",*a);
	b=20; 
	}
