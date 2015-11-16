#Importing a python file ....
import SearchForFiles,posixpath,os

Dict,Fol=SearchForFiles.SaiKiran("/home/RGUKT/",[],{})
x,Result2,List,Result=raw_input("Enter name :: "),[],[],[]

for y in [".avi",".mkv",".flv",".mp4",".mp3",".3gp",".mpeg1",".mpeg2",".mpeg",".wmv",".AAC",".AC3",".ALAC",".AMR",".amr",".wma"]:
	if y in Dict:
		result,Result=SearchForFiles.SearchForFiles(Dict[y],x,[]),[]
		for a in result:
			Result=Result+[a+y]
	Result2+=[Result]

for w in Result2:
	for a in w:
		List+=[a]

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

_list1=[]
for r in List:
	_list1+=[ChangeMe(r)]

list1=[]
for r in set(_list1):
	list1+=[r]

if len(list1)==1:
	os.system("vlc "+list1[0])
else:
	SAI={}
	for re in range(len(list1)):
		SAI[re+1]=list1[re]
	print "\nResults returned are %d files.\n"%len(list1)
	for w in range(1,len(SAI)+1):
		print "press %d to open '%s' .\n"%(w,SAI[w])
	x=raw_input("\n\nChoice : to exit 0 :")

	while x!='0':
		STRING=''
		for Ints in [int(strs) for strs in x.split(',') if int(strs) in SAI]:
			STRING+=SAI[Ints]+"  "
		os.system("vlc "+STRING)
		x=raw_input("\n\nChoice : to exit 0 :")

print ("\n\nA program by saikiran N !!!!!\n")
