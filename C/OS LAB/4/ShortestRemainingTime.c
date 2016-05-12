/*
Program	: Scheduling Algorithm
Type	: Shortest Remaining Time First
Author	: saikiran638
*/

#include<stdio.h>
#include<stdlib.h>
#define MPID 10

/*
Define enumeration constants.
*/
typedef enum {false,true} Bool;


typedef struct {
	char pid[MPID];
	int Atime;
	int Btime;
	int Ctime;
	Bool exec;
	}process;

//Global variables declaration.	
int N=0;//no.of processes

/*
This function sorts given array of processes  based on their arrival times.
Assuming less number of processes, wrote insertion sort.
*/
void sortAtime(process **array){
	int var=1,index=0;
	process* key=NULL;
	for (;var<N;++var){
		key=array[var];
		index=var-1;
		while (index>=0 && key->Atime < array[index]->Atime)
			array[index+1]=array[index],index--;
		array[index+1]=key;
		}
	}
/*
This function prints given process on console
*/
void Show(process **array){
	int var=0;
	for (;var<N;++var)
		printf("\n%s %d %d %d\n",array[var]->pid,array[var]->Atime,array[var]->Btime,array[var]->Ctime);
	}

/*
* This function constitutes major part of this program (Scheduling algorithm)
* It receives sorted array of processes(based on their arrival times)
* It assigns completion time for every process .
*/
void Schedule(process **array){
	int cpu_time=array[0]->Atime,	//initialize cpu-time with first process's arrival time
		completed=0,		//execution completed processes are 0
		min=0,			// initialize min index
		var=0;
	while ( completed !=N){	//all processes are completed
		min=var=0;
		while (array[var]->exec)var++;	//find first non completed process in array
		min=var;
		for (; var < N && array[var]->Atime <= cpu_time;++var){	//This loop finds process with minimum burst-time
			if (array[var]->exec)continue;	//check whether it is finished or not
			if (array[var]->Btime < array[min]->Btime)min=var;
			}
		array[min]->Btime--;	//allocate one unit time slice to the process
		cpu_time++;				//update cpu-time as we have allocated it to the process.
		if (array[min]->Btime == 0){	//If its burst-time is 0.
			array[min]->exec=true;		//label this process as executable
			array[min]->Ctime=cpu_time;	//update its completed time
			completed++;				//update completed count 
			}
		}
	}
	
int main(void){
	int var=0;
	scanf("%d",&N);
	process* parray[N];
	for (;var<N;++var){
		parray[var]=(process*)malloc(sizeof(process));
		parray[var]->exec=false;
		scanf("%s%d%d",parray[var]->pid,&parray[var]->Atime,&parray[var]->Btime);
		parray[var]->Ctime=0;
		}
	sortAtime(parray);
	Show(parray);
	Schedule(parray);
	Show(parray);
	return 0;
	}