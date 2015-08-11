/*
In this program we will learn how to use type-qualifiers to pointers
*/

#include <stdio.h>

int
main(void){	
	int a;
	/*This declaration specifies b is a constant pointer, the location to which it points can't be changed.It points to a location 
	that is assumed constant by the pointer . We can't change the value in the location pointed by b using b.*/
	const int *const b=&a;
	a=10;
	printf("%d\n",*b);
	// *b=6; //Will raise an error
	a=11;
	return 0;
	}
	
