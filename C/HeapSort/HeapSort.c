/*
Sorting program using heap sort algorithm
				- by saikiran638
This works as 'qsort' function of standard library.
It needs a specified or user defined callback function for comparing any two objects.
*/

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "HeapMacros.h"

void* array 		= NULL;
static size_t length 	= 0;
static size_t size 	= 0;
static int (*compare)(void const*,void const*)	= NULL; // 

/*
We know that no variable can take its type as 'void'. But we can use 'void' pointers to point 'any' type of data.
It will useful when we don't know the type of the data we are working on.
If you increment pointer to 'int' with value 1. It will point to next integer, but not the next 'byte'.
Usually integer size may vary with respect to system(more than 1 byte). How it is done?
	Here you specified the variable is a pointer to specified type. Using that specified size pointer will be
incremented to sizeof('type') bytes.
	But 'void' pointers has an interesting role. As void specifies no type it has no size mentioned with it.
It is also implementation dependent. Actually it will 1 byte. So we need size of each object while dealing with
void pointer.
*/

// This function swaps two memory locations of some specified size.
static void swap(void* a,void* b){
	// size of each object plays major role here.
	void* temp=malloc(size);	// Temporary storing
	memcpy(temp,a,size);		// temp = a
	memcpy(a,b,size);		// a=b
	memcpy(b,temp,size);		// b=a
	}

// This function established max-heap property
static void MaxHeapify(size_t index){
	int right = RIGHT(index);
	int left  = LEFT(index);
	size_t largest = index;
	if (right<=length && compare( array+ACCESS(index)*size,array+ACCESS(right)*size ) < 0 ) largest = right;
	if (left <=length && compare( array+ACCESS(largest)*size,array+ACCESS(left)*size ) < 0 )largest = left;
	if (largest != index){
		swap( array+ACCESS(largest)*size , array+ACCESS(index)*size);
		MaxHeapify(largest);
		}
	}
// To build max heap.
static void BuildMaxHeap(void){
	size_t var;
	SETZERO(var);
	for (var = length>>1; var>=1; --var)
		MaxHeapify(var);

	}

/* heapsort with same protype of 'qsort'.
   This is not as efficient but an basic implementation from CLRS book.
*/
void heapsort(void* list,size_t len,size_t siz,int (*comp)(void const*,void const*)){
	array = list;
	length = len;
	size = siz;
	compare = comp;
	BuildMaxHeap();
	int var;
	SETZERO(var);
	for (var=length;var>=2;--var){
		swap(list+ACCESS(var)*size,list+ACCESS(1));
		length--;
		MaxHeapify(1);
		}
	}

