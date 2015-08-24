# include <stdio.h>
# include <string.h>
# include "HeapSort.h"
# include "HeapMacros.h"

//int compare(void const* a, void const *b){
//	return *(int*)a - *(int*)b ;
//	}
int compare(void const*a,void const *b){
	return strcmp(*(char**)a,*(char**)b);
	}
int main(int nargs,char *const*const args){
	//int a[]={4,1,3,2,16,9,10,14,8,7,-1};//{16,14,10,8,7,9,3,2,4,1};
//	int a[]={120,-9,0,34,-123};
	char *a[]={"saikiran","abhinav","Itw","Cloud computing","CSE"};
	heapsort(a,sizeof(a)/sizeof(char*),sizeof(char*),compare/*,swap*/);
	int var=0;
//	for (;var<5;++var)printf("- %d\n",a[var]);
	for (;var<sizeof(a)/sizeof(char*);++var) printf("%s\n",a[var]);
	return 0;
	}
