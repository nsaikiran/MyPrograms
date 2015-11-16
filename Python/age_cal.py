import calendar as cal,time

def CheckMe(year,month,date):
	return 1<=month<=12 and cal.monthrange(year,month)[1]>=date

def End(Year,month,date):
	if not month-1:
		return date
	return date+End(Year,month-1,cal.monthrange(Year,month-1)[1])#recursion .....

def Leap(year):
	if cal.isleap(year):
		return 366
	return 365

def AgeDays(year,month,date,Year,Month,Date):
	start,end,List=End(year,month,date),End(Year,Month,Date),[]
	for years in range(year,Year):
		List,start=List+[(Leap(years)+1)-start],1
	return sum(List+[(end+1)-start])

#Program starts here ....

print " \n||| AGE CALCULATOR ||| \n\nEnter your DOB ::"

cur=time.asctime()
#declarations .....
Dict={"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}

Date,Year,Month=int(cur.split()[2]),int(cur.split()[-1]),Dict[cur.split()[1]]

year,month,date=input("YYYY :"),input("MM :"),input("DD :")

if CheckMe(year,month,date) and CheckMe(Year,Month,Date) and year<=Year:
	print "\n\n..::RESULTS::..\n\nYour age from (%d - %d - %d) To (%d - %d - %d) is %d day(s).\n"%(year,month,date,Year,Month,Date,AgeDays(year,month,date,Year,Month,Date))

else:
	raise ValueError("SaiKiran : Warning :an Error occured .")

"""
def Sai_Years():
	year,init,List=2012,0,[]
	for e in range(1,13):
		init+=cal.monthrange(year,e)[1]
		List+=[init]
	print List
Sai_Years()

def TestMe(num,num2,y,d):
	if 0<=num2-num:
		return 1,num2-num
	return num+1

def AgeYears(year,month,date,Year,Month,Date):
	st_y,YEARS,DAYS=year,0,0
	for years in range(year+1,Year):	
		print TestMe(AgeDays(st_y,month,date,years,month,date)-1,AgeDays(st_y,month,date,years,month,date)-1,YEARS,DAYS)
		st_y=st_y+1
	print TestMe(AgeDays(st_y,month,date,Year,month,date)-1,AgeDays(st_y,month,date,Year,Month,Date)-1,0,0)
#AgeYears(2001,2,3,2012,7,31)
#print AgeDays(2012,2,3,2012,7,31)

def Limit(num,num2,years,days):
	if num2>=num:
		print years
		return years+1,days+(num2-num)
	return years,days+num+1


def AgeYears(year,month,date,Year,Month,Date):
	st_y,st_m,st_d,ed_y,ed_m,ed_d,YEARS,DAYS=year,month,date,Year,Month,Date,0,0
	for years in range(year+1,Year):
		YEARS,DAYS=Limit(AgeDays(st_y,st_m,st_d,years,st_m,st_d)-1,AgeDays(st_y,st_m,st_d,years,st_m,st_d)-1,YEARS,DAYS)
		st_y=st_y+1
	print Limit(AgeDays(st_y,st_m,st_d,ed_y,ed_m,ed_d)-1,AgeDays(st_y,st_m,st_d,ed_y,month,date)-1,YEARS,DAYS)
	print AgeDays(st_y,st_m,st_d,ed_y,ed_m,ed_d)-1,AgeDays(st_y,st_m,st_d,ed_y,month,date)-2
	print year,month,date,Year,Month,Date
"""
