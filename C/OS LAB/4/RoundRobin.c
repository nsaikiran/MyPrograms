/*
Scheduling Algorithm
Type: Round Robin
Author :saikira638
Assumption: All processes are assumed in sorted-sequence of their arrival times. (if not
			we will need another function to sort the processes)
*/

#include<stdio.h>
#include<stdlib.h>
#define MPID 10

typedef enum {false,true} Bool;

typedef struct node{
	char pid[MPID];
	int Atime;
	int Btime;
	int Ctime;
	struct node* nextProcess;
	}process;

int TQ=0;
process *head=NULL,*end=NULL,*queue_head=NULL,*queue_end=NULL;	

//This function used in creation of linked-list.
process* create(){
	process* temp=(process*)malloc(sizeof(process));	//allocate sufficient memory
	temp->Ctime=0;		//initialize completion time of the process to zero.
	temp->nextProcess=NULL;		//initialize next process to be NULL
	return temp;
	}
//This function is used in creation of linked-list of processes.
void Add(process* temp){
	end->nextProcess=temp;
	end=temp;
	}

//Utility function to print attributes/data of a process
void PrintProcess(process *pro){
	printf("\n%s %5d %5d %5d\n",pro->pid,pro->Atime,pro->Btime,pro->Ctime);
	}
//It prints whole list of processes...
void Print(){
	process* temp=head;
	printf("\nPID Atime Btime Ctime\n");
	for (;temp!=NULL;temp=temp->nextProcess){
		printf("\n%s %5d %5d %5d\n",temp->pid,temp->Atime,temp->Btime,temp->Ctime);
		}
	}
/*This function constitutes major part of the program, as it schedules the list
of processes using a queue.
* We will be using list of processes created while reading input(as we assume all processes 
	are in the sorted order) if not add a function that do sorting.

*/
void Schedule(){
	process* temp=NULL;
	queue_end=queue_head=head;
	head=head->nextProcess;
	queue_head->nextProcess=NULL;
	int cpu_time=queue_head->Atime;

	printf("\nAfter scheduling\n");
	while (queue_head || head){		//if at-least on element in queue or initial process list
		if (!queue_head){
			queue_end=queue_head=head;
			head=head->nextProcess;
			queue_head->nextProcess=NULL;
			cpu_time=queue_head->Atime;
			}
		if (queue_head->Btime <= TQ){
			cpu_time+=queue_head->Btime;
			queue_head->Btime=0;
			queue_head->Ctime=cpu_time;
			}
		else {
			cpu_time+=TQ;
			queue_head->Btime-=TQ;
			}
		while (head && head->Atime <= cpu_time){
			queue_end->nextProcess=head;
			head=head->nextProcess;
			queue_end=queue_end->nextProcess;
			}
		queue_end->nextProcess=NULL;
		if (queue_head->Btime){
			queue_end->nextProcess=queue_head;
			queue_head=queue_head->nextProcess;
			queue_end=queue_end->nextProcess;
			}
		else {
			PrintProcess(queue_head);
			temp=queue_head;
			queue_head=queue_head->nextProcess;
			free(temp);
			}
		queue_end->nextProcess=NULL;
		}
	}

int main(void){
	int N=0,var=0;
	process* temp=NULL;
	scanf("%d%d",&N,&TQ);
	if (N<=0)return 1;
	head=end=create();
	scanf("%s%d%d",head->pid,&head->Atime,&head->Btime);
	for (;var<N-1;++var){
		temp=create();
		scanf("%s%d%d",temp->pid,&temp->Atime,&temp->Btime);
		Add(temp);
		}
	Print();
	Schedule();
	return 0;
	}
