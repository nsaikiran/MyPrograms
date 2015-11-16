"""
A program useful to open a directory by searching in the database .

AUTHOR : N SAIKIRAN 638 .
This program uses built-in modules os,posixpath,user etc , in it to open a directory . 
"""
import os,user,posixpath as sai

"""
AUTHOR ::N SAIKIRAN 638 .
	A program to open a directory by searching it in the datebase (especially in home folder ). 
"""

def ChangeMe(string,String):
	for ele in range(len(string)):
		if string[ele] in ["!","@","#","$","%","^","&","*","(",")"," ","}","{","[","]","<",">"]:
			String=String+"\\"+string[ele]
		else:
			String=String+string[ele]
	return String

def Dir(Folder):
	return [Folder+files+"/" for files in os.listdir(Folder) if sai.isdir(Folder+files)]

def Recur(List,Name):
	return [files for files in List if files.split("/")[-2].lower().find(Name.lower()) is not -1]

def Recursion(Folder,Result):
	Result=Result+Dir(Folder)
	for files in Dir(Folder):
		try:
			Result=Recursion(files,Result)
		except:pass
	return Result

#Execution starts ...
	
Name=raw_input("Enter directory name :: ")
RESULT=[]

home=user.home+"/"

for results in Recur(Recursion(home,[],),Name):
	new=''
	for result in results.split("/"):
		new=new+"/"+ChangeMe(result,'')
	RESULT=RESULT+[new]

"""
priting search results ..... 
"""

if len(RESULT)==1:
	"""
	executing a command to open a directory using the path of that directory on command line .
	"""
	os.system("nautilus "+RESULT[0])

elif not len(RESULT):
	"""
	No search results found .
	"""
	print "\n\n no directries found !!!!\n"
else:
	SAI={}
	for re in range(len(RESULT)):
		SAI[re+1]=RESULT[re]
	print "\nResults returned are %d directories .\n"%len(RESULT)
	for w in range(1,len(SAI)+1):
		print "press %d to open '%s' .\n"%(w,SAI[w])
	try:
		os.system("nautilus "+SAI[input("Enter ur choice ::: ")])
	except KeyError:
		print "\n\nWrong choice !!!!!\n\n"

print "\n\nA PROGRAM BY SAIKIRAN 638 .\n\n"
