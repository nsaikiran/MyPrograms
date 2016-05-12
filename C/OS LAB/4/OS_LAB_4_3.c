/*
Round Robin
All processes are assumed in sorted-sequence of their arrival times.
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
	int allotedTime;
	struct node* ptr;
	}process;

process* head=NULL,*end=NULL,*queue_head=NULL,*queue_end=NULL;
static int TQ;//Time Quantum

process* create(){
	process* temp=(process*)malloc(sizeof(process));
	temp->Ctime=0;
	temp->allotedTime=0;
	temp->ptr=NULL;
	return temp;
	}

void Add(process* temp){
	end->ptr=temp;
	end=temp;
	}

void print_result(process* temp){
	printf("%s %d %d\n",temp->pid,temp->Atime,temp->Ctime);
	free(temp);
	}
	
static void ShowCtime(process* p){
	printf("\n%s %d \n",p->pid,p->Ctime);
	}
	
void Schedule(){
	process *curr=NULL,*temp=NULL,*flag=NULL,*queue_head=NULL,*queue_end=NULL;
	
	queue_end=queue_head=head;
	head=head->ptr;				//update head as we inserted first process in queue
	queue_end->ptr=queue_head;	//circular double linked list with only one element in it .
	int cpu_time=queue_head->Atime;		//initialize cpu time with first process's arrival time
	
	
	}
	
void Print(){
	process* temp=head;
	while (temp){
		printf("%s %d %d %d\n",temp->pid,temp->Atime,temp->Btime,temp->Ctime);
		temp=temp->ptr;
		}
	}

int main(void){
	int n,var=0;
	process* temp=NULL;
	scanf("%d%d",&n,&TQ);
	if (n<=0)return 1;
	head=end=create();
	scanf("%s%d%d",head->pid,&head->Atime,&head->Btime);
	for (;var<n-1;++var){
		temp=create();
		scanf("%s%d%d",temp->pid,&temp->Atime,&temp->Btime);
		Add(temp);
		}
	Print();
	Schedule();
	return 0;
	}
