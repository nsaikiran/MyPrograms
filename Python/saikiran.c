/*
AGE CALCULATOR , calculates age in  days ....
Author :: N SAI KIRAN .
*/

#include<stdio.h>
//prototypes of the functions ....
int sai(short,short,int);
int leap(int);
int MonthDays(short,int);
short Error(short,short,short,short,int,int);

void main(void)
	{
	short int  Month,Date,date,month;int Year,year,days=0,start,end,years;
	printf("\n...: AGE CALCULATOR :...\n\nEnter your DOB (Enter as date-month-year )::\n");
	scanf("%hd-%hd-%d",&date,&month,&year);
	printf("Your age up to (Enter as date-month-year):: \n");
	scanf("%hd-%hd-%d",&Date,&Month,&Year);
	if (!Error(date,Date,month,Month,year,Year))//if there is any error .. 
		printf("\n\nError :::: Please check input values you have given !!!!\n");
	else
		{
		start=sai(date,month,year);
		for (years=year;years<Year;++years)
			{
			end=leap(years)+1;
			days+=(end-start);
			start=1;
			}
		days+=((sai(Date,Month,Year)+1)-start);
		printf("\n\nUr age from (%hd-%hd-%d) to (%hd-%hd-%d) is %d day(s).\n",date,month,year,Date,Month,Year,days);
		//printf("\nError occured (1 - false , 0 - true) :: %d \n",Error(date,Date,month,Month,year,Year));
		}
	printf("\nA Program By :::-  Saikiran N .\nReport a bug N100638@nuz.rgukt.in\n");
	}

int MonthDays(short month,int year)
	{
	short x[]={31,28,31,30,31,30,31,31,30,31,30,31};
	if ((year%4==0)&&((year%400!=0)||(year%100!=0)))
		{
		x[1]=29;
		}
	return x[month];
	}

int sai(short date,short month,int year)
	{
	short b;
	for (b=0;b!=month-1;++b)
		{
		date+=MonthDays(b,year);
		}
	return (date);
	}

int leap(int year)
	{
	if ((year%4==0)&&((year%400!=0)||(year%100!=0)))
		return(366);
	return(365);
	}

short Error(short date,short Date,short month,short Month,int year,int Year)
	{
	return ((Year>=year)&&((1<=month<=12)&&(1<=Month<=12))&&(date<=MonthDays(month,year)&&Date<=MonthDays(Month,Year)))?1:0;
	}
