import os,time,random,string
def Print(bredth):
	#print "\t"*3+"saikiran's"
	for s in range(bredth):
		print "\n"
#print " "*168

#space from the edge taken as 20 bytes .
string=raw_input("Enter a name :::: ")
string=string.upper()
base=" "*20
stri=" "
length=0
bredth=7
iteration=0

def Colouring(string):
	return "\033[1;"+str(random.choice(range(29,36)))+"m "+string+"\033[1;m"

while iteration<=10:
	Length,length=128-len(string),0
	while length<Length:
		os.system('clear')
		Print(bredth)#num2
		print base+stri*length+Colouring(string)+"\n"
		print "\n"+" "*148+"\033[1;34m by saikiran\033[1;m"
		time.sleep(.120)
		length+=1

	while length:
		os.system('clear')
		Print(bredth)#num2
		print base+stri*length+Colouring(string)+"\n"
		print "\n"+" "*148+"\033[1;34m by saikiran\033[1;m"
		time.sleep(.120)
		length-=1
	iteration+=1

