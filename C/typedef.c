/*We can use typedef in the situations that 'confuses' us. So make good use of it.*/


/* We can typedef function declarations and use that typede-name in pointer to function declarations.
But we can't use this typedef-names to define functions.
*/

#include <stdio.h>
/*
Here we are creating a type 'function returns int and takes no arguments'. The most importatnt point is that we can't use this type
we created to define functions. But we can use in other declrations like 'pointers'.
*/

typedef int func(void);

int callme(void){
	int a =10;
	printf("%d\n",a);
	return 0;
	}

int main (void){
	func *ptr=callme;
	ptr();
	callme();
	return 0;
	}
