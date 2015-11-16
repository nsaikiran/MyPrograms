import os,posixpath,user,time

def delete(Home):
	for files in os.listdir(Home):
		if posixpath.isdir(Home+files+"/"):
			delete(Home+files+"/")
			os.rmdir(Home+files)
		else:
			os.remove(Home+files)

print "\n\n...:::: Unwanted File Remover :::...\n"

def SaiKiran(Home):
	List=['config.properties','java(new).policy','log4j.properties','NewClass.class']
	List2=['bean','com','display','META-INF','model','org','plugins','sample','support']

	for Files in os.listdir(Home):
		if posixpath.isdir(Home+Files+"/"):
			if Files in List2:
				delete(Home+Files+"/")
				os.rmdir(Home+Files+"/")
			else:
				SaiKiran(Home+Files+"/")	
		else:
			if Files in List:
				os.remove(Home+Files)
Time=time.clock()
SaiKiran(user.home+"/")
Time2=time.clock()
print "Time elapsed to remove files is %f"%(Time2-Time)
print "A program by saikiran638\n"
