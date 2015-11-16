"""
A program that produce fibonacci series with a1,a2 .
\nAuthor : N SAIKIRAN 638 .\n
"""
def Fibonacci(start,Start,End):
	
	"""
	start - > a1(int) ,Start - > a2(int) , End(int) up to the term .
	\n\nFibonacci series starts with a   , a    ........ a   , and continues ...
				       1     2             n
	a     = a  + a
	 n+1     n    n-1

	"""

	List,count=[start,Start],0
	for limit in range(End):
		List+=[start+Start]
		start,Start=List[-2],List[-1]
	return List

def Result():
	"""
	Used by Fibonacci method to print result ...
	"""

	print "Fibonacci series :::"
	for e in Fibonacci(input("a1 :"),input("a2 :"),input("up to term :")):
		print e,
