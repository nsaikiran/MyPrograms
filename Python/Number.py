#A program to represent the given number in words ..
import platform
def Add(List,st):#sub function ...
	for w in List:
		st=st+w
	return st.replace(st[1],st[1].upper(),1)+"."

def number(List,Number):#sub function ...
	List.sort()
	for w in List:
		if w<=Number:
			Max=w
	return Max

def SaiKiran(Number,String):#Main function .....
	#declarations ...........
	Dict={0:" zero",1:" one",2:" two",3:" three",4:" four",5:" five",6:" six",7:" seven",8:" eight",9:" nine",10:" ten",11:" eleven",12:" twelve",13:" thirteen",14:" fourteen",15:" fifteen",16:" sixteen",17:" seventeen",18:" eighteen",19:" nineteen",20:" twenty",30:" thirty",40:" fourty",50:" fifty",60:" sixty",70:" seventy",80:" eighty",90:" ninty",100:" one hundred",200:" two hundred",300:" three hundred",400:" four hundred",500:" five hundred",600:" six hundred",700:" seven hundred",800:" eight hundred",900:" nine hundred"}
	try:
		return String+Dict[Number]
	except KeyError:
		Max=number(Dict.keys(),Number)
		String=String+Dict[Max]
		return SaiKiran(Number-Max,String+"") #recursion ....

def Saikiran(Number,String):#Main function ...
	if Number>=1000:
		Dict={1000:" thousand",100000:" lakh",10000000:" crore"}
		Max=number(Dict.keys(),Number)
		if int(float(Number)/float(Max))==float(Number)/float(Max):
			return Saikiran(int(float(Number)/float(Max)),"")+Dict[Max]
		else:
			while Number>=Max:
				String,Number=String+SaiKiran(Number/Max,"")+Dict[Max]+" |",Number%Max
			return String+Saikiran(Number,"") #recursion .....
	else:
		return String+SaiKiran(Number,"")
print("\n\nREPRESENTION OF GIVEN NUMBER IN WORDS !!!!!!!!\n")
#Program starts .......................................................................................
if platform.system()=="Linux":#Condition on platform ...
	Result=Saikiran(input("\nEnter an integer  >>  "),"")#Program starts ......
	if Result.count("|")>=2:
		result=Result.split("|",Result.count("|")-1)
		result[-1]=result[-1].replace("|","and")
		print"\n\n",Add(result,""),"\n\n"
	else:
		result=Result.split("|")
		print"\n\n",Add(result,""),"\n\n"
else:
	print("This program needs some modifications !!!!")	
print "by - Saikiran N .\n"
