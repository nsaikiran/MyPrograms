# include <stdio.h>

void InsertionSort(int* arr,int len){
	int var = len - 1,flag;
	int  key = arr[var];
	while ( var > 0  && key < arr[var-1] ) {
		arr[var]=arr[var-1];
		var--;
		for (flag = 0; flag < len-1; printf("%d ",arr[flag++]) );
		printf("%d\n",arr[flag]);
		}
	arr[var]=key;
	printf("%d",arr[0]);
	for (flag = 1; flag < len; printf(" %d",arr[flag++]) );
	printf("\n");
	}

int main(void){
	int len,var=0;
	scanf("%d",&len);
	int arr[len];
	for (;var<len;++var)
		scanf("%d",&arr[var]);
	InsertionSort(arr,len);	

	return 0;
	}
