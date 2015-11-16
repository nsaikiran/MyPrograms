#Coding in Python ...
#Author : N SAIKIRAN

import time
def FindEvenNumbers(x):
	q=0
	Time=time.clock()
	for w in [y for y in range(x) if y%2==0]:
		q+=1

	print "\nTime elpased in seconds to find %d even number is %f .\n"%(q,time.clock()-Time)
FindEvenNumbers(input("Enter range to get number of even numbers :: "))
