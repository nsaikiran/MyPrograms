_version_=2.0
def ChangeDir(Dir,Dir2):
	if Dir!=Dir2:
		os.system("..")

import os,posixpath as path,user
def ChangeMe(string):
	String=""
	for ele in range(len(string)):
		if string[ele] in ["!","@","#","$","%","^","&","*","(",")"," ","}","{","[","]","<",">"]:
			String=String+"\\"+string[ele]
		else:
			String=String+string[ele]
	return String

List=[".avi",".mkv",".flv",".mp4",".mp3",".3gp",".mpeg1",".mpeg2",".mpeg",".wmv",".AAC",".AC3",".ALAC",".AMR",".amr",".wma"]
Input=raw_input("Enter file name :: ")
os.chdir(user.home)
File="File.txt"
Result=[]

for Ext in List:
	os.system("locate "+Ext+" > "+File)
	f=open(File,"r")
	Result+=[x for x in f.read().split("\n") if path.basename(x).lower().find(Input) is not -1]

	f.close()
	os.remove(File)

_list1=[]
for r in Result:
	_list1+=[ChangeMe(r)]

list1=_list1
#print list1
if len(list1)==1:
	os.system("cvlc "+list1[0])
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
		os.system("cvlc "+STRING)
		x=raw_input("\n\nChoice : to exit 0 :")

print ("\n\nA program by saikiran N !!!!!\n") 
