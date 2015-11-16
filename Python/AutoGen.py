#import os,posixpath as use,user

#def Config():
#	if use.exists(use.join(user.home,".AutoGen")):
#		print "T"
#	else:
#		print "F"
#f=open(use.join(user.home,".AutoGen"),"w")
#f.write("ET et MP mp PHY Phy phy Math2 MATH2 ENG eng PDS pds ")
#f.close()
#Config()

import user,os,posixpath as use,zipfile,shutil,random,sys

Logo="""
 _     ___  _        _ ___    _
|_|| |  |  | | |\/| |_| |  | |  
| ||_|  |  |_| |  | | | |  | |_
				FILE GENERATOR
"""
year='E1'
sub='ET MP PHY MATH ENG PDS ED CHEM ENM'
location='Documents'

if len(sys.argv)>1:
	if sys.argv[1]=='clear':
		os.remove(use.join(use.join(user.home),'.AutoGen'))
		print "\nHistory Cleared !!!\n"
		print "\n\n\033[1;"+str(random.choice(range(31,39)))+"m AUTHOR :: N SaiKiran N100638\033[1;m"
		print "\n\tUpdated soon with more options !!! ."
		quit()
	elif sys.argv[1]=='set':
		print "\nAutoGen - Set Up\n\n"
		config=open(use.join(user.home,'.AutoGen'),'w')
		config.write(raw_input("Enter your studying year (Ex :E1)")+'\n')
		config.write(raw_input("Enter where files to be generated (/home/RGUKT/+ ? ) or (home+ ?) (Ex :Documents ) :")+'\n')
		config.write(raw_input("Enter your subjects as a string separated by spaces (Ex: )::ET MP PHY MATH ENG .."))
		config.close()
		
year='E1'
sub='ET MP PHY MATH ENG PDS ED CHEM ENM'
location='Documents'
print "\033[1;"+str(random.choice(range(31,39)))+"m"+Logo+"\033[1;m"

if '.AutoGen' in os.listdir(user.home):
	config=open(use.join(user.home,'.AutoGen'),'r')
	temp=config.read()
	text=temp.split("\n")
	year=text[0]
	location=text[1]
	sub=text[2]
else:
	config=open(use.join(user.home,'.AutoGen'),'w')
	config.write(year+'\n')
	config.write(location+'\n')
	config.write(sub)
	config.close()
	print "SETTINGS ::\n\n\t:Default:\n\tYEAR:E1\n\tSUBJECTS:ET MP PHY MATH ENG PDS ED CHEM ENM"
	
ext=".jar"
home = user.home
path=use.join(home,use.join(location,"Xams"))

if not use.exists(path):
	os.mkdir(path)

def Extract(path,Result):
	for Files in Result:
		try:
			name=use.splitext(use.basename(Files))[0]
			os.mkdir(use.join(path,name))
			os.chdir(use.join(path,name))
			for files in zipfile.ZipFile(Files).namelist():
				if use.dirname(files)=='':
					if use.splitext(files)[1]=='.txt':
						zipfile.ZipFile(Files).extract(files)
			os.chdir(path)
		except OSError:pass

def files(link):return Separate(link,[files for files in os.listdir(link) if files[0]!='.'])

def Separate(path,List):
	Files,Folders=[],[]
	for files in List:
		if use.isdir(use.join(path,files)):
			 Folders.append(use.join(path,files))
	for files in List:
		if files not in Folders and use.splitext(files)[1]=='.jar':
			Files.append(use.join(path,files))
	return Folders,Files

Folders,Files=files(user.home)
x,y,Result=[],[],[]
for fol in Folders:
	x,y=files(fol)
	Folders+=x
	Files+=y
Final=[]
for files in Files:
	if use.splitext(use.basename(files))[0].upper().find(year)!=-1:
		Final.append(files)
#z="ET MP PHY MATH ENG PDS ED CHEM ENM"
text=sub.split()
SaiKiran={}
for sub in text:
	SaiKiran[sub]=[]
	for files in Final:
		if use.splitext(use.basename(files))[0].upper().find(sub)!=-1:
			SaiKiran[sub].append(files)
#print Dict
print "Year::",year,"\nSubjects ::: ",SaiKiran.keys()



def HTML(path):
	file_=open(use.join(path,use.basename(path)+'.htm'),"w")
	Str="<html><title>"+use.basename(path)+"</title><body>"
	Dict={}
	for files in os.listdir(path):
		if use.splitext(files)[1]=='.txt':
			Dict[int(use.splitext(files)[0])]=files
	list_=Dict.keys()
	list_.sort()
	for files in list_:
		Str+="<img src="+Dict[files]+">"
	file_.write(Str+"<br><br><font color='red'>&copy AUTOMATIC file generator</font></body></center></html>")
	file_.close()
#print Dict['ED']
for files in SaiKiran:
	#print Dict[files]
	if not SaiKiran[files]:continue
	if use.exists(use.join(path,"EXAM_"+files.upper())):
		os.chdir(use.join(path,"EXAM_"+files.upper()))
	else:
		os.mkdir(use.join(path,"EXAM_"+files.upper()))
		os.chdir(use.join(path,"EXAM_"+files.upper()))

	cur=os.getcwd()
	
	Extract(cur,SaiKiran[files])

	for files in os.listdir(cur):
		Dict,link={},use.join(cur,files)
		if use.isdir(link):
			for txt in os.listdir(link):
				if use.splitext(txt)[1]=='.txt':
					Dict[int(use.splitext(txt)[0])]=txt
			_list=Dict.keys()
			_list.sort()
			file_=open(use.join(link,use.basename(files))+'.htm',"w")
			Str="<html><title>"+use.basename(path)+"</title><body>"
			for files in _list:
				Str+="<img src="+Dict[files]+"><br>"
			file_.write(Str+"<br><br><font color='red'>&copy AUTOMATIC file generator</font></body></center></html>")
			file_.close()


	file_=open(use.join(os.getcwd(),"index.htm"),"w")
	Str="<html><title>"+sub.upper()+"</title><center><head><font color='green'>LIST OF FILES</font></head><br><br><br><br><table border='0'>"
	for files in os.listdir(cur):
		if use.isdir(use.join(os.getcwd(),files)):
			Str+="<tr><td><a href="+files+"/"+files+".htm>"+files+"</a></td></tr>"
	file_.write(Str+"</table><br><br><font color='red'>&copy AUTOMATIC file generator</font></body></center></html>")
	file_.close()

file_=open(path+"/index.htm","w")
Str="<html><title>EXAM FILES</title><center><head><font color='green' size='70'>SUBJECTS</font></head><br><br><br><br><table border='0'>"
for files in os.listdir(path):
	if use.isdir(use.join(path,files)):
		Str+="<tr><td><a href="+files+"/index.htm>"+files+"</a></td></tr>"
file_.write(Str+"</table><br><br><font color='red'>&copy AUTOMATIC file generator</font></body></center></html>")
file_.close()
print "\n\n\nCompleted Generating Files on ",path
print "\n\n\033[1;"+str(random.choice(range(31,39)))+"m AUTHOR :: N SaiKiran N100638\033[1;m"
print "\n\tUpdated soon with more options !!! ."

