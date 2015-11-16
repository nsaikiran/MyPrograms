import platform,os,posixpath,user

"""
saikiran is a good boy ....
"""
#Function to search files
def SaiKiran(Home,Folders,Dict):
	try:
		for Files in os.listdir(Home):
			if posixpath.isdir(Home+Files+"/"):
				Folders=Folders+[Home+Files+"/"]
				SaiKiran(Home+Files+"/",Folders,Dict)	
			else:
				ext=posixpath.splitext(Home+Files)
				if ext[1] in Dict:
					Dict[ext[1]]+=[ext[0]]
				else:
					Dict[ext[1]]=[ext[0]]
	except OSError:
		print "you are unable to access :",Home
	return Dict,Folders
home=user.home+"/"
Dict,Folders=SaiKiran(home,[],{})

def SearchForFiles(Filenames,Input,List):
	for files in Filenames:
		try:
			Index=posixpath.split(files)[1].lower().index(Input.lower())
			List=List+[files]
		except ValueError:pass
	return List

#Starts .......This program is to open vlc based applications . .
#by saikiran 638
"""
Input=raw_input("Enter file name ::: ")

ext=posixpath.splitext(Input)
#print ext
#print Dict[ext[1]]
try:
	print "RESULTS :::::"
	for w in SearchForFiles(Dict[ext[1]],ext[0],[]):
		print w
except KeyError:
	print "extension does not exist ."
"""
