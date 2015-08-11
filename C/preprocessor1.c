/* This programs is to demonstrate the third type of preprocessor macro #include
Ref: The book , Reference manual.. It is intriguing there
*/

# define STDIO <stdio.h>

#include STDIO

int main(void){
	printf("Hello");
	return 0;
	}
