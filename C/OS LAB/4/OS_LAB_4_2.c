/*
Scheduling Algorithm : SJF Shortest Job First.
saikiran638
*/
#include<stdio.h>
#include<stdlib.h>
#define MPID 10

typedef enum {false,true} Bool;

typedef struct {
	char pid[MPID];
	int Atime;
	int Btime;
	int Ctime;
	Bool exec;
	}process;
//Insertion Sort
void Sort_Btime(process* array[],int n){
	int var=1,index;
	process* key=NULL;
	for (;var<n;++var){
		key=array[var];
		index=var-1;	
		while (index >= 0 && key->/*Btime*/Atime < array[index]->/*Btime*/Atime )
			array[index+1]=array[index],index--;
		array[index+1]=key;
		}
	}

void Schedule(process* parray[],int n){
	int mindex,flag,c_process=0,cpu_time=0;
	for (;c_process < n;){	
		mindex=-1;
		for (flag=0;flag<n;++flag){
			if (parray[flag]->exec == true || parray[flag]->Atime > cpu_time)continue;
			if (mindex==-1)
				mindex=flag;
			else
				if (parray[mindex]->Btime > parray[flag]->Btime )mindex=flag;
			}
		if (mindex==-1)cpu_time++;
		else {
			parray[mindex]->exec=true;
			cpu_time+=parray[mindex]->Btime;
			parray[mindex]->Ctime=cpu_time;
			++c_process;
			}
		}
	}

void Print(process* parray[],int n){
	int var=0;
	printf("%10s %10s %10s %10s %10s %10s\n","PID","Atime","Btime","Ctime","TATime","WTime");
	for (;var<n;++var)printf("%10s %10d %10d %10d %10d %10d\n",parray[var]->pid,parray[var]->Atime,parray[var]->Btime,
		parray[var]->Ctime,parray[var]->Ctime-parray[var]->Atime,parray[var]->Ctime-parray[var]->Atime-parray[var]->Btime);
	}
	
int main(){
	int n,var=0;
	scanf("%d",&n);
	process* parray[n];
	for (;var<n;++var){
		parray[var]=(process*)malloc(sizeof(process));
		parray[var]->exec=false;
		scanf("%s%d%d",parray[var]->pid,&parray[var]->Atime,&parray[var]->Btime);
		}
	Sort_Btime(parray,n);
	//Print(parray,n);
	Schedule(parray,n);
	printf("\n\n\n\n");
	Print(parray,n);
	}
