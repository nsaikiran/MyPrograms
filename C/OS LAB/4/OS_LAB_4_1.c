/*
Scheduling algorithm : FCFS

*/
#include<stdio.h>
#include<stdlib.h>
#define MPID 10
typedef struct {
	char pid[MPID];
	int Atime;
	int Btime;
	int Ctime;
}process;

void PSort(process** parray,int n)
	{
	int var=1,j;
	process* key=NULL;
	for (;var<n;++var){
		key=parray[var];
		j=var-1;
		while ( j >= 0 && parray[j]->Atime > key->Atime){
			parray[j+1]=parray[j];
			--j;
			}
		parray[j+1]=key;
		}
	}

void Schedule(process** parray,int n){
	int cpu_time=0,var=0;
	for (;var<n;++var){
		if (cpu_time < parray[var]->Atime)
			cpu_time=parray[var]->Atime;
		cpu_time+=parray[var]->Btime;
		parray[var]->Ctime=cpu_time;
		}
	printf("%10s %10s %10s %10s %10s %10s\n","PID","Atime","Btime","Ctime","TATime","WTime");
	for (var=0;var<n;++var)
		printf("%10s %10d %10d %10d %10d %10d\n",parray[var]->pid,parray[var]->Atime,
				parray[var]->Btime,parray[var]->Ctime,parray[var]->Ctime - parray[var]->Atime,
				parray[var]->Ctime - parray[var]->Atime - parray[var]->Btime);
	}

int main(void)
	{
	int n,var=0;
	scanf("%d",&n);
	process* parray[n];
	for (;var<n;++var)
		{
		parray[var]=(process*)malloc(sizeof(process));
		scanf("%s%d%d",parray[var]->pid,&parray[var]->Atime,&parray[var]->Btime);
		}
	PSort(parray,n);
	Schedule(parray,n);
	return 0;
	}
