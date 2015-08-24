# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "HeapMacros.h"

void* array 		= NULL;
static size_t length 	= 0;
static size_t size 	= 0;
static int (*compare)(void const*,void const*)	= NULL;


static void swap(void* a,void* b){
	void* temp=malloc(size);
	memcpy(temp,a,size);
	memcpy(a,b,size);
	memcpy(b,temp,size);
	}

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

static void BuildMaxHeap(void){
	size_t var;
	SETZERO(var);
	for (var = length>>1; var>=1; --var)
		MaxHeapify(var);

	}

void heapsort(void* list,size_t len,size_t siz,int (*comp)(void const*,void const*)/*,void (*swp)(void *,void *)*/){
	array = list;
	length = len;
	size = siz;
	compare = comp;
	//swap = swp;
	BuildMaxHeap();
	int var;
	SETZERO(var);
	for (var=length;var>=2;--var){
		swap(list+ACCESS(var)*size,list+ACCESS(1));
		length--;
		MaxHeapify(1);
		}
	}

