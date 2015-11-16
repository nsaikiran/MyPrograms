import user,os
if "user.txt" in os.listdir(user.home):
	print "True"
F=open(user.home+"/user.txt","w")
F.write("saikiran ... \n")
F.close()

