/*
A program to find factorial of a given number ( we get relatively large factorial ).
It follows basic arithmetic operation ( hand multiplication )
Author : saikiran638
*/

# include <stdio.h>
# include <assert.h>
# define LEN 200	// Expected max-number of digits in a factorial

void Factorial( size_t num ) {
	size_t arr[LEN],temp = num,index=0,var=0,flag=0;
	while ( temp ) {
		arr[index++] = temp%10;
		temp/=10;
		}

	for (var=num-1; var>=2 ; var-- ) {
		temp = 0;
		for (flag = 0; flag < index ; ++flag ){
			temp += arr[flag]*var;
			arr[flag ] = temp%10;
			temp/=10;
			}
		while (temp){
			assert(index < 200 ); // Unknowingly if digits exceed max-number of digits, throw run-time error. and exit
			arr[index++]=temp%10;
			temp/=10;
			}
		}
	while ( index ) {printf("%lu",arr[index-1]); index--;}
	printf("\n");
	}

int main ( void ){
	int num;
	scanf("%d",&num);
	Factorial(num);
	return 0;
	}

	
