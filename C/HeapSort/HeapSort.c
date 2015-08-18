/* Heapsort:: It draws in-place sorting property from insertion sort and O(nlong n) complexity from Merge sort */

# include <stdio.h>
# include <stdlib.h>


# define PARENT	(ind) 	( ind >> 1)
# define LEFT(ind)	( ind << 1)
# define RIGHT(ind) ( LEFT(ind) + 1 )
inline int func( int a ) { return a;}


int main (int nargs, const char* const * const args) {
	func(4);	
	return EXIT_SUCCESS;	
	}
