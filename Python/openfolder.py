"""
A program useful to search a directory in database & to open it .

\nAUTHOR : N SAIKIRAN 638 .
\nThis program uses built-in modules os,posixpath,user etc , in it to open a directory . 
"""
import os,user,posixpath as sai

def ChangeMe(string):
	"""
	\nThis method useful to make a path into a path that can be executable in command line.\nEx:'/home/My folder/Desktop/my * personal files' to '/home/My\ folder/Desktop/my\ \*\ personal\ files'
	"""
	String=""
	for ele in range(len(string)):
		if string[ele] in ["!","@","#","$","%","^","&","*","(",")"," ","}","{","[","]","<",">"]:
			String=String+"\\"+string[ele]
		else:
			String=String+string[ele]
	return String

def Dir(Folder):
	"""
	This function returns folders or directories in a directory .
	"""
	return [Folder+files+"/" for files in os.listdir(Folder) if sai.isdir(Folder+files)]

def Recur(List,Name):
	"""
	\n It is a sub-function used to search the directory in all directories . Mainly searching a string .\n
	"""
	return [files for files in List if files.split("/")[-2].lower().find(Name.lower()) is not -1]

def Recursion(Folder,Result):
	"""
	\n It is also a sub-function used by opendirs .\n
	"""
	Result=Result+Dir(Folder)
	for files in Dir(Folder):
		try:
			Result=Recursion(files,Result)
		except:pass
	return Result

def opendirs(Name):
	"""
	\nIt is Main method that can open a directory .\nopendirs(string) - > string is a directory name not path .\nIt open directory or directories  .\n
	"""
	RESULT=[]

	home=user.home+"/"

	for results in Recur(Recursion(home,[],),Name):
		new=''
		for result in results.split("/"):
			new=new+"/"+ChangeMe(result)
		RESULT=RESULT+[new]

	if not len(RESULT):
		print "No search results found .\n "
	elif len(RESULT)==1:
		os.system("nautilus "+RESULT[0])
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
		print "\n\nBy saikiran 638 .\n"
